from yaml_reader import *
import random

def get_input_and_verify(answer: str) -> int:
    '''
    根据input来校验结果
    '''
    input_str = input("").strip()

    if input_str == answer:
        print('Correct')
        return 1
    else:
        print('Wrong! correct Answer is : {} !'.format(answer))
        return 0

def get_verb_vi() -> str:
    # 随机获取动词
    verb_conjugation = get_yaml("deutsch_yaml/verb_vi.yaml")
    return random.choice(list(verb_conjugation)) 

def get_verb_conjugation(verb, proun):
    # 获取动词变位后形式
    verb_conjugation = get_yaml("deutsch_yaml/verb_conjugation.yaml")
    return verb_conjugation[verb][proun]

def get_possessive_eng():
    # 获取动词变位后形式
    possessive_prounoun = get_yaml("deutsch_yaml/possessive_pronoun.yaml")
    return random.choice(list(possessive_prounoun))

def get_possessive_deut(eng):
    # 获取动词变位后形式
    possessive_prounoun = get_yaml("deutsch_yaml/possessive_pronoun.yaml")
    return possessive_prounoun[eng]['N.m']

def get_adjective_eng():
    # 获取动词变位后形式
    adjective = get_yaml("deutsch_yaml/adjective.yaml")
    return random.choice(list(adjective))    

def get_adjective_deut(eng, possessive):
    # 获取动词变位后形式
    possessive_prounoun = get_yaml("deutsch_yaml/adjective.yaml")
    return possessive_prounoun[eng][possessive]