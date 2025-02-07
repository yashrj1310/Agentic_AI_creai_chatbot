import warnings
warnings.filterwarnings('ignore')

import os
from crewai import Agent, Crew, Task, LLM       #changed imports
from crewai_tools import PDFSearchTool

llm=LLM( model="ollama/gemma2", 
        base_url="http://localhost:11434")

pdf_search_tool = PDFSearchTool(
    pdf=r'C:\Users\lenovo\Desktop\Project\Agentic_ai\static\attention.pdf',
    config=dict(
        llm=dict(
            provider="ollama",
            config=dict(
                model="gemma2",
                base_url="http://localhost:11434",
            ),
        ),
        embedder=dict(
            provider="ollama",
            config=dict(
                model="nomic-embed-text",
                base_url="http://localhost:11434",
            ),
        ),
    )
)

# --- Agents ---
research_agent = Agent(
    role="Research Agent",
    goal="Search through the PDF to find relevant answers",
    allow_delegation=False,
    backstory=(
        """
        The research agent is adept at searching and 
        extracting data from documents, ensuring accurate and prompt responses.
        """
    ),
    tools=[pdf_search_tool],
    max_iter=2,
    llm=llm
)

# --- Tasks ---
answer_customer_question_task = Task(
    description=(
        """
        Answer the customer's questions based on the attention PDF.
        The research agent will search through the PDF to find relevant answers.
        Your final answer MUST be clear and accurate, based on the content of the 
        attention PDF.

        Here is the customer's question:
        {customer_question}
        """
    ),
    expected_output="""Provide clear and accurate answers to the customer's questions based on the content of the attention PDF.""",
    tools=[pdf_search_tool],
    agent=research_agent
)

# --- Crew ---
crew = Crew(
    agents=[research_agent],
    tasks=[answer_customer_question_task]
)

customer_question = "What is defination of Transformer?"

results = crew.kickoff({"customer_question": customer_question})