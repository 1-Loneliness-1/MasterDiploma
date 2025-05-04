import json
import spacy
from pathlib import Path
from spacy.tokens import DocBin
from spacy.training import Example

def bio_to_entities(labels):
    entities = []
    start = None
    label = None

    for i, tag in enumerate(labels):
        if tag.startswith("B-"):
            if start is not None:
                entities.append((start, end, label))
            label = tag[2:]
            start = i
            end = i + 1
        elif tag.startswith("I-") and start is not None:
            end = i + 1
        else:
            if start is not None:
                entities.append((start, end, label))
                start = None
                label = None
    if start is not None:
        entities.append((start, end, label))
    return entities

def load_rumedbench_bio(path, nlp):
    docs = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            example = json.loads(line)
            tokens = example["tokens"]
            tags = example["ner_tags"]

            text = " ".join(tokens)
            doc = nlp.make_doc(text)

            current_pos = 0
            token_offsets = []

            for token in tokens:
                start = text.find(token, current_pos)
                end = start + len(token)
                token_offsets.append((start, end))
                current_pos = end

            entities = []
            for ent_start, ent_end, label in bio_to_entities(tags):
                start_char = token_offsets[ent_start][0]
                end_char = token_offsets[ent_end - 1][1]
                span = doc.char_span(start_char, end_char, label=label, alignment_mode="contract")
                if span:
                    entities.append(span)

            doc.ents = entities
            docs.append(doc)
    return docs

def convert_and_save_to_spacy(docs, output_path):
    doc_bin = DocBin()
    for doc in docs:
        doc_bin.add(doc)
    doc_bin.to_disk(output_path)
    print(f"Сохранено в spaCy формате: {output_path}")

def train_spacy_model(train_path, model_output_dir="output_model"):
    nlp = spacy.blank("ru")

    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner", last=True)

    doc_bin = DocBin().from_disk(train_path)
    docs = list(doc_bin.get_docs(nlp.vocab))

    for doc in docs:
        for ent in doc.ents:
            ner.add_label(ent.label_)

    examples = [Example.from_dict(nlp.make_doc(doc.text), {
        "entities": [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]
    }) for doc in docs]

    nlp.begin_training()
    for i in range(10):
        losses = {}
        nlp.update(examples, drop=0.2, losses=losses)
        print(f"Эпоха {i+1}: {losses}")

    nlp.to_disk(model_output_dir)
    print(f"[✓] Модель сохранена в: {model_output_dir}")

def merge_jsonl_files(input_files, output_file):
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for file_path in input_files:
            with open(file_path, 'r', encoding='utf-8') as in_f:
                for line in in_f:
                    if line.strip():  # пропуск пустых строк
                        out_f.write(line.strip() + '\n')
    print(f"Объединено {len(input_files)} файлов → {output_file}")

if __name__ == "__main__":
    path_with_datasets = Path("datasets")
    input_json_file = "merged.jsonl"
    jsonl_files = sorted(path_with_datasets.glob("*.jsonl"))
    merge_jsonl_files(jsonl_files, input_json_file)

    spacy_output = "train_data.spacy"
    model_output = "retrained_model"
    nlp = spacy.blank("ru")
    docs = load_rumedbench_bio(input_json_file, nlp)
    convert_and_save_to_spacy(docs, spacy_output)
    train_spacy_model(spacy_output, model_output)
