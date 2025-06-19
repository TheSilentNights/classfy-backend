from flask import current_app
import os

class Classify:
    def __init__(self,saved_file_name):
        path_to_file = os.path.join(current_app.config['UPLOAD_FOLDER'],saved_file_name)