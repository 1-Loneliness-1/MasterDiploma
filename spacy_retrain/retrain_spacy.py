import json
import spacy
from pathlib import Path
from spacy.tokens import DocBin
from spacy.training import Example
from utils.jsonl_merger import merge_jsonl_files


def load_rumedbench_bio(path, nlp):
    output_docbins = []
    with open(path, mode='r', encoding='utf-8') as file_with_data_in_bio_format:
        for line in file_with_data_in_bio_format:
            example = json.loads(line)
            tokens = example["tokens"]
            tags = example["ner_tags"]

            text = " ".join(tokens)
            output_docbins = nlp.make_doc(text)

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
                span = output_docbins.char_span(start_char, end_char, label=label, alignment_mode="contract")
                if span:
                    entities.append(span)

            output_docbins.ents = entities
            output_docbins.append(output_docbins)
    return output_docbins


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


def convert_and_save_to_spacy(docs, output_path):
    doc_bin = DocBin()
    for doc in docs:
        doc_bin.add(doc)
    doc_bin.to_disk(output_path)


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

    nlp.to_disk(model_output_dir)


if __name__ == "__main__":
    name_of_path_with_datasets = "../datasets"
    file_with_training_data_for_spacy = "train_data.spacy"
    name_of_retrained_model = "retrained_model"
    input_jsonl_file = "merged.jsonl"

    # Объединение всех jsonl-файлов из папки "datasets" для дообучения spacy
    path_with_datasets = Path(name_of_path_with_datasets)
    jsonl_files = sorted(path_with_datasets.glob("*.jsonl"))
    merge_jsonl_files(jsonl_files, input_jsonl_file)

    # Дообучение spacy
    nlp = spacy.blank("ru")
    docs = load_rumedbench_bio(input_jsonl_file, nlp)
    convert_and_save_to_spacy(docs, file_with_training_data_for_spacy)
    train_spacy_model(file_with_training_data_for_spacy, name_of_retrained_model)
