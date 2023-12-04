import random
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

def get_input_and_verify(answer):
    '''
    根据input来校验结果
    '''
    input_str = input("").strip()

    if input_str == answer:
        print('Correct')
    else:
        print('Wrong! correct Answer is : {} !'.format(answer))
    print('--------------')    


def get_verb_vi():
    # 随机获取动词
    verb_conjugation = get_yaml("deutsch_yaml/verb_vi.yaml")
    return random.choice(list(verb_conjugation)) 

def get_verb_conjugation(verb, proun):
    # 获取动词变位后形式
    verb_conjugation = get_yaml("verb_conjugation.yaml")
    return verb_conjugation[verb][proun]

def check_n_a():
    # 随机出题，校验一格四格熟悉度
    personal_pronoun = get_yaml("deutsch_yaml/nda.yaml")
    N_proun = random.choice(list(personal_pronoun)) 
    A_proun = random.choice(list(personal_pronoun))
    verb_eng = "love"
    ques = "{} {} {} ".format(N_proun,verb_eng, A_proun)
    print(ques)
    #一格用N，四格用A的数据
    verb_deu = get_verb_conjugation(verb_eng, N_proun)
    answer = "{} {} {}".format(personal_pronoun[N_proun]['N'], verb_deu, personal_pronoun[A_proun]['A'])
    get_input_and_verify(answer)

def check_n_d():
    # 随机出题，校验一格三格熟悉度
    personal_pronoun = get_yaml("deutsch_yaml/nda.yaml")
    N_proun = random.choice(list(personal_pronoun)) 
    A_proun = random.choice(list(personal_pronoun))
    verb_eng = get_verb_vi() 
    ques = "{} {} {} ".format(N_proun,verb_eng, A_proun)
    print(ques)
    #一格用N，四格用A的数据
    verb_deu = get_verb_conjugation(verb_eng, N_proun)
    answer = "{} {} {}".format(personal_pronoun[N_proun]['N'], verb_deu, personal_pronoun[A_proun]['D'])


    get_input_and_verify(answer)

def check_noun_of_A():
    '''
    随机出题，校验定冠词、不定冠词四格训练
    人三物四    
    '''
    personal_pronoun = get_yaml("deutsch_yaml/nda.yaml")
    noun = get_yaml("nda_the.yaml")
    N_proun = random.choice(list(personal_pronoun)) 
    D_proun = random.choice(list(personal_pronoun))
    A_noun = random.choice(list(noun))
    verb_eng = "give"
    ques = "{} {} {} {}".format(N_proun,verb_eng, D_proun, A_noun)
    print(ques)
    #一格用N，四格用A的数据
    verb_deu = get_verb_conjugation(verb_eng, N_proun)
    answer = "{} {} {} {}".format(personal_pronoun[N_proun]['N'], verb_deu, personal_pronoun[D_proun]['D'], noun[A_noun]['A'])

    get_input_and_verify(answer)

def check_adjective_D():
    '''
    形容词检查
    he thank the beautiful girl 
    she liebe the beautiful man
    they liebe the beautiful cinema
    '''
    personal_pronoun = get_yaml("deutsch_yaml/nda.yaml")
    adj_list = get_yaml("deutsch_yaml/adjective.yaml")
    N_proun = random.choice(list(personal_pronoun)) 
    adj = random.choice(list(adj_list))
    verb_eng = get_verb_vi() #不及物动词，后面接3格
    ques = "{} {} {} ".format(N_proun,verb_eng, adj)
    print(ques)
    #一格用N，四格用A的数据
    verb_deu = get_verb_conjugation(verb_eng, N_proun)
    answer = "{} {} {}".format(personal_pronoun[N_proun]['N'], verb_deu, adj_list[adj]['D'])  

    get_input_and_verify(answer)

def check_adjective_A():
    '''
    形容词检查
    he thank the beautiful girl 
    she liebe the beautiful man
    they liebe the beautiful cinema
    '''
    personal_pronoun = get_yaml("deutsch_yaml/nda.yaml")
    adj_list = get_yaml("deutsch_yaml/adjective.yaml")
    N_proun = random.choice(list(personal_pronoun)) 
    adj = random.choice(list(adj_list))
    verb_eng = "love"
    ques = "{} {} {} ".format(N_proun,verb_eng, adj)
    print(ques)
    #一格用N，四格用A的数据
    verb_deu = get_verb_conjugation(verb_eng, N_proun)
    answer = "{} {} {}".format(personal_pronoun[N_proun]['N'], verb_deu, adj_list[adj]['A'])  

    get_input_and_verify(answer)    

if __name__ == "__main__":
    # nda_ques_list = [check_n_d, check_n_a, check_noun_of_A] #一三四格检验
    adj_ques_list = [check_adjective_D, check_adjective_A] #形容词检验
    while True:
        # 随机出题
        random.choice(adj_ques_list)()
        # check_adjective_D()
    