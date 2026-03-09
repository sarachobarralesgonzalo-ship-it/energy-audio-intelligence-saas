# Energy & Mobility Audio Intelligence SaaS - Core Logic
# Purpose: Automate the curation of high-value energy data for audio synthesis.

class EnergyIntelligenceBot:
    def __init__(self, niche="BESS & Mobility"):
        self.niche = niche
        self.target_audience = "C-Level Executives"

    def filter_strategic_topics(self, raw_data):
        """
        Filters news that generates ROI for a CFO (CAEs, BESS, etc.)
        """
        # Palabras clave estratégicas para tu nicho
        keywords = ["CAE", "BESS", "Grid", "Sodium-ion", "ROI", "Tax Deduction", "V2G", "Certificados de Ahorro"]
        curated_topics = [item for item in raw_data if any(key.lower() in item.lower() for key in keywords)]
        return curated_topics

    def generate_briefing_prompt(self, topic):
        """
        Prepares the context for the audio engine (NotebookLM/LLM).
        """
        return f"Act as a Senior Energy Consultant. Create a strategic dialogue about: {topic}"

# Simulation of the daily workflow
if __name__ == "__main__":
    bot = EnergyIntelligenceBot()
    
    # Simulación de entrada de datos (BOE, Noticias técnicas, LinkedIn)
    raw_news = [
        "New BESS regulations in Spain 2026", 
        "General automotive lifestyle trends", 
        "CAE monetization strategies for industrial fleets",
        "Public lighting maintenance updates"
    ]
    
    print(f"--- Processing for: {bot.target_audience} ---")
    selected = bot.filter_strategic_topics(raw_news)
    
    print(f"Selected Strategic Topics for Audio: {selected}")
    
    for topic in selected:
        print(f"\n[Generated Prompt for AI]: {bot.generate_briefing_prompt(topic)}")
