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
search_tool = DuckDuckGoSearchRun()

# Define your agents with roles and goals
researcher = Agent(
  role='Senior Research Analyst',
  goal='Uncover luxury travel destinations in 2024',
  backstory="""You are a Senior Research Analyst at a leading travel think tank.
  Your expertise lies in identifying emerging trends and destinations in luxury travel and
  luxury resorts. You find the newest air plane routes. You find trends of where big money is spent in travel. 
  You have a knack for dissecting complex data and presenting actionable insights.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool]
  # llm=OpenAI(temperature=0.7, model_name="gpt-4"). It uses langchain.chat_models, default is GPT4
)
writer = Agent(
  role='Travel industry business Strategist',
  goal='Craft compelling content on travel advancements',
  backstory="""You are a renowned Travel industry business Strategist, known for your insightful
  and engaging articles on the luxury travel industry. You specialize in luxury travel. Luxury Villas.  With a deep understanding of
  the travel industry, you transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=True
)

# Create tasks for your agents
task1 = Task(
  description="""Conduct a comprehensive analysis of the latest advancements in travel in 2024.
  Identify key trends, new plane routes, new luxury trends, and potential industry impacts.
  Compile your findings in a detailed report.""",
  agent=researcher
)

task2 = Task(
  description="""Using the insights from the researcher's report, develop an engaging blog
  post that highlights the most significant travel changes.
  Your post should be informative yet accessible, catering to a travel-savvy audience.
  Aim for a narrative that captures the essence of these breakthroughs and their
  implications for the future.""",
  agent=writer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[researcher, writer],
  tasks=[task1, task2],
  verbose=2, # Crew verbose more will let you know what tasks are being worked on, you can set it to 1 or 2 to different logging levels
  process=Process.sequential # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)