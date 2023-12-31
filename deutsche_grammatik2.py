import random
from yaml_reader import *
from deutsch_tools import *
'''
1、物主代词练习(一格)
2、形容词尾练习
'''
noun_dict ={
    'm':['Strand', 'Kaffee', 'Käse']
}

noun_dict_m = {
    'enemy':'Feind',
    'coffee':"Kaffee",
    'beach':'Strand',
    'report':'Bericht',
}

def check_possessive_N():

    possessive_eng = get_possessive_eng()
    possessive_deut = get_possessive_deut(possessive_eng)

    noun_eng = random.choice(list(noun_dict_m))
    noun_deut = noun_dict_m[noun_eng]

    ques = "{} {}".format(possessive_eng, noun_eng)
    answer = "{} {}".format(possessive_deut, noun_deut)
    print(ques)
    return get_input_and_verify(answer)

# 形容词一格词尾
def check_adjective_suffix_N():
    eng = get_adjective_eng()
    ques = "{}".format(eng)
    print(ques)
    deut = get_adjective_deut(eng, "N")
    answerPart = ""
    answer = "{}".format(deut)
    return get_input_and_verify(answer)

# 形容词四格词尾
def check_adjective_suffix_A():
    eng = get_adjective_eng()
    ques = "he loves {}".format(eng)
    print(ques)
    deut = get_adjective_deut(eng, "A")
    answerPart = "Er liebt "
    answer = "{}".format(deut)
    return get_input_and_verify(answer=answer, answer_part=answerPart)

# 形容词三格词尾
def check_adjective_suffix_D():
    eng = get_adjective_eng()
    ques = "you help {}".format(eng)
    print(ques)
    deut = get_adjective_deut(eng, "D")
    answerPart = "du hilfst "
    answer = "{}".format(deut)
    return get_input_and_verify(answer=answer, answer_part=answerPart)

# 形容词二格词尾
def check_adjective_suffix_G():
    eng = get_adjective_eng()
    ques = "car of {}".format(eng)
    print(ques)
    deut = get_adjective_deut(eng, "G")
    answerPart = "Auto "
    answer = "{}".format(deut)
    return get_input_and_verify(answer=answer, answer_part=answerPart)

if __name__ == "__main__":

    ques_list = [check_adjective_suffix_G] #一三四格检验
    # adj_ques_list = [check_adjective_D, check_adjective_A] #形容词检验
    # ques_all_list = [check_n_d, check_n_a, check_noun_of_A,check_adjective_D, check_adjective_A]
    total = 0
    total_correct = 0
    try:
        while True:
            # 随机出题
            total += 1
            correct = random.choice(ques_list)()
            total_correct += correct
    except KeyboardInterrupt:
        total_correct+=1
        print("\n  {} Correct Rate".format(round(total_correct/total,2)))

     