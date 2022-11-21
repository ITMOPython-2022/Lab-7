import requests
import json


def analyze(text_en):
    url = "http://api.text2data.com/v3/analyze"

    payload = {
        'DocumentText': f'{text_en}',
        'IsTwitterContent': 'false',
        'PrivateKey': '94B27606-BF53-415D-B690-A45D611DF7C9',  # add your private key here (you can find it in the admin panel once you sign-up)
        'Secret': '123',  # this should be set-up in admin panel as well
        'RequestIdentifier': ''  # optional, used for reporting context
    }

    resp_an = requests.post(url, data=payload)
    # print(resp_an.text)
    data = resp_an.json()

    if data['Status'] == 1:
        # print('Text: %s', data['SentenceText'])

        print('This document is: %s%s %+.2f' % (
        data['DocSentimentPolarity'], data['DocSentimentResultString'], data['DocSentimentValue']))
        print('Magnitude: %.2f' % (data['Magnitude']))
        print('Subjectivity: %s' % (data['Subjectivity']))

        for item in data['CoreSentences']:
            print('Main text: %s' % (
            item['Text']))

        print('Keywords')

        for item in data['Keywords']:
            print('%s (%s) %s%s %+.2f' % (
            item['Text'], item['KeywordType'], item['SentimentPolarity'], item['SentimentResult'],
            item['SentimentValue']))

    else:
        print(data['ErrorMessage'])


# response = requests.get('http://numbersapi.com/')
# print(response.text)


while True:
    fact = input('1 - facts from life, 2 - facts from math, 0 - exit: ')
    match fact:
        case '1':
            number = input('Enter the number: ')
            response = requests.get(f'http://numbersapi.com/{number}/trivia')
            text = response.text
            analyze(text)
        case '2':
            number = input('Enter the number: ')
            response = requests.get(f'http://numbersapi.com/{number}/math')
            text = response.text
            analyze(text)
        case '0':
            break
        case _:
            print("Wrong type!")
