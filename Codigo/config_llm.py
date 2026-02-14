from crewai import LLM
from dotenv import load_dotenv
import os

load_dotenv()

api_key_groq = os.getenv("API_KEY_GROQ")

#Un raise por si no existe una api_key en .env
if not api_key_groq:
    raise RuntimeError("Falta API_KEY_GROQ en el entorno. Añádela al .env")



#Conectamos al modelo
llm = LLM(
    model="llama-3.3-70b-versatile",
    #model="llama-3.1-8b-instant",
    temperature=0.5,
    #Dirección donde CrewAi enviará las peticiones al modelo LLM que ofrece Groq
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key_groq
)
