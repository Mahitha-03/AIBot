import streamlit as st
import subprocess

st.set_page_config(page_title="AI Chatbot (Local Ollama)")
st.title("🤖 AI Chatbot ")

# -----------------------------
# Initialize chat history
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Function to call Ollama
# -----------------------------
def get_response(prompt):
    try:
        process = subprocess.Popen(
            ["ollama", "run", "phi3"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        stdout, stderr = process.communicate(prompt.encode("utf-8"))

        if stdout:
            return stdout.decode("utf-8", errors="ignore").strip()

        if stderr:
            return stderr.decode("utf-8", errors="ignore").strip()

        return "No response generated."

    except Exception as e:
        return f"Error: {e}"

# -----------------------------
# Display chat history
# -----------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**AI:** {msg['content']}")

# -----------------------------
# User input
# -----------------------------
user_input = st.text_input("Ask something:")

col1, col2 = st.columns(2)

with col1:
    ask_btn = st.button("Ask")

with col2:
    clear_btn = st.button("Clear Chat")

# -----------------------------
# Ask button logic
# -----------------------------
if ask_btn and user_input.strip():
    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Build conversation context
    conversation = ""
    for m in st.session_state.messages:
        if m["role"] == "user":
            conversation += f"User: {m['content']}\n"
        else:
            conversation += f"Assistant: {m['content']}\n"

    with st.spinner("Thinking..."):
        answer = get_response(conversation)

    # Add AI message
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()

# -----------------------------
# Clear chat
# -----------------------------
if clear_btn:
    st.session_state.messages = []
    st.experimental_rerun()
