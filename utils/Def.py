import os
from pathlib import Path
"""项目路径"""
PROJECT_DIR = Path(__file__).resolve().parent.parent
HOMEWORK_URL = 'upload\\homeworks'
HOMEWORK_ROOT = os.path.join(PROJECT_DIR, HOMEWORK_URL)
# HOMEWORK_ROOT = PROJECT_DIR + HOMEWORK_URL
"""数据库表"""
CLASS = "cl_class"
HOMEWORK = "cl_homework"
CLASS_USER = "cl_class_user"
