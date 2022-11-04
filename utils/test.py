import os
from pathlib import Path
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# a = os.path.abspath(__file__)
# print(BASE_DIR)
# print(a)
# print(os.path.dirname(a))
print(Path(__file__).resolve().parent)