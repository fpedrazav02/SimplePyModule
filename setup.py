from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='SimplePyModule',
    version='0.1.0',
    author='Francisco Pedraza',
    author_email='fpedrazav@uoc.edu',
    description='Módulo sencillo de Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
