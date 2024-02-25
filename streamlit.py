from chain import chatbot_chain
import streamlit as st

chain = chatbot_chain()

st.title("SQL Question Answering bot")

bot_logo_path = "logo.png"

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{"role": "bot",
                                     "content": "Hello, How can I help you today?"}]

for message in st.session_state.messages:
    if message["role"] == 'bot':
        with st.chat_message(message["role"], avatar=bot_logo_path):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if query := st.chat_input("Ask your query"):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant", avatar=bot_logo_path):
        message_placeholder = st.empty()
        result = chain({"question": query})
        message_placeholder.markdown(result['answer'])

    st.session_state.messages.append({"role": "bot", "content": result['answer']})
