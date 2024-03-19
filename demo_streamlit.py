import streamlit as st
from ai_agent import sql_agent
from ai_agent import pandas_agent

# Create a title and description
st.title("Pandas AI Agent App 🤖")
st.markdown("""
AI agent to answer questions about a CSV file using the pandas library.

This app is a demo of my [GitHub repository](https://github.com/0xrsydn/Data-AI-Agent)
""")

# Get user input
file = st.file_uploader("Upload CSV file")
agent_input = st.text_input("Enter question")

if st.button('Execute'):
    if file is not None and agent_input != "":
        # Create a loading spinner
        with st.spinner('Running the agent...'):
            # Call the pandas_agent function
            output = pandas_agent(file, agent_input)

        # Display the output
        st.write(output)
    else:
        st.write("Please upload a file and enter a question.")