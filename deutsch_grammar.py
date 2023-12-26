import random
from yaml_reader import *
from deutsch_tools import *
'''
一三四格校验
'''

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
    return get_input_and_verify(answer)

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


    return get_input_and_verify(answer)

def check_noun_of_A():
    '''
    随机出题，校验定冠词、不定冠词四格训练
    人三物四    
    '''
    personal_pronoun = get_yaml("deutsch_yaml/nda.yaml")
    noun = get_yaml("deutsch_yaml/nda_the.yaml")
    N_proun = random.choice(list(personal_pronoun)) 
    D_proun = random.choice(list(personal_pronoun))
    A_noun = random.choice(list(noun))
    verb_eng = "give"
    ques = "{} {} {} {}".format(N_proun,verb_eng, D_proun, A_noun)
    print(ques)
    #一格用N，四格用A的数据
    verb_deu = get_verb_conjugation(verb_eng, N_proun)
    answer = "{} {} {} {}".format(personal_pronoun[N_proun]['N'], verb_deu, personal_pronoun[D_proun]['D'], noun[A_noun]['A'])

    return get_input_and_verify(answer)

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

    return get_input_and_verify(answer)

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

    return get_input_and_verify(answer)    

if __name__ == "__main__":
    # nda_ques_list = [check_n_d, check_n_a, check_noun_of_A] #一三四格检验
    adj_ques_list = [check_adjective_D, check_adjective_A] #形容词检验
    ques_all_list = [check_n_d, check_n_a, check_noun_of_A,check_adjective_D, check_adjective_A]
    total = 0
    total_correct = 0
    while True:
        # 随机出题
        total += 1
        correct = random.choice(ques_all_list)()
        total_correct += correct

        # print("{} Correct Rate".format(round(total_correct/total,2)))
        # check_adjective_D()
    