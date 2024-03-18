import os


def extract_text(path):
    text_data = dict()
    for filename in os.listdir(path):
        if filename.endswith(".txt"):
            file_path = os.path.join(str(path+filename))
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                return text   


extract_text("/Volumes/Extended/projects/RFP Bot/file injest")