from setuptools import setup, find_packages

setup(
    name='tools3',  # 库名
    version='0.1.1',  # 版本号
    author='qq1060656096',  # 作者名
    author_email='1060656096@qq.com',  # 作者邮箱
    description='develop tools',  # 简短描述
    long_description=open('README.md').read(),  # 长描述，通常从 README.md 读取
    long_description_content_type='text/markdown',  # 描述内容类型
    url='https://github.com/qq1060656096',  # 项目主页
    packages=find_packages(),  # 自动查找包
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'tools3-cli=tools3.cli.cli:run',  # 入口点，格式为 '命令名=模块名:函数名'
        ],
    },
    python_requires='>=3.10',  # Python 版本要求
    package_data={
        "tools3": ["data/*.*", "data/**/*"],  # 包含data目录及其所有子目录
    },
    # 如果有依赖项，可以在这里列出
    install_requires=[
        "loguru==0.7.3",
        "langchain-community==0.3.19",
        "langchain-core==0.3.43",
        "langchain-ollama==0.2.3",
        "langchain-openai==0.2.14"
    ],
)
