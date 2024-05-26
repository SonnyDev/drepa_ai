import os
from groq import Groq
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "What is sickle cell disease",
        }
    ],
    model="mixtral-8x7b-32768",
)
result = chat_completion.choices[0].message.content

print(result)