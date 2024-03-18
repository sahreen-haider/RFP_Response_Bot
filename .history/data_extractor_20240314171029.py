import os


def extract_text(path):
    text_data = dict()
    for root, dirs, files in os.dir(path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
