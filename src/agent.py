from typing_extensions import TypedDict

from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END

llm = ChatOllama(model = 'qwen3:0.6b')

class State(TypedDict):
    question: str
    answer: str

def answer_question(state: State):
    
    prompt = PromptTemplate(input_variables = ['question'],
                            template = """
                            You are a helpful AI assistant. Answer the user's question. Do NOT include any extra commentary.

                            ## Here is the user's question
                            {question}
                            """)
    messages = prompt.invoke({'question' : state['question']})

    response = llm.invoke(messages)
    print(response.usage_metadata)

    return {'answer' : response.content}

def compile_agent():

    graph = StateGraph(State)

    graph.add_node('answer_question', answer_question)

    graph.add_edge(START, 'answer_question')
    graph.add_edge('answer_question', END)

    return graph.compile()
