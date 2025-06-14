from flask import Flask, request, jsonify
from flask_cors import CORS  # 处理跨域问题

app = Flask(__name__)
CORS(app)  # 允许所有域跨域访问

@app.route('/api/health', methods=['GET'])
def handle_data():
    return jsonify({"status":"success"})

@app.route('/api/upload',methods=['POST'])
def handle_img():

if __name__ == '__main__':
    app.run(debug=True,port=7777)