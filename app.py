import os
import streamlit as st
from groq import Groq
import pandas as pd
import json

# Set up the GROQ client
os.environ["GROQ_API_KEY"] = "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"
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Function to send a query to GROQ's API for chat completion, including dataset as context and the user's prompt and receive an answer/error in return from model
def query_groq(prompt, context):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": context},  # Include the dataset as context
                {"role": "user", "content": prompt},  # User's query
            ],
            model="llama-3.3-70b-versatile",  # Specify the model
        )
        # Return the response content
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def summarize_context(context, limit = 5000):
    if len(context) > limit:
        return context[:limit] + "... (truncated)"
    return context

def summarize_dataframe(df, rows = 5):
    return df.head(rows).to_csv(index = False)

def process_dataset(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1].lower()

    if file_extension == 'txt':
        return uploaded_file.read().decode("utf-8")
    elif file_extension == 'json':
        return json.dumps(json.load(uploaded_file), indent=2)
    elif file_extension == 'csv':
        df = pd.read_csv(uploaded_file)
        return summarize_dataframe(df)
    elif file_extension == 'xlsx':
        df = pd.read_excel(uploaded_file)
        return summarize_dataframe(df)
    else:
        return None

#Initialize 
if "messages" not in st.session_state:
    st.session_state.messages = []
if "dataset_context" not in st.session_state:
    st.session_state.dataset_context = None
if "user_query" not in st.session_state:
    st.session_state.user_query = ""


MAX_HISTORY_SIZE = 5000

def trim_messages(messages, max_size = MAX_HISTORY_SIZE):
    total_size =  0
    trimmed_messages = []
    for message in reversed(messages):
        message_size = len(message["content"])
        if total_size + message_size <= max_size:
            trimmed_messages.append(message)
            total_size += message_size
        else:
            break
    return list(reversed(trimmed_messages))


def handle_submit():
    if st.session_state.user_query.strip():
        st.session_state.messages = trim_messages(st.session_state.messages)
        st.session_state.messages.append({"role":"user", "content":st.session_state.user_query})
        summarized_context = summarize_context(st.session_state.dataset_context)
        response = query_groq(st.session_state.user_query, summarized_context)
        st.session_state.messages.append({"role":"assistant", "content":response})
        st.session_state.user_query=""

# Streamlit App UI
st.title("AI Chatbot with GROQ")
st.write("Ask questions based on the dataset provided!")

# Upload Dataset
st.sidebar.title("Dataset Management")
uploaded_file = st.sidebar.file_uploader("Upload your txt dataset", type=["txt", "json", "csv","xlsx"])

if uploaded_file:
    # Read uploaded file and extract content
    dataset_content = process_dataset(uploaded_file)
    if dataset_content:
        st.sidebar.success("Dataset loaded successfully!")
    # Store context in session state
        st.session_state.dataset_context = dataset_content
    else:
        st.sidebar.error("Unsupported file format. Please upload a .txt, .json, .csv or .xlsx file to continue.")
else:
    st.sidebar.warning("Please upload a dataset to proceed.")

# Chat UI
if st.session_state.dataset_context:
    st.text_area("Dataset Preview", dataset_content, height=200, disabled=True)

# Display chat history
    st.subheader("Chat History")
    if st.session_state.messages:
        for message in st.session_state.messages:
            if message["role"] == "user":
                st.write(f"**You:** {message['content']}")
            elif message["role"] == "assistant":
                st.write(f"**Buddy:** {message['content']}")

    st.text_input(
        "Enter your question:",
        value = st.session_state.user_query,
        key = "user_query",
        on_change=handle_submit,
    )
else:
    st.info("Upload a dataset to start asking questions.")
