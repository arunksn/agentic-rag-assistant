from pathlib import Path

from app.ingestion.loader import load_document
from app.ingestion.pipeline import IngestionPipeline


SAMPLE_DOCUMENT = Path("data/sample/sample.txt")


def test_load_document() -> None:
    documents = load_document(SAMPLE_DOCUMENT)

    assert len(documents) == 1

    document = documents[0]

    assert "Agentic RAG Assistant" in document.page_content
    assert document.metadata["file_type"] == "txt"
    assert document.metadata["file_name"] == "sample.txt"
    assert document.metadata["document_id"]


def test_ingestion_pipeline_creates_chunks() -> None:
    pipeline = IngestionPipeline(
        chunk_size=150,
        chunk_overlap=30,
    )

    chunks = pipeline.process(
        str(SAMPLE_DOCUMENT)
    )

    assert len(chunks) > 1

    for chunk in chunks:
        assert chunk.page_content
        assert chunk.metadata["document_id"]
        assert "chunk_index" in chunk.metadata
        assert "chunk_size" in chunk.metadata