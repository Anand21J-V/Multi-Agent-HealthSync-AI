from crewai import Task
from agents import doctor_agent, pharmacist_agent, nutritionist_agent

def get_tasks(symptoms):
    return [
        Task(
            description=f"Analyze the following symptoms and provide a diagnosis: {symptoms}",
            agent=doctor_agent
        ),
        Task(
            description=f"Based on the diagnosis, recommend medications considering allergies.",
            agent=pharmacist_agent
        ),
        Task(
            description=f"Create a suitable diet plan for the patient's condition.",
            agent=nutritionist_agent
        )
    ]
