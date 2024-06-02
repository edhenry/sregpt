import os

from llama_index.llms import OpenAI
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SentenceSplitter
from 


def configure_global_settings():
    """Configure the global settings of the LlamaIndex instance"""
    model = os.getenv("MODEL", "gpt-3.5-turbo")
    Settings.llm(OpenAI(model=model))
    Settings.embed_model(HuggingFaceEmbedding(model_name="all-mpnet-base-v2"))
    Settings.node_parser = SentenceSplitter(chunk_size=1024, chunk_overlap=20)
    Settings.context_window = 3900
    Settings.num_output = 512
