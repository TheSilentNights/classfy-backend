
import os
from datetime import datetime
from werkzeug.utils import secure_filename
from flask import current_app

def handle(file):
    if file.filename == '':
        return None, '未选择文件'

    if not allowed_file(file.filename):
        return None, '不允许的文件类型'

    try:
        # 生成安全文件名
        original_filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{timestamp}_{original_filename}"

        # 获取上传目录配置
        upload_folder = current_app.config['UPLOAD_FOLDER']

        # 确保目录存在
        os.makedirs(upload_folder, exist_ok=True)

        # 保存文件
        save_path = os.path.join(upload_folder, filename)
        file.save(save_path)

        return {
            'filename': filename,
            'original_name': original_filename,
            'path': save_path,
            'size': os.path.getsize(save_path)
        }, None

    except Exception as e:
        current_app.logger.error(f"文件保存失败: {str(e)}")
        return None, f"服务器错误: {str(e)}"


def allowed_file(filename):
    """检查文件扩展名是否允许"""
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in allowed_extensions
