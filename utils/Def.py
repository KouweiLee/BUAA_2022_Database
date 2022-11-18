import os
from pathlib import Path
"""项目路径"""
PROJECT_DIR = Path(__file__).resolve().parent.parent
DOWNLOAD_DIR = os.path.join(PROJECT_DIR, "upload")
HOMEWORK_URL = 'homeworks'
HEADER_URL = 'headers'
MATERIAL_URL = 'materials'
HEADER_ROOT = os.path.join(DOWNLOAD_DIR, HEADER_URL)
HOMEWORK_ROOT = os.path.join(DOWNLOAD_DIR, HOMEWORK_URL)
MATERIAL_ROOT = os.path.join(DOWNLOAD_DIR, MATERIAL_URL)
# HOMEWORK_ROOT = PROJECT_DIR + HOMEWORK_URL
"""数据库表"""
VIEW_HOMEWORK_USER = "view_homework_user"
VIEW_MATERIAL_CLASS = "view_material_class"
TB_CLASS = "cl_class"
TB_HOMEWORK = "cl_homework"
TB_CLASS_USER = "cl_class_user"
TB_HOMEWORK_USER = "cl_homework_user"
TB_MATERIAL = "cl_material"
TB_PICS = "tb_pics"
TB_USERS = "tb_user"
AN_DEVELOPS = "an_develops"
AN_PICS = "an_pics"
AN_DEVELOP_MEMBER = "an_develop_member"