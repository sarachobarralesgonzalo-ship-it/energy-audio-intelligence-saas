import feedparser
import openai
import os

# El motor buscará tu clave de OpenAI automáticamente
openai.api_key = os.getenv("OPENAI_API_KEY")

def agente_noticias_energeticas():
    # Fuente de noticias líder en almacenamiento de energía
    url_noticias = "https://www.energy-storage.news/feed/" 
    feed = feedparser.parse(url_noticias)
    
    print(f"--- [RADIACIÓN POSITIVA] Analizando últimas noticias ---")
    
    # Analizamos las 3 noticias más recientes
    for entry in feed.entries[:3]:
        print(f"\n📰 NOTICIA: {entry.title}")
        
        # La IA actúa como tu analista senior
        resumen = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un analista experto en BESS y sector solar. Resume noticias para un CEO enfocándote en ROI y estrategia."},
                {"role": "user", "content": f"Analiza este contenido: {entry.summary}"}
            ]
        )
        print(f"💡 INSIGHT ESTRATÉGICO: {resumen.choices[0].message.content}")

            if __name__ == "__main__":
                 agente_noticias_energeticas()
