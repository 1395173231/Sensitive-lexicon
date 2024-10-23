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

def remove_strings_from_file(filename, strings_to_remove):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            if line.strip() not in strings_to_remove:
                file.write(line)

def process_files_in_directory(strings_to_remove):
    current_dir = os.getcwd()
    for filename in os.listdir(current_dir):
        if filename.endswith('.txt'):
            remove_strings_from_file(filename, strings_to_remove)
            print(f"Processed file: {filename}")

def is_pure_letters(line):
    # 检查是否只包含英文字母（可以包含空白字符）
    return bool(re.match(r'^[a-zA-Z\s]+$', line.strip()))

def remove_pure_letters_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            if not is_pure_letters(line):
                file.write(line)

def process_files_remove_pure_letters():
    current_dir = os.getcwd()
    for filename in os.listdir(current_dir):
        if filename.endswith('.txt'):
            remove_pure_letters_from_file(filename)
            print(f"Removed pure letters from file: {filename}")

# 主程序
if __name__ == "__main__":
    # 执行扫描
    scan_directory()

    # 移除指定字符串
    strings_to_remove = ["信访"]  # 要移除的字符串列表
    process_files_in_directory(strings_to_remove)

    # 移除纯字母行
    process_files_remove_pure_letters()