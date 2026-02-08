#=================================================
#Módulo crew.py: lanzar la crew de gentes y tareas
#=================================================


from crewai import Crew, LLM
from dotenv import load_dotenv
import os

load_dotenv()

api_key_groq = os.getenv("API_KEY_GROQ")

#Conectamos al modelo
llm = LLM(
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    #Dirección donde CrewAi enviará las peticiones al modelo LLM que ofrece Groq
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key_groq
)
