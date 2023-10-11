#%%
from langchain.llms import OpenAIChat
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAIChat
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
import logging 
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.agents import ZeroShotAgent, AgentExecutor
import sys
import json
from langchain.agents.tools import Tool
sys.path.append("./tools/")
from langchain.chat_models import ChatOpenAI
import os
from langchain.tools import BaseTool
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
import rake 
from rake_nltk import Rake

data = pd.read_excel("/Users/sumeetvijaywargiya/Downloads/about_datascience.xlsx")
data.head()
os.environ["LOG_DIR"]="."
os.environ["WORDLIST_DIR"]="."
llm = OpenAIChat(model_name='gpt-3.5-turbo',openai_api_key="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",temperature=0)
# %%
about_array = data["about"].values
prompt_initial_template = """
        You are an expert in summarising and extracting keywords. You will be given a paragraph as input. Your task is to extract all the necessary and relevant keywords from the inputted 
        paragraph, which are similar or match the job role: {role}.
        Return all the extracted keywords in the form of list.
        The inputted paragraph is:
        {input}
    """

prompt = PromptTemplate(input_variables=['role', 'input'], template=prompt_initial_template)
chain = LLMChain(llm=llm, prompt = prompt, verbose=True)
summarized_array = []

#%%
value = about_array[0]
data_val = chain.run({'role' : 'Data scientist', 'input' : value})
summarized_array.append(data_val)
# %%
