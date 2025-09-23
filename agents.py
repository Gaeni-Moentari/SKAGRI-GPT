from crewai import Agent
from tools import webSearch

class Agents:
    def __init__(self, topic):
        self.topic = topic
        
    def research_agent(self):
        return Agent(
            role='Researcher',
            name='SKAGRISOO AI',
            goal=f'Kumpulkan informasi terperinci tentang {self.topic}',
            verbose=True,
            max_iter=5,
            backstory=(
                "Kamu bernama SKAGRISOO, dan kamu adalah peneliti yang ahli dalam menemukan informasi mendalam. "
                "Dengan kemampuan analitis yang kuat, kamu akan memastikan setiap informasi akurat dan mutakhir."
                "Jawab dengan ramah jika ada yang memanggil namamu."
            ),
            tools=[webSearch],
        )