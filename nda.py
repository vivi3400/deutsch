import random
import yaml
import os

def get_yaml(fileName):
# 获取当前脚本所在文件夹路径
    curPath = os.path.dirname(os.path.realpath(__file__))
    # 获取yaml文件路径
    yamlPath = os.path.join(curPath, fileName)
    # open方法打开直接读出来
    with open(yamlPath, 'r', encoding='utf-8') as f:
        config = f.read()
    d = yaml.load(config,Loader=yaml.FullLoader)  # 用load方法转字典
    return d

def conjugation(verb, N):

    if verb == "give":
        if N == "i":
            return "gebe"
        elif N == "you":
            return "gibst"
        elif N == "he" or N == "she" or N == "es" or N == "youguys":
            return "gibt"
        elif N == "we":
            return "geben"
        elif N == "You":
            return "geben"


def check_n_a():
    personal_pronoun = get_yaml("nda.yaml")
    # 随机出题
    N_proun = random.choice(list(personal_pronoun)) 
    A_proun = random.choice(list(personal_pronoun))
    verb_eng = "give"
    ques = "{} {} {} ".format(N_proun,verb_eng, A_proun)
    #一格用N，四格用A的数据
    verb_deu = conjugation(verb_eng, N_proun)
    answer = "{} {} {}".format(personal_pronoun[N_proun]['N'], verb_deu, personal_pronoun[A_proun]['A'])
    print(ques)
    input_str = input("Enter your answer: \n").strip()

    if input_str == answer:
        print('Correct')
    else:
        print('Wrong! correct Answer is : {} !'.format(answer))

if __name__ == "__main__":
    check_n_a()
    