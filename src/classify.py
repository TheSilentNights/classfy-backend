from flask import current_app
import os
from bert import bert_tuili
from src.ocr import recognize


class Classify:
    def __init__(self, saved_file_name):
        self.path_to_file = os.path.join(current_app.config['UPLOAD_FOLDER'], saved_file_name)

    def classify(self):
        text_content = recognize(image_path=self.path_to_file)
        bert_tuili.start(text_content)


if __name__ == '__main__':
    os.environ['HF_ENDPOINT'] = "https://hf-mirror.com"
    path_to_img = "D:/web/project/classfy-backend/test/page_1.png"
    classifier = Classify(path_to_img)
    classifier.classify()
