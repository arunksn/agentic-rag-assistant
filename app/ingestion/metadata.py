from __future__ import annotations

import hashlib
from pathlib import Path

from langchain_core.documents import Document


def calculate_document_id(path: Path) -> str:
    """Create a deterministic identifier from the file contents."""

    digest = hashlib.sha256()

    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)

    return digest.hexdigest()


def build_base_metadata(path: Path) -> dict:
    """Build metadata shared by all chunks from a source document."""

    return {
        "document_id": calculate_document_id(path),
        "source": str(path.resolve()),
        "file_name": path.name,
        "file_type": path.suffix.lower().lstrip("."),
    }


def enrich_documents(
    documents: list[Document],
    path: Path,
) -> list[Document]:
    """Attach normalized source metadata to loaded documents."""

    base_metadata = build_base_metadata(path)

    enriched: list[Document] = []

    for index, document in enumerate(documents):
        metadata = {
            **base_metadata,
            **document.metadata,
            "source_document_index": index,
        }

        enriched.append(
            Document(
                page_content=document.page_content,
                metadata=metadata,
            )
        )

    return enriched