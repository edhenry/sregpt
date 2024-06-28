import logging

from hippocamp.config.env import DATA_DIR
from hippocamp.engine.settings import settings
from hippocamp.engine.utils import init_pg_vector_store_from_env
from hippocamp.engine.loader import get_documents

from llama_index.core import (
    VectorStoreIndex,
    StorageContext,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def generate_datasource(service_context):
    logger.info("Creating new index")
    # load the documents and create the index
    documents = get_documents()
    store = init_pg_vector_store_from_env()
    storage_context = StorageContext.from_defaults(vector_store=store)
    VectorStoreIndex.from_documents(
        documents,
        service_context=service_context,
        storage_context=storage_context,
        show_progress=True,  # this will show you a progress bar as the embeddings are created
    )
    logger.info(
        f"Successfully created embeddings in the PG vector store, schema={store.schema_name} table={store.table_name}"
    )


if __name__ == "__main__":
    generate_datasource(settings())
