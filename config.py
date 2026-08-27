from dotenv import find_dotenv,load_dotenv
import os

def getthekey():
    load_dotenv(find_dotenv(),override=True)
    return os.getenv('GOOGLE_API_KEY')






