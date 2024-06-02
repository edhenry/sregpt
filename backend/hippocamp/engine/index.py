import logging
from llama_index.core import VectorStoreIndex
from hippocamp.engine.utils import init_pg_vector_store_from_env
from hippocamp.engine.settings import settings


def get_chat_engine():
    service_context = settings()
    logger = logging.getLogger("uvicorn")
    logger.info("Connecting to index from PGVector...")
    store = init_pg_vector_store_from_env()
    index = VectorStoreIndex.from_vector_store(store, service_context)
    logger.info("Finished connecting to index from PGVector.")
    return index.as_chat_engine(similarity_top_k=5, chat_mode="condense_plus_context")
