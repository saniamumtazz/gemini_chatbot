from google import genai
from config import getthekey

def talk(question:str):
    key=getthekey()
    obj=genai.Client(api_key=key)
    response=obj.models.generate_content(
        model='gemini-3.5-flash',
        contents=question
    )
    return response

qs=input('Ask any question')
info=talk(qs)
print(info.text)

