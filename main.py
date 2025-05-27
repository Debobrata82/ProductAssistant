import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field


load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

## Langsmith Tracking And Tracing
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"]="true"

# load the Groq gemma model
model = ChatGroq(temperature=0.7, model="gemma2-9b-it")

class Product(BaseModel):
    product_name: str = Field(description="The name of the product")
    product_details: str = Field(description="The details of the product")
    product_price: int = Field(description="The tentative price of the product in USD")

parser = JsonOutputParser(pydantic_object=Product)

# Using ChatPromptTemplate with more specific instructions
prompt = ChatPromptTemplate(
    messages=[
        ("system", "You are a product expert and assistant. Always respond with product information in the requested JSON format. For any product query, provide the product name, detailed description, and a reasonable price estimate in USD."),
        ("user", "{input}"),
        ("assistant", "Here is the product information in the required format: {format_instructions}")
    ],
    input_variables=["input"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt | model | parser
try:
    # Using a more specific product query
    response = chain.invoke({"input": "Tell me about the LG C2 OLED 65-inch TV."})
    print(response)
except Exception as e:
    print(f"Error: {e}")


