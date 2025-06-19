def extract_category_1(input_file, output_file):
    try:
        # 打开输入文件进行读取
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 筛选出类别为1的内容
        category_1_lines = [line for line in lines if line.strip().endswith('4')]

        # 将筛选出的内容写入输出文件
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(category_1_lines)

        print(f"成功提取类别为1的内容，并保存到文件 {output_file} 中。")
    except FileNotFoundError:
        print(f"错误：文件 {input_file} 未找到，请确保文件路径正确。")
    except Exception as e:
        print(f"发生错误：{e}")


# 输入文件和输出文件的路径
input_file_path = 'train.txt'  # 输入文件名
output_file_path = '4xl.txt'  # 输出文件名

# 调用函数执行提取操作
extract_category_1(input_file_path, output_file_path)