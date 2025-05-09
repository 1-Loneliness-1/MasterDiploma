import random

from spacy.tokens import DocBin
from spacy.lang.ru import Russian
from spacy.util import get_lang_class

from spacy_retrain.data_for_train import train_data


def split_spacy_to_train_and_dev(
        input_path: str,
        train_path: str,
        dev_path: str,
        dev_ratio: float = 0.2,
        lang: str = "ru",
        seed: int = 42
):

    nlp = get_lang_class(lang)()
    doc_bin = DocBin().from_disk(input_path)
    docs = list(doc_bin.get_docs(nlp.vocab))

    random.seed(seed)
    random.shuffle(docs)
    split_idx = int(len(docs) * (1 - dev_ratio))
    train_docs = docs[:split_idx]
    dev_docs = docs[split_idx:]

    train_bin = DocBin(docs=train_docs)
    train_bin.to_disk(train_path)

    dev_bin = DocBin(docs=dev_docs)
    dev_bin.to_disk(dev_path)



def convert_data_to_spacy_and_save(training_data):
    nlp = Russian()
    docbin = DocBin()

    for text, annotations in training_data:
        doc = nlp(text)
        entities = []

        for start, end, label in annotations["entities"]:
            span = doc.char_span(start, end, label=label, alignment_mode="contract")
            if span is not None:
                entities.append(span)

        doc.ents = entities
        docbin.add(doc)

    docbin.to_disk("train.spacy")


if __name__ == '__main__':
    # convert_data_to_spacy_and_save(train_data)
    split_spacy_to_train_and_dev(
        input_path="train.spacy",
        train_path="train_split.spacy",
        dev_path="dev_split.spacy",
        dev_ratio=0.2,
        lang="ru"
    )
