import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq 
from time import sleep

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("api error")
client = Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
prompt="How internet works  explain in simple terms?"
message = [{"role": "user", "content": prompt}]
messages=[message]
# response = client.chat(model=model, messages=messages)
# answer = response.choices[0].message.content
# print(answer)
stream_response = client.chat_stream(model=model, messages=messages,stream =True)
for chunk in stream_response:
    if chunk.choices[0].delta:
        print(chunk.choices[0].delta.content, end="", flush=True)
        