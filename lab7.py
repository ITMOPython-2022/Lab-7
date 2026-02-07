import requests


def analyze(text_to_analyze):
    url = 'http://api.text2data.com/v3/analyze'
    payload = {
        'DocumentText': f'{text_to_analyze}', 
        'IsTwitterContent': 'false',
        'PrivateKey': '94B27606-BF53-415D-B690-A45D611DF7C9', #add your private key here (you can find it in the admin panel once you sign-up)
        'Secret':'123', #this should be set-up in admin panel as well
        'RequestIdentifier': '' #optional, used for reporting context
    }
 
    r = requests.post(url, data=payload)
    data=r.json()
    print(data)


while True:
    site = input('1 - cats, 2 - logos, 0 - exit: ')
    match site:
        case '1':
            response = requests.get('https://meowfacts.herokuapp.com')
            response = response.json()
            analyze(response['data'])

        case '2':
            response = requests.get('https://www.logotypes.dev/random/data')
            response = response.json()
            analyze(response['example_description'])
        
        case '0':
            break

        case _:
            print("Try again!")