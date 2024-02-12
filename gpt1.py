import requests

user_input = input('Введите сообщение: ')

while len(user_input) < 10:
    print('Ваше сообщение должно содержать не менее 10 символов.')
    user_input = input('Введите сообщение: ')

data = {
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": user_input}],
     "temperature": 0.7
   }

headers = {
"Content-Type": "application/json" ,
"Authorization": "Bearer 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",
}

response = requests.post('https://api.openai.com/v1/chat/completions',
headers=headers, json=data)

print(response.json())
