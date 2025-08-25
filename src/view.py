import streamlit as st

def load_css(path: str):
    """
    Load CSS styling

    :param path: Path to CSS file
    :type path: str
    """

    with open(path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

def show_messages(placeholder: st._DeltaGenerator):
    """
    Show messages

    :param placeholder: Placeholder to put messages
    :type placeholder: st._DeltaGenerator
    """

    messages: list[tuple[str, str]] = st.session_state.get('messages', [])

    with placeholder.container():
        for profile, message in messages:
            with st.chat_message(profile):
                st.write(message)
