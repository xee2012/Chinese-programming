# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Chinese programming',
    version='0.1.0',
    packages=find_packages(),
    description='A package that allows writing Python code in Chinese.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Your Name',
    author_email='your.email@example.com',
    keywords='python chinese programming',
    url='https://github.com/yourusername/chinese-programming',  # 你的项目主页
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/chinese-programming/issues",
        "Documentation": "https://github.com/yourusername/chinese-programming/README.md",
        "Source Code": "https://github.com/yourusername/chinese-programming",
    },
    classifiers=[
        # 选择适当的分类器来描述你的项目
        # For a full list, see https://pypi.org/classifiers/
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # 举例，根据你的许可证修改
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 指定Python版本要求
    install_requires=[  # 你的包依赖的其他包
        # 'package_name>=version',
    ],
    entry_points={  # 如果你的包提供了命令行工具，可以在这里指定
        'console_scripts': [
            'chinese-code-executor=chinese_code_executor:main',
        ],
    },
)