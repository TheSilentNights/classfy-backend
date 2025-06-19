import os
from transformers import BertTokenizer
import torch
from src.bert.bert_get_data import BertClassifier


def remove_last_sentence(text):
    # 找到最后一个逗号的位置
    last_period_index = text.rfind('.')
    # 如果没有找到逗号，返回原始文本
    if last_period_index == -1:
        return text
    # 删除最后一个逗号之前的内容，包括逗号
    return text[:last_period_index]


def start_classifier(text):
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

# while True:
#     text = input('请输入题目：')
#     # 删除最后一个逗号之前的内容
#     text = remove_last_sentence(text)
#     bert_input = tokenizer(text, padding='max_length',
#                            max_length=35,
#                            truncation=True,
#                            return_tensors="pt")
#     input_ids = bert_input['input_ids'].to(device)
#     masks = bert_input['attention_mask'].unsqueeze(1).to(device)
#     output = model(input_ids, masks)
#     pred = output.argmax(dim=1)
#     print(real_labels[pred.item()])
