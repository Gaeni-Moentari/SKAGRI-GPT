from crewai import Task
from urlbase import url
from agents import Agents
from tools import webSearch
class Tasks:
    def __init__(self, topic, language):
        self.topic = topic
        self.language = language
        
    def research_task(self):
        return Task(
            description=(
                f"Hey! Mari kita cari tahu tentang {self.topic} di SMK PGRI SOOKO MOJOKERTO! 🔍 "
                f"Kita akan fokus mengeksplorasi info terkini dan akurat dari {url}. "
                "Pastikan sumber informasinya valid ya! 📚"
            ),
            expected_output=(
                f"""
                ✨ Berikan laporan lengkap dalam bahasa {self.language} yang:
                
                📝 Maksimal 4 baris per paragraf
                🗣️ Menggunakan bahasa {self.language} yang gaul & kekinian yang sopan
                🎯 Fokus menjawab tentang {self.topic}
                ❌ Katakan Maaf jika tidak ada info valid
                
                Format jawaban:
                
                💡 [Judul yang Catchy]
                
                [Paragraf 1 - max 4 baris]
                [Paragraf 2 - max 4 baris] (opsional)
                [Paragraf 3 - max 4 baris] (opsional)
                [Paragraf 4 - max 4 baris] (opsional)
                [Paragraf 5 - max 4 baris] (opsional)
                
                🔍 Sumber: [link valid]
                """
            ),
            agent=Agents(self.topic).research_agent(),
            tools=[webSearch],
        )