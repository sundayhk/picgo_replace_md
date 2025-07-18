import os
import re
import sys
from urllib.parse import urlparse
import requests

def picgo_upload(url):
    data = {"list": [url]}
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(
            'http://127.0.0.1:36677/upload',
            json=data,
            headers=headers
        )
        response.raise_for_status()
        data = response.json()
        if data['success']:
            return data['result'][0]
        return None
    except requests.RequestException as e:
        print("请求失败:", e)
        return None

# 定义文本文件扩展名
text_extensions = ['.txt', '.md']
# 正则表达式匹配图片 Markdown 语法
pattern = re.compile(r'!\[.*?\]\((https?://.*?)\)')
oss_url = "http://oss.sundayhk.com"

def process_file(file_path):
    """
    处理单个文本文件，替换其中符合条件的图片链接
    :param file_path: 要处理的文件路径
    """
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        new_lines = []
        for line in lines:
            matches = pattern.findall(line)
            for url in matches:
                if not url.startswith(oss_url):
                    oss_url = picgo_upload(url)
                    if oss_url:
                        print(oss_url)
                        line = line.replace(url, oss_url)
            new_lines.append(line)

        # 写入修改后的内容
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(new_lines)

    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")

def dir_file_list_process(current_dir):
    # 遍历当前目录下的一级文件
    for file_name in os.listdir(current_dir):
        file_path = os.path.join(current_dir, file_name)
        # 检查是否为文件且扩展名符合要求
        if os.path.isfile(file_path) and any(file_name.lower().endswith(ext) for ext in text_extensions):
            process_file(file_path)
    print("处理完成")
    
# 获取命令行参数
args = sys.argv[1:]

if len(args) > 2:
    print("参数数量不能超过 2 个，请检查输入。")
    sys.exit(1)
elif len(args) == 1:
    # 处理文件或目录
    file_path = args[0]
    if os.path.isfile(file_path) and any(file_path.lower().endswith(ext) for ext in text_extensions):
        process_file(file_path)
    else:
        dir_file_list_process(file_path)
else:
    # 获取当前目录
    current_dir = os.getcwd()
    dir_file_list_process(current_dir)


