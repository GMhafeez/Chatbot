from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os

from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title= "Langchain Server",
    version="1.0",
    description="An simple API server"
)
# add_routes(
#     app,
#     ChatOpenAI(),
#     path = "/openai"
# # )
# model = ChatOpenAI()
#ollama llama2
llm = Ollama(model="gemma")

prompt1 = ChatPromptTemplate.from_template(
    "write me an essay about {topic} with 100 words"
)
# prompt2 = ChatPromptTemplate.from_template(
#     "write me an poem about {topic} with 100 words"
# )
# add_routes (
#     app,
#     prompt1|model,
#     path="/essay"
# )
add_routes(
    app,
    prompt1|llm,
    path="/essay"

)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)