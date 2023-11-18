import json
import requests

def get_text():
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYjJlMTIxYjUtOWJlNy00YjAzLWEzMGYtNjE3YjMxODVlYjRkIiwidHlwZSI6ImFwaV90b2tlbiJ9.lGQpMRulvr5QIAYIIEL4shQhqGtVbN0Zg_0VvJacDvo"}

    url = "https://api.edenai.run/v2/text/generation"
    payload = {
        "providers": "openai",
        "text": "tell me something about space adventures",
        "temperature": 0.2,
        "max_tokens": 250
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    print(result)
    print(result['openai']['generated_text'])

city_name = 'Madrid'
key = '2f44ab8d94825710392977b37c24d3ac'
response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
result = json.loads(response.text)
print(result)
