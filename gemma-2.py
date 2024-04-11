import ollama
from langchain_community.llms import Ollama
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_core.messages import AIMessage, HumanMessage


def main() -> None:

    question="Who is Bonzez?"
    print(f"Question: {question}")
    print("")

    ollama = Ollama(base_url="http://localhost:11434", model="gemma:7b")
    print(ollama.invoke(question))
    print("")
    print("")

    input("Press Enter to continue...")

    documents = []
    for source in ["./data/the_frozen_year.md", "./data/bonzez.md"]:
        print(f"Loading document: {source}")
        loader = TextLoader(source)
        data = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        split_documents = text_splitter.split_documents(data)

        documents.extend(split_documents)
    
    print(documents)
    print("")
    print("")

    input("Press Enter to continue...")

    oembed = OllamaEmbeddings(
        base_url="http://localhost:11434", model="nomic-embed-text"
    )
    vectorstore = Chroma.from_documents(documents=documents, embedding=oembed)

    qachain=RetrievalQA.from_chain_type(ollama, retriever=vectorstore.as_retriever())
    print(qachain.invoke({"query": question}))
    print("")
    print("")

if __name__ == "__main__":
    main()
