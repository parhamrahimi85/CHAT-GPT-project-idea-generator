import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbu",
    messages=[
        {'role': 'user', 'content': 'Hi ChatGPT. say hi back'}
    ]
)
answer = response.choices[0].message.content
print(answer)
