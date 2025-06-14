from paddleocr import PaddleOCR

# 初始化PaddleOCR实例（使用PP-OCRv4模型）
ocr = PaddleOCR(
    use_doc_orientation_classify=True, # 启用方向分类
    lang='ch',           # 中文识别（支持中英文混合）      # 根据环境选择是否使用GPU
    ocr_version='PP-OCRv4',  # 指定使用v4模型       # 关闭日志输出
)

def recognize_and_print(image_path):
    """
    识别图片中的文字并打印到终端
    :param image_path: 图片路径
    """
    # 执行OCR识别
    result = ocr.predict(image_path)

    # 提取所有识别文本
    result_text=""
    for res in result:
        for text in res["rec_texts"]:
            result_text = result_text + text
    print(result_text)

if __name__ == "__main__":
    # 替换为你的图片路径
    image_path = 'page_1.png'  # 或使用绝对路径如：r'C:\path\to\image.jpg'
    recognize_and_print(image_path)