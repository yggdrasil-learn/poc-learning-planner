from typing import Any

from langgraph.graph.state import CompiledStateGraph
import streamlit as st
from streamlit_extras.bottom_container import bottom

from agent import compile_agent
from view import show_messages, load_css

def main():
    """
    Entrypoint for streamlit application
    """

    st.set_page_config(initial_sidebar_state = 'collapsed')
    load_css('src/style.css')

    _, center, _ = st.columns(3)
    center.image('src/img/tree.svg', width = 200)
    st.title('Yggdrasil Learning', anchor = False)

    agent: CompiledStateGraph = compile_agent()
    messages: list[tuple[str, str]] = st.session_state.get('messages', [])

    chat_placeholder: st._DeltaGenerator = st.empty()

    with bottom():
        prompt: str | None = st.chat_input('Ask a question')

    if prompt:
        messages.append(('human', prompt))
        st.session_state['messages'] = messages
        show_messages(chat_placeholder)

        with st.spinner('Thinking'):
            response: dict[str, Any] = agent.invoke(
                {'question' : prompt},
                {'configurable' : {'thread_id' : 1}}
            )

        answer: str = response['answer'].split('</think>')[1].strip()
        messages.append(('ai', answer))
        st.session_state['messages'] = messages

    show_messages(chat_placeholder)

if __name__ == '__main__':
    main()
