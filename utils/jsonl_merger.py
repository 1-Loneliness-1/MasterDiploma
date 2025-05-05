# Функция объединения нескольких файлов датасетов в формате jsonl в один для дальнейшего дообучения spacy
def merge_jsonl_files(input_files, output_file):
    with open(output_file, mode='w', encoding='utf-8') as out_file:
        for jsonl_file in input_files:
            with open(jsonl_file, mode='r', encoding='utf-8') as current_json_file:
                for line in current_json_file:
                    if line.strip():
                        out_file.write(line.strip() + '\n')