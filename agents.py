from crewai import Agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    temperature=0.3,
    model_name="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

doctor_agent = Agent(
    role="Medical Diagnostician",
    goal="Diagnose patient symptoms accurately",
    backstory="An experienced AI doctor with deep knowledge in medicine.",
    verbose=True,
    allow_delegation=True,
    llm=llm
)

pharmacist_agent = Agent(
    role="Pharmacist",
    goal="Recommend appropriate medications",
    backstory="Expert in pharmacology and drug interactions.",
    verbose=True,
    allow_delegation=True,
    llm=llm
)

nutritionist_agent = Agent(
    role="Nutritionist",
    goal="Provide dietary recommendations",
    backstory="Skilled in patient nutrition planning.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)
