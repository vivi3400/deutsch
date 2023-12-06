import yaml
import os 

def get_yaml(fileName) -> dict:
# 获取当前脚本所在文件夹路径
    curPath = os.path.dirname(os.path.realpath(__file__))
    # 获取yaml文件路径
    yamlPath = os.path.join(curPath, fileName)
    # open方法打开直接读出来
    with open(yamlPath, 'r', encoding='utf-8') as f:
        config = f.read()
    d = yaml.load(config,Loader=yaml.FullLoader)  # 用load方法转字典
    return d