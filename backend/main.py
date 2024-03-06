from dotenv import load_dotenv
from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI(
    title="Ai translate Server",
    version="1.0",
    description="A ai translate api"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

model = ChatOpenAI()

prompt = ChatPromptTemplate.from_template("Translate the following sentence to Portuguese: {sentence}")
add_routes(app, prompt | model, path="/translate")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
