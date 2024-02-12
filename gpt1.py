import requests

user_input = input('message: ')

while len(user_input) < 10:
    print('your message must contain at least 10 characters')
    user_input = input('message: ')

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

response_json = response.json()

print(response_json['choices'][0]['message']['content'])
