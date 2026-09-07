from __future__ import annotations

from pathlib import Path

from langchain_core.documents import Document

from app.ingestion.cleaner import clean_documents
from app.ingestion.metadata import enrich_documents
from app.ingestion.parser import parse_file


def load_document(path: str | Path) -> list[Document]:
    """Load, parse, clean, and enrich a single document."""

    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Document not found: {file_path}"
        )

    if not file_path.is_file():
        raise ValueError(
            f"Expected a file, received: {file_path}"
        )

    documents = parse_file(file_path)

    documents = clean_documents(documents)

    documents = enrich_documents(
        documents,
        file_path,
    )

    return documents


def load_directory(
    directory: str | Path,
) -> list[Document]:
    """Load all supported documents from a directory."""

    directory_path = Path(directory)

    if not directory_path.exists():
        raise FileNotFoundError(
            f"Directory not found: {directory_path}"
        )

    documents: list[Document] = []

    for path in sorted(directory_path.iterdir()):
        if not path.is_file():
            continue

        try:
            documents.extend(load_document(path))
        except ValueError:
            # Unsupported files are skipped.
            continue

    return documents