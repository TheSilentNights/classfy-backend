import os
from transformers import BertTokenizer
import torch
from src.bert.bert_get_data import BertClassifier

bert_name = 'D:/web/project/classfy-backend/src/bert/bert-base-chinese'


tokenizer = BertTokenizer.from_pretrained(bert_name)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

save_path = "D:/web/project/classfy-backend/src/bert/bert_checkpoint"
model = BertClassifier()
model.load_state_dict(torch.load(os.path.join(save_path, 'best.pt')))
model = model.to(device)
model.eval()

real_labels = []
with open('D:/web/project/classfy-backend/src/bert/math/data/class.txt', 'r', encoding='utf-8') as f:
    for row in f.readlines():
        real_labels.append(row.strip())

def get_last_clause(s):
    if not s:
        return ""

    # 定义分句分隔符（包括中英文常见标点）
    delimiters = set(',.!?;:，。！？；：')
    n = len(s)
    end_index = n - 1

    # 步骤1：跳过末尾的分隔符和空白字符
    while end_index >= 0 and (s[end_index] in delimiters or s[end_index].isspace()):
        end_index -= 1

    # 整个字符串都是分隔符或空白
    if end_index < 0:
        return ""

    # 步骤2：向前查找最后一个分句的起始位置（即最近的分隔符）
    start_index = 0
    found_delimiter = False
    for i in range(end_index, -1, -1):
        if s[i] in delimiters:
            start_index = i + 1  # 分句起始位置是分隔符的下一个字符
            found_delimiter = True
            break

    # 步骤3：提取分句并去除首尾空白
    last_clause = s[start_index:end_index + 1].strip()
    return last_clause


def start_classifier(text):

    # text = remove_last_sentence(text)
    bert_input = tokenizer(text, padding='max_length',
                           max_length=35,
                           truncation=True,
                           return_tensors="pt")
    input_ids = bert_input['input_ids'].to(device)
    masks = bert_input['attention_mask'].unsqueeze(1).to(device)
    output = model(input_ids, masks)
    pred = output.argmax(dim=1)

    print(real_labels[pred.item()])
    return real_labels[pred.item()]

while True:
    text = input('请输入题目：')
    # 删除最后一个逗号之前的内容
    text2 = get_last_clause(text)
    print(text2)
    bert_input = tokenizer(text2, padding='max_length',
                           max_length=35,
                           truncation=True,
                           return_tensors="pt")
    input_ids = bert_input['input_ids'].to(device)
    masks = bert_input['attention_mask'].unsqueeze(1).to(device)
    output = model(input_ids, masks)
    pred = output.argmax(dim=1)
    print(real_labels[pred.item()])
