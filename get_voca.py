import requests
import json
from yaml_reader import *

headers = {'content-type': 'application/json'}
def post_data(url, data):
    json_data = json.dumps
    r = requests.post(url=url, data=data)
    return json.loads(r)

def get_data(url):
    print(url)
    r = requests.get(url=url, headers=headers)
    return json.loads(r.text)


def get_gender(word: str):
    verb_lexicon = get_yaml("deutsch_yaml/voca.yaml")
    
    try:
        return verb_lexicon[word]['gender'], verb_lexicon[word]['meaning']
    except:
        return None

if __name__ == "__main__":
    r = get_gender("fish")
    print(r)