import os
from dotenv import load_dotenv
from groq import Groq 

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("api error")
client = Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt1="hi"
prompt2="explain time travel"
prompt3="write a 300 word essay on cats"
prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
    "role":role,
    "content":prompt,
}
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages)
    usage=response.usage
    print(f"Prompt: {prompt} -->your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens}  Finish Reason: {response.choices[0].finish_reason}")
# message_sys={
#     "role":"system",
#     "content":"you are manager who suggests name for my food company.name should be in one word",
# }

# message={
#     "role":role,
#     "content":prompt,
# }
# messages=[message_sys,message]
# response=client.chat.completions.create(model=model,messages=messages,temperature=2)
# # print(response)
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# answer=response.choices[0].message.content
# print (answer)