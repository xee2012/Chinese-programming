# setup.py

from setuptools import setup, find_packages

# 读取README.md作为长描述
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    # 包的名称
    name='Chinese-programming',
    # 包的版本号
    version='0.1.0',
    # 包的作者
    author='gosling',
    # 包的作者电子邮件
    author_email='zhchxee@outlook.com',
    # 包的描述
    description='A Python package that allows writing code using Chinese keywords.',
    # 长描述，通常从README.md读取
    long_description=long_description,
    # 长描述的内容类型
    long_description_content_type="text/markdown",
    # 包的URL
    url='https://github.com/xee2012/Chinese-programming',
    # 包的许可证
    license='MIT',  # 根据你的项目许可证进行修改
    # 包的分类器
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 包的Python版本要求
    python_requires='>=3.6',
    # 包的依赖
    install_requires=[
        # 'numpy>=1.18.1',  # 示例，根据你的项目依赖进行修改
    ],
    # 包包含的包和模块
    packages=find_packages(),
    # 包的入口点，如果库提供命令行工具
    entry_points={
        'console_scripts': [
            # 'chinese-prog=chinese_programming.module:main_function',  # 示例
        ],
    },
    # 包含额外的文件
    include_package_data=True,
    # 额外的数据文件
    package_data={
        # 如果你的包有额外的数据文件，可以在这里指定
        # 'package_name': ['data/*.dat'],
    },
)
