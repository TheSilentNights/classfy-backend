# 定义一个函数来统计标签数量
def count_labels(file_path):
    # 初始化标签计数器
    label_counts = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

    # 打开文件并逐行读取
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 去掉行尾的换行符并分割行内容
            parts = line.strip().split()
            # 获取最后一部分作为标签
            if parts:  # 确保行不为空
                label = int(parts[-1])  # 假设标签是最后一部分且为整数
                if label in label_counts:
                    label_counts[label] += 1

    return label_counts


# 调用函数并打印结果
file_path = 'train.txt'  # 替换为你的文件路径
result = count_labels(file_path)
print("标签统计结果：")
for label, count in result.items():
    print(f"标签 {label}: {count}次")