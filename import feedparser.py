import feedparser
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configuramos Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def agente_noticias_energeticas():
    url_noticias = "https://www.energy-storage.news/feed/" 
    feed = feedparser.parse(url_noticias)
    
    print(f"--- [MOTOR GEMINI ACTIVADO] ---")
    
    for entry in feed.entries[:3]:
        print(f"\n📰 NOTICIA: {entry.title}")
        
        prompt = f"Eres un analista experto en energía. Resume esta noticia para un CEO enfocándote en BESS y rentabilidad: {entry.summary}"
        response = model.generate_content(prompt)
        
        print(f"💡 INSIGHT DE GEMINI: {response.text}")

if __name__ == "__main__":
    agente_noticias_energeticas()