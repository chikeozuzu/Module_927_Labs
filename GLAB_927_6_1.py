# Task 1: Retrieving the Groq API Key

# groq account and API key created and retrieved successfully. The API key is saved with the display name 'Chike_Groq_API'.

# Task 2: Setting up LangChain and LangChain-Groq

import os
from langchain_groq import ChatGroq

#Assigning the Groq API key to an environment variable
#os.environ["GROQ_API_KEY"] = "Add your Groq API key here"

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

# Step 2: Create the second prompt template to fetch order details based on extracted information
second_prompt_template = PromptTemplate(
    input_variables=["extracted_info"],
    template="Using the extracted information: {extracted_info}, retrieve the relevant order details."
)

# Step 3: Create the third prompt template to generate a detailed response for the customer.
third_prompt_template = PromptTemplate(
    input_variables=["order_details"],
    template="Based on the following order details: {order_details}, generate a detailed response to address the customer's query."
)

# Step 4: Define the chains
first_chain = LLMChain(
    llm=llm,
    prompt=first_prompt_template,
)
second_chain = LLMChain(
    llm=llm,
    prompt=second_prompt_template,
)
third_chain = LLMChain(
    llm=llm,
    prompt=third_prompt_template,
)

# Input to start the prompt chain (example customer query)
initial_input = "Can you help me with the status of my order #12345? placed last week?"

# Run the first chain to extract key information from the query
extracted_info = first_chain.run(initial_input)
print("Extracted Information:", extracted_info)

# Run the second chain to retrieve order details based on extracted information
order_details = second_chain.run(extracted_info)
print("Order Details:", order_details)

# Run the third chain to generate a detailed response based on the order details
customer_response = third_chain.run(order_details)
print("Customer Response:", customer_response)

# Task 4: Optimizing and Evaluating Workflows

# Prompt 1
template1 = PromptTemplate(
    input_variables=["customer_query"],
    template="Extract the key information from the following customer query: {customer_query}"
)

# Prompt 2
template2 = PromptTemplate(
    input_variables=["extracted_info"],
    template="Using the extracted information: {extracted_info}, retrieve the relevant order details."
)

# Prompt 3
template3 = PromptTemplate(
    input_variables=["order_details"],
    template="Based on the following order details: {order_details}, generate a detailed response to address the customer's query."
)
