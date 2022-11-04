import os
from pathlib import Path
"""项目路径"""
PROJECT_DIR = Path(__file__).resolve().parent.parent
HOMEWORK_URL = 'upload\\homeworks'
HEADER_URL = 'upload\\headers'
HEADER_ROOT = os.path.join(PROJECT_DIR, HEADER_URL)
HOMEWORK_ROOT = os.path.join(PROJECT_DIR, HOMEWORK_URL)
# HOMEWORK_ROOT = PROJECT_DIR + HOMEWORK_URL
"""数据库表"""
TB_CLASS = "cl_class"
TB_HOMEWORK = "cl_homework"
TB_CLASS_USER = "cl_class_user"
TB_HOMEWORK_USER = "cl_homework_user"