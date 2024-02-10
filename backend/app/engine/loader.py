import os

from llama_index.readers import SimpleWebPageReader
from app.engine.constants import DATA_DIR
from llama_index import VectorStoreIndex, download_loader
from llama_index import SimpleDirectoryReader
from llama_index import download_loader

from typing import List
from llama_index import Document

def get_documents():
    return SimpleDirectoryReader(DATA_DIR).load_data()

def get_k8s_documents(url: str) -> List[Document]:
    """
    Get the K8s documentation from the webdocs
    """
    SimpleWebPageReader = download_loader("SimpleWebPageReader")
    loader = SimpleWebPageReader()
    documents = loader.load_data("https://kubernetes.io/docs/home")

    return documents
