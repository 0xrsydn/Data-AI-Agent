import getpass
import os
import pandas as pd
import tabulate
from sqlalchemy import create_engine

from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from langchain.output_parsers.openai_tools import JsonOutputKeyToolsParser
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_experimental.tools import PythonAstREPLTool
from langchain_experimental.agents import create_pandas_dataframe_agent

# Get the API key
api_key = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)

def sql_agent(file, agent_input):
    # Read the uploaded file into a DataFrame
    df = pd.read_csv(file)
    # Create SQLAlchemy engine
    engine = create_engine("sqlite:///uploaded_data.db")
    # Write the DataFrame to the SQLite database
    df.to_sql("uploaded_data", engine, index=False, if_exists='replace')
    db = SQLDatabase(engine=engine)
    # Create SQL agent
    agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)
    agent_output = agent_executor.invoke(agent_input)
    return agent_output

def pandas_agent(file, agent_input):
    # Check if the file extension is CSV
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    # Check if the file extension is XLSX or XLS
    elif file.name.endswith('.xlsx') or file.name.endswith('.xls'):
        df = pd.read_excel(file)
    else:
        return "Unsupported file format. Only CSV, XLS, or XLSX files are supported."
    # Proceed with your agent code
    agent = create_pandas_dataframe_agent(llm, df, agent_type="openai-tools", verbose=True)
    agent_output = agent.invoke(agent_input)
    return agent_output
