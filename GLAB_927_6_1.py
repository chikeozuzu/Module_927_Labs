# Task 1: Retrieving the Groq API Key

# groq account and API key created and retrieved successfully. The API key is saved with the display name 'Chike_Groq_API'.

# Task 2: Setting up LangChain and LangChain-Groq

import os
from langchain_groq import ChatGroq

#Assigning the Groq API key to an environment variable
os.environ["GROQ_API_KEY"] = "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"

#Initialize LangChain with Groq Llama LLM
llm = ChatGroq(
    model= "llama3-8b-8192"
    )

#Create a prompt template for FAQs
messages = [
    ("system", "You are a customer support representative. Your goal is to efficiently handle queries."),
    ("human", "What are your business hours?"),
]
result = llm.invoke(messages)
print(result.content)

# Task 3: Creating Advanced Prompt Chains

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq

llm = ChatGroq(
    model= "llama3-8b-8192"
)

# Step 1: Create the first prompt template to retrieve customer query details
first_prompt_template = PromptTemplate(
    input_variables=["customer_query"],
    template="Extract the key information from the following customer query: {customer_query}"
)

