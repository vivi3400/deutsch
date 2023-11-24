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

def get_verb_vi():
    # 随机获取动词
    verb_conjugation = get_yaml("verb_vi.yaml")
    return random.choice(list(verb_conjugation)) 

def get_verb_conjugation(verb, proun):
    # 获取动词变位后形式
    verb_conjugation = get_yaml("verb_conjugation.yaml")
    return verb_conjugation[verb][proun]

def check_n_a():
    # 随机出题，校验一格四格熟悉度
    personal_pronoun = get_yaml("nda.yaml")
    N_proun = random.choice(list(personal_pronoun)) 
    A_proun = random.choice(list(personal_pronoun))
    verb_eng = "give"
    ques = "{} {} {} ".format(N_proun,verb_eng, A_proun)
    #一格用N，四格用A的数据
    verb_deu = get_verb_conjugation(verb_eng, N_proun)
    answer = "{} {} {}".format(personal_pronoun[N_proun]['N'], verb_deu, personal_pronoun[A_proun]['A'])
    print(ques)
    input_str = input("Enter your answer: \n").strip()

    if input_str == answer:
        print('Correct')
    else:
        print('Wrong! correct Answer is : {} !'.format(answer))

def check_n_d():
    # 随机出题，校验一格三格熟悉度
    personal_pronoun = get_yaml("nda.yaml")
    N_proun = random.choice(list(personal_pronoun)) 
    A_proun = random.choice(list(personal_pronoun))
    verb_eng = get_verb_vi() 
    ques = "{} {} {} ".format(N_proun,verb_eng, A_proun)
    #一格用N，四格用A的数据
    verb_deu = get_verb_conjugation(verb_eng, N_proun)
    answer = "{} {} {}".format(personal_pronoun[N_proun]['N'], verb_deu, personal_pronoun[A_proun]['D'])
    print(ques)
    # input_str = input("Enter your answer: \n").strip()
    input_str = input("").strip()

    if input_str == answer:
        print('Correct')
    else:
        print('Wrong! correct Answer is : {} !'.format(answer))
    print('--------------')    


if __name__ == "__main__":
    while True:
        check_n_d()
    