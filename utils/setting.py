import json
import shutil
import os
from enum import Enum
with open("config.json", "r") as file:
    config = json.load(file)
#性能图片文件夹
PLOTS_DIR=config["PLOTS_DIR"]
PLOTS_FOLDER=f'{PLOTS_DIR}'#保存图片
#用户上传文件夹
MODEL_DIR=config["MODEL_DIR"] #模型存放文件夹
UPLOAD_DIR=config["UPLOAD_DIR"]#用户存储文件夹
UPLOAD_FOLDER=f'{UPLOAD_DIR}' #用户上传数据集
MODEL_FILE=f'{MODEL_DIR}' #模型存放
DEFAULT_DIR=config["DEFAULT_DIR"]#默认项目数据集
PREDICT_DIR=config["PREDICT_DIR"]#默认预测文件
def get_U_M_path(userId,missionId,filename):
    return os.path.join(filename,str(userId),str(missionId))
def copy_files(path1, path2):
    # 获取 path1 下的所有文件和文件夹
    files = os.listdir(path1)

    # 创建目标文件夹
    if not os.path.exists(path2):
        os.makedirs(path2)

    for file in files:
        # 构建源文件路径和目标文件路径
        src = os.path.join(path1, file)
        dst = os.path.join(path2, file)
        
        # 复制文件
        shutil.copy2(src, dst)

# 
class Planet(Enum):
    train = "train"
    test = "test"
    model = "model"
    metrics = "metrics"
    modelpath = "modelpath"
    predictfile="predict"