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

JD ="""
We are hiring a Backend Python Developer

Requirements:
- Strong Python
-FastAPI or Django
- PostgreSQL
-Docker
-AWS
- Rest API
- 2+ years of experience

"""
RESUME="""
Name : Rahul Sharma

Exprience : 3 years as a software engineer

Skills : Python,docker,SQL,
Rest API,Git.

Projects :
food delivering system using FASTAPI and MYSQL

Delpoyed application using Docker.

"""
def ask_llm(system_prompt,user_prompt):
    sys_msg={
        "role": "system",
        "content": system_prompt
    }
    user_msg={
        "role": "user",
        "content": user_prompt
    }
    messages=[sys_msg,user_msg]
    response = client.chat(model=model, messages=messages)
    answer = response.choices[0].message.content
    return answer

def step1_res_extract():
    system_prompt="""
You are professional HR assistant. You have to extract the skills from the resume 
and return the skills from the candidates resume providec.
only return the skills no other information. Don not invent any skillsby yourself. If the skills are not present in the resume, return "No skills found"""

    user_prompt=f"""Extract the skills from the resume: {RESUME}"""
    
    return ask_llm(system_prompt,user_prompt)   

def step2_JD_extract():
    system_prompt="""
You are professional HR assistant. You have to extract the skills from the resume 
and return the skills from the candidates resume providec.
only return the skills no other information. Don not invent any skillsby yourself. If the skills are not present in the resume, return "No skills found"""

    user_prompt=f"""Extract the skills from this JD {JD}"""
    
    return ask_llm(system_prompt,user_prompt)   

def step3_match(candidate,jd):
    system_prompt="""
You are professional HR assistant. You have to match the skills from the resume and JD.Prepare a final score from 1 to 100  . Also produce a short verdict
wheather the candidate is suitable for the job or not. If the candidate is suitable, return "Suitable" otherwise return "Not Suitable".
"""
    user_prompt=f"""Compare and match the skills from the candidate's resume and the job description: {candidate} vs {JD}"""
    return ask_llm(system_prompt,user_prompt)

candidate_skills=step1_res_extract(RESUME)
print ("Candidate Skills:",candidate_skills)
sleep(2)
jd_skills=step2_JD_extract(JD)
print ("JD Skills:",jd_skills)
sleep(2)
score=step3_match(candidate_skills,jd_skills)
print ("Final Score and Verdict:",score)
