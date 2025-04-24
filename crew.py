from crewai import Crew
from tasks import get_tasks
from agents import doctor_agent, pharmacist_agent, nutritionist_agent

def run_crew(symptoms):
    tasks = get_tasks(symptoms)
    healthcare_crew = Crew(
        agents=[doctor_agent, pharmacist_agent, nutritionist_agent],
        tasks=tasks,
        verbose=True
    )
    result = healthcare_crew.kickoff()
    return result
