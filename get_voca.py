import requests
import json
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
    property = None

    url = 'https://www.godic.net/dicts/prefix/{}'.format(word) 

    raw_data = (get_data(url=url))
    
    try:
        first_meaning = (raw_data[0]['label'])
    except:
        return None
    
    if 'f.' in first_meaning:
        property = "f"
    elif 'n.' in first_meaning:
        property = 'n'
    elif 'm.' in first_meaning:
        property = 'm'
    # for _ in raw_data:
    #     print(_['label'])

    return property

if __name__ == "__main__":
    r = get_gender("Form")
    print(r)