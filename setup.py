
# -*- encoding: UTF-8 -*-
from setuptools import setup,find_packages

setup(
    name = "UpdateSystem",          # 包名
    version = "0.1",              # 版本信息
    packages = find_packages('lib'),  # 要打包的项目文件夹
    package_dir={ '': 'lib' },
    install_requires = [          # 安装依赖的其他包
    ],
    scripts=[
         'bin/us',
    ],
    url='www.google.com',
    license='MIT',
    author='shalk',
    author_email='shalk@aliyun.com',
    description='update system '
)
