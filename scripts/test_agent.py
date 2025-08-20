import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from agent import compile_agent

agent = compile_agent()
response = agent.invoke({'question' : 'What is Yggdrasil?'})

answer = response['answer']
answer = answer.split('</think>')[1].strip()

print(answer)