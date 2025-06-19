from flask import Flask, request, jsonify
from flask_cors import CORS  # 处理跨域问题
import os

from sqlalchemy.testing.plugin.plugin_base import logging

import accept_image
from src.classify import Classify

app = Flask(__name__)
CORS(app)  # 允许所有域跨域访问


#确保大小可接受
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB

# 确保上传目录存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    """文件上传端点"""
    # 检查是否有文件部分
    if 'image' not in request.files:
        return jsonify({'error': '请求中未包含文件部分'}), 400

    file = request.files['image']

    # 调用服务层处理文件
    file_info, error = accept_image.handle(file)

    if error:
        return jsonify({'error': error}), 400

    return jsonify({
        'message': '文件上传成功',
        'filename': file_info['filename'],
        'original_name': file_info['original_name'],
        'size': file_info['size']
    }), 200


@app.route('/api/health', methods=['GET'])
def handle_data():
    return jsonify({"status":"success"})

@app.route('/api/classify',methods=['GET'])
def classify():
    classify = Classify(request.args.get('filename'))
    result = classify.classify()
    return jsonify({"categeory":result})

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

if __name__ == '__main__':
    app.run(debug=True,port=7777)
