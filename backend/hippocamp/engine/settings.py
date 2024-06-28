from llama_index.core import Settings

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import SentenceSplitter
from hippocamp.config.env import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    CONTEXT_WINDOW,
    NUM_OUTPUT,
    EMBEDDING_MODEL,
    LLM,
)


def settings():
    Settings.llm(OpenAI(model=LLM))
    Settings.embed_model(HuggingFaceEmbedding(model_name=EMBEDDING_MODEL))
    Settings.node_parser = SentenceSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )
    Settings.context_window = CONTEXT_WINDOW
    Settings.num_output = NUM_OUTPUT
