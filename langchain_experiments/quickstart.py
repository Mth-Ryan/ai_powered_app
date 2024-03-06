from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.documents import Document
from langchain.chains import create_retrieval_chain


load_dotenv()

llm = ChatOpenAI()

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class thecnical documentation writer."),
    ("user", "{input}")
])


def basic_invoke():
    response = llm.invoke("how can langsmith help me with testing?")
    print(response)


def chaining():
    chain = prompt | llm

    response = chain.invoke({"input": "How can langsmith help with testing?"})
    print(response)


def output_parsers():
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    response = chain.invoke({"input": "How can langsmith help with testing?"})
    print(response)


def web_document_load():
    embeddings = OpenAIEmbeddings()
    loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    vector = FAISS.from_documents(documents, embeddings)
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

        <context>
        {context}
        </context>

        Question: {input}""")
    document_chain = create_stuff_documents_chain(llm, prompt)

    # response = document_chain.invoke({
    #     "input": "How can langsmith help with testing?",
    #     "context": [Document(page_content="langsmith can let you visualize test results")]
    # })
    # print(response)

    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    response = retrieval_chain.invoke({ "input": "How can langsmith help with testing?" })
    print(response["answer"])


if __name__ == "__main__":
    # basic_invoke()
    # chaining()
    # output_parsers()
    # output_parsers()
    web_document_load()
    pass
