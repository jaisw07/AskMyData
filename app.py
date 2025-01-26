import os
import streamlit as st
from groq import Groq

# Set up the GROQ client
os.environ["GROQ_API_KEY"] = "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"  # Replace with your API key
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Function to query GROQ chat completion
def query_groq(prompt, context):
    """
    Send a query to GROQ's API for chat completions.

    Args:
        prompt (str): User's query.
        context (str): Predefined dataset as context.

    Returns:
        str: The chatbot's response or an error message.
    """
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

# Streamlit App
st.title("AI Chatbot with GROQ")
st.write("Ask questions based on the dataset provided!")

# Upload Dataset
st.sidebar.title("Dataset Management")
uploaded_file = st.sidebar.file_uploader("Upload your txt dataset", type=["txt"])

if uploaded_file:
    # Read uploaded file and extract content
    dataset_content = uploaded_file.read().decode("utf-8")
    st.sidebar.success("Dataset loaded successfully!")
else:
    st.sidebar.warning("Please upload a dataset to proceed.")
    dataset_content = None

# Chat UI
if dataset_content:
    st.text_area("Dataset Preview", dataset_content, height=200, disabled=True)
    user_query = st.text_input("Enter your question:")

    if st.button("Submit"):
        if user_query.strip():
            response = query_groq(user_query, dataset_content)
            st.text_area("Answer:", response, height=300, disabled=True)
        else:
            st.warning("Please enter a valid question.")
else:
    st.info("Upload a dataset to start asking questions.")

