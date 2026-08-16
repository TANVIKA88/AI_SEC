import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq 

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("api error")
client = Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"

def ask_llm(question):
    system_message = {
        "role":"system",
        "content":"You are a helpful assistant."
        }
    message = {
        "role":"user",
        "content": question
        }
    messages=[system_message, message]
    response = client.chat.completions.create(model=model, messages=messages)
    answer =  response.choices[0].message.content
    return answer

question = "What is the capital of France?"
print(ask_llm(question))