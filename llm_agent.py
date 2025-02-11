# llm_agent.py
import openai
import os

class LLM_Agent:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")

    def execute_task(self, task):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an automation assistant."},
                      {"role": "user", "content": task}]
        )
        return response["choices"][0]["message"]["content"]