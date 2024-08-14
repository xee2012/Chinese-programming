# chinese_code_executor.py

import sys
import argparse

# 版本检查
if sys.version_info < (3, 0, 0):
    raise ImportError("This package requires Python 3.0.0 or above.")


# 定义中文函数名和变量
def 打印(*args, **kwargs): print(*args, **kwargs)


def 输入(*args, **kwargs): input(*args, **kwargs)


真 = True
假 = False
范围 = range
整数 = int
小数 = float
长度 = len

# 定义中文关键字替换为Python关键字的字典
replace_dic = {
    '定义': 'def',
    '类': 'class',
    '导入': 'import',
    '是': 'is',
    '返回': 'return',
    '送代循环': 'for',
    "‘": "'",
    "’": "'",
    '的': '.',
    "“": '"',
    "”": '"',
    '（': '(',
    '）': ')',
    '《': '<',
    '》': '>',
}


def replace_keys_with_values(input_string, key_value_dict):
    for key in key_value_dict:
        input_string = input_string.replace(key, key_value_dict[key])
    return input_string


def execute_chinese_code(file_path):
    """
    读取并执行指定路径的中文Python代码文件。
    """
    try:
        with open(file_path, encoding='utf-8') as f:
            cn_code = f.read()

        trans_code = replace_keys_with_values(cn_code, replace_dic)
        exec(trans_code)
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 未找到。")
        sys.exit(1)
    except Exception as e:
        print(f"执行时发生错误：{e}")
        sys.exit(1)


def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="执行中文编写的Python代码。")
    parser.add_argument("file_path", type=str, help="要执行的中文Python代码文件的路径")

    # 解析命令行参数
    args = parser.parse_args()

    # 执行中文代码
    execute_chinese_code(args.file_path)


if __name__ == "__main__":
    main()