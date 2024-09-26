import re
import os

def is_valid_two_letter_group(line):
    # 去除行首尾的空白字符
    line = line.strip()

    # 检查是否只包含恰好两个英文字母
    return bool(re.match(r'^[a-zA-Z]{2}$', line))

def check_file(filename):
    print(f"\nChecking file: {filename}")
    with open(filename, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, 1):
            if is_valid_two_letter_group(line):
                print(f"Line {line_number}: Valid - {line.strip()}")
            else:
                pass
                # print(f"Line {line_number}: Invalid - {line.strip()}")

def scan_directory():
    current_dir = os.getcwd()
    for filename in os.listdir(current_dir):
        if filename.endswith('.txt'):
            check_file(filename)

# 执行扫描
scan_directory()
