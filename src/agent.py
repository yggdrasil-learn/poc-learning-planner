from typing import Any
from typing_extensions import TypedDict

from langchain_core.messages.ai import AIMessage
from langchain_core.prompt_values import PromptValue
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph

from config import CONFIG

AGENT_CONFIG: dict[str, Any] = CONFIG['agent']
llm: ChatOllama = ChatOllama(model = 'qwen3:0.6b')

class State(TypedDict):
    question: str
    answer: str
    input_tokens: int
    output_tokens: int

def answer_question(state: State) -> dict[str, Any]:
    """
    Answer the user's question

    :param state: Current state of graph
    :type state: State
    :return: Answer with token usage
    :rtype: dict[str, Any]
    """
    
    prompt: PromptTemplate = PromptTemplate(
        input_variables = ['question'],
        template = AGENT_CONFIG['answer_question']['prompt']
    )
    messages: PromptValue = prompt.invoke({'question' : state['question']})

    response: AIMessage = llm.invoke(messages)

    results: dict[str, Any] = {
        'answer' : response.content,
        'input_tokens' : response.usage_metadata['input_tokens'],
        'output_tokens' : response.usage_metadata['output_tokens']
    }

    return results

def compile_agent() -> CompiledStateGraph:
    """
    Compile agent

    :return: Compiled agent
    :rtype: CompiledStateGraph
    """

    memory: InMemorySaver = InMemorySaver()
    graph: StateGraph = StateGraph(State)

    graph.add_node('answer_question', answer_question)

    graph.add_edge(START, 'answer_question')
    graph.add_edge('answer_question', END)

    return graph.compile(checkpointer = memory)
