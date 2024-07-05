import MLs.Classification as MC
import MLs.Regression  as MR
import MLs.Clustering   as MCL

from enum import Enum
class MLClass(Enum):
    classification = "classification"
    regression = "regression"
    clustering = "clustering"
    Other=None
def get_ml_class(value):
    for member in MLClass.__members__.values():
        if member.value == value:
            return member
    return MLClass.Other
class PycaretManager:
    def __init__(self):
        self.ml_class=MLClass.Other
        self.ml=None
        self.predict=None
        pass
    def Init(self,mode:MLClass,*args,**kwargs):
        self.ml_class=mode
        if mode == MLClass.classification:
            print("分类")
            self.ml=MC.AutoMLPipeline(*args,**kwargs)
            self.predict=MC.get_predict
        elif mode == MLClass.regression:
            # 设置回归任务
            self.ml=MR.AutoMLPipeline(*args,**kwargs)
            self.predict=MR.get_predict
        elif mode ==MLClass.clustering:
            # 设置聚类任务
            self.ml=MCL.AutoMLPipeline(*args,**kwargs)
            self.predict=MCL.get_predict
        else:
            self.ml=MC.AutoMLPipeline(*args,**kwargs)
            self.predict=MC.get_predict

    def Get_ML(self):
        return self.ml
    def get_predict(self,*args):
        print("预测,",*args)
        return self.predict(*args)

