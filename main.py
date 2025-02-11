# main.py
import os
from llm_agent import LLM_Agent

def main():
    agent = LLM_Agent()
    task = "Automate data extraction and summarization."
    response = agent.execute_task(task)
    print("AI Response:", response)

if __name__ == "__main__":
    main()
