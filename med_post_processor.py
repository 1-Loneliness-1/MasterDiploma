import re
from spacy.tokens import Span


class MedicalPostProcessor:
    def __init__(self, nlp):
        self.nlp = nlp
        self.entity_types = {
            "DIAGNOSIS": "DIAGNOSIS",
            "MEDICINE": "Drugname",
            "PROCEDURE": "PROCEDURE"
        }
        self.drug_lexicon = self.load_drug_lexicon()
        self.abbr_map = self.load_abbreviations()

    def load_drug_lexicon(self):
        return {
            "амоксиклав": "Амоксиклав",
            "амоксиклав-дуо": "Амоксиклав",
            "аугментин": "Амоксициллин/клавуланат",
            "цефтриаксон-дуф": "Цефтриаксон",
            "цефтриаксон-эльфа": "Цефтриаксон",
            "энап": "Эналаприл",
            "престариум": "Периндоприл",
            "конкор": "Бисопролол",
            "метапролол": "Метопролол",
            "небивал": "Небиволол",
            "аналог": "Анальгин",
            "кетанов": "Кеторолак",
            "дексалгин": "Декскетопрофен",
            "аспекард": "Ацетилсалициловая кислота",
            "тромбо-асс": "Ацетилсалициловая кислота",
            "метаформин": "Метформин",
            "глибомет": "Глибенкламид + метформин",
            "аторис": "Аторвастатин",
            "розувастатин-сз": "Розувастатин"
        }

    def load_abbreviations(self):
        return {
            'ХСН': 'хроническая сердечная недостаточность',
            'ОКС': 'острый коронарный синдром',
            "ИБС": "ишемическая болезнь сердца",
            "ГБ": "гипертоническая болезнь",
            "ХОБЛ": "хроническая обструктивная болезнь легких",
            "ЯБЖ": "язвенная болезнь желудка",
            "ОИМ": "острый инфаркт миокарда",
            "ОНМК": "острое нарушение мозгового кровообращения",
            "ДН": "дыхательная недостаточность",
            "ХПН": "хроническая почечная недостаточность",
            "ЭКГ": "электрокардиография",
            "ФГДС": "фиброгастродуоденоскопия",
            "УЗДГ": "ультразвуковая допплерография",
            "КТ": "компьютерная томография",
            "МРТ": "магнитно-резонансная томография",
            "ОАК": "общий анализ крови",
            "БАК": "биохимический анализ крови",
            "ОАМ": "общий анализ мочи",
            "СОЭ": "скорость оседания эритроцитов",
            "ЛДГ": "лактатдегидрогеназа"
        }

    def apply_rules(self, doc):
        rules = [
            self.correct_drug_spelling,
            self.expand_abbreviations,
            self.merge_composite_terms,
            self.correct_lab_values
        ]

        for rule in rules:
            doc = rule(doc)

        return doc

    def correct_drug_spelling(self, doc):
        for ent in doc.ents:
            if ent.label_ == "MEDICINE" and ent.text.lower() in self.drug_lexicon:
                ent.corrected_text = self.drug_lexicon[ent.text.lower()]
        return doc

    def expand_abbreviations(self, doc):
        for token in doc:
            if token.text in self.abbr_map:
                token.expanded_form = self.abbr_map[token.text]
        return doc

    def merge_composite_terms(self, doc):
        new_ents = []
        for ent in doc.ents:
            if ent.label_ == "DIAGNOSIS" and " " not in ent.text:
                next_token = doc[ent.end]
                if next_token.text == "-" or next_token.text.isdigit():
                    new_ent = Span(doc, ent.start, ent.end + 1, label="DIAGNOSIS")
                    new_ents.append(new_ent)
            else:
                new_ents.append(ent)
        doc.ents = new_ents
        return doc

    def correct_lab_values(self, doc):
        lab_patterns = [
            (r"(\d+)\s*мм/ч", "\\1 мм/ч"),
            (r"(\d+)\s*г/л", "\\1 г/л")
        ]
        for match, repl in lab_patterns:
            doc.text = re.sub(match, repl, doc.text)
        return self.nlp(doc.text)
