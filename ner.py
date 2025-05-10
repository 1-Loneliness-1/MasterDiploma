import spacy

from PyQt6.QtCore import QThread, pyqtSignal


class MedicalNER(QThread):
    signal_with_res = pyqtSignal(object)
    signal_with_error = pyqtSignal(str)

    def __init__(self, transcribed_text, spacy_model="spacy_retrain/pretrained_med_model/model-best"):
        super().__init__()
        self.nlp = None
        self.spacy_model = spacy_model
        self.text_for_ner = transcribed_text
        self.entity_types = ["Drugname", "symptom", "procedure"]

    def run(self):
        try:
            if self.nlp is None:
                self.nlp = spacy.load(self.spacy_model)

            # Извлечение сущностей
            doc = self.nlp(self.text_for_ner)
            entities = {label: [] for label in self.entity_types}

            for ent in doc.ents:
                if ent.label_ in self.entity_types:
                    entities[ent.label_].append({
                        "text": ent.text,
                        "start": ent.start_char,
                        "end": ent.end_char
                    })

            res_dictionary = {
                "text": self.text_for_ner,
                "entities": entities
            }
            self.signal_with_res.emit(res_dictionary)
        except Exception as e:
            self.signal_with_error.emit(f"Ошибка распознавания сущностей: {e}")
        finally:
            self.nlp = None
