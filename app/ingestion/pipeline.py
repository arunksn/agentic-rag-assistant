from __future__ import annotations

from langchain_core.documents import Document

from app.ingestion.chunker import DocumentChunker
from app.ingestion.loader import load_document


class IngestionPipeline:
    """End-to-end document ingestion pipeline."""

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ) -> None:
        self.chunker = DocumentChunker(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def process(
        self,
        path: str,
    ) -> list[Document]:
        """Process a document into retrieval-ready chunks."""

        documents = load_document(path)

        return self.chunker.split(documents)