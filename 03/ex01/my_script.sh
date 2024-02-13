#!/bin/bash
pip install --upgrade pip

echo "pip version:"
pip --version

pip install --upgrade --force-reinstall git+https://github.com/jaraco/path.git --target=./local_lib --log=./install.log
export PYTHONPATH=$PYTHONPATH:./local_lib
python3 my_program.py
