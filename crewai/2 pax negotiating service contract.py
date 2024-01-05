import os
from openai import OpenAI

from crewai import Agent, Task, Crew, Process

# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
OpenAI(api_key=os.getenv("OPENAI_API_KEY") or "YOUR API KEY HERE")

# Define your tools, custom or not.
# Install duckduckgo-search for this example:
#
# !pip install -U duckduckgo-search
from langchain.tools import DuckDuckGoSearchRun
# search_tool = DuckDuckGoSearchRun()

# # Define your agents with roles and goals
# researcher = Agent(
#   role='Senior Research Analyst',
#   goal='Uncover cutting-edge developments in AI and data science',
#   backstory="""You are a Senior Research Analyst at a leading tech think tank.
#   Your expertise lies in identifying emerging trends and technologies in AI and
#   data science. You have a knack for dissecting complex data and presenting
#   actionable insights.""",
#   verbose=True,
#   allow_delegation=False,
#   tools=[search_tool]
#   # llm=OpenAI(temperature=0.7, model_name="gpt-4"). It uses langchain.chat_models, default is GPT4
# )
writer = Agent(
  role='negotiator',
  goal='Craft compelling negotiation dialog',
  backstory="""You are a negotiator and writer, known for your insightful
  and engaging articles on negotiation. You have a deep understanding of
  the human psychology around negotiation and conflicts. You transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=True
)

# # Create tasks for your agents
# task1 = Task(
#   description="""Conduct a comprehensive analysis of difficult negotiations involving finance and education.
#   Compile your findings in a detailed report.""",
#   agent=researcher
# )

task2 = Task(
  description="""Write a long dialog for a play with at least 16 lines for each character. 
  The play is about negotiation. 
  Set up the scene and the characters. What is at stake? Who wants what?
  The characters are negotiating the price of a service agreement for software.
  Develop an engaging dialog between two people that are 
  negotiating the cost, and service level agreements of the software.
  The dialog will clearly indicate who is speaking and their emotions.
  The negotiators will both try to get the best deal on price, delivery, and service.
  the Dialog  should be lively yet accessible, catering to an ESL audience.
  Aim for a dialog captures the essence of negotiations. 
  Provide a brief analysis of the negotiation strategy and tactics.""",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[writer],
  tasks=[task2],
  verbose=2, # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
  process=Process.sequential # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)