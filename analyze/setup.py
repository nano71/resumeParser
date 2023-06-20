from setuptools import setup

setup(
    name='ecloud_python_sdk',
    version='1.1.0',
    url="https://ecloud.10086.cn",
    packages=[
        'ocr_ecloud',
    ],
    author='ocr_ecloud',
    description='Ecloud AI SDK',
    install_requires=[
        'requests',
    ],
)
