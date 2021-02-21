from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(this_directory, 'version.txt'), encoding='utf-8') as f:
    version = f.read()

setup(
    name = 'misty2py',
    version = version,
    description = 'Misty II python3 wrapper',
    license = "MIT",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author='ChrisScarred',
    author_email='scarred.chris@gmail.com',
    url="https://github.com/ChrisScarred/misty2py",
    packages=['misty2py'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests'],
    python_requires='>=3'
)
