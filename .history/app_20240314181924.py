# importing necessary libraries
import os
from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.memory import ConversationBufferMemory
import streamlit as st
# import boto3
from data_extractor import *


# API keys
# os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_KEY']
# os.environ['SERPAPI_API_KEY'] = st.secrets['SERPAPI_KEY']


# File upload
uploaded_file = extract_text("file injest/ex1.txt")
st.text(uploaded_file)



# # three tempertature modes
# if temp == "creative":
#     llm = OpenAI(temperature=0.9)
# if temp == "balanced":
#     llm = OpenAI(temperature=0.6)
# if temp == "imitative":
#     llm = OpenAI(temperature=0.2)



# memory = ConversationBufferMemory()

# tools = load_tools(['serpapi', 'llm-math'], llm=llm)

# agent = initialize_agent(
#     tools,
#     llm,
#     agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     memory = memory,
#     verbose = False
# )
# col1, col2 = st.columns(2)

# prompt = col1.text_input('Enter your Prompt here: ')

# if prompt:
#     result = agent.run(prompt)
#     st.write(result)

# elif col2.button('Voice'):
#     st.write('recording.......')
#     record_audio(7, path_to_audio)
#     st.write('recording ended.......')
#     resultant = agent.run(transcribe_to_text(path_to_audio))
#     st.write(resultant)
# else:
#     st.write("Please enter a prompt or use voice model")