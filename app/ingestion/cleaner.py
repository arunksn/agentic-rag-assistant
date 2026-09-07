from __future__ import annotations

import re

from langchain_core.documents import Document


def clean_text(text: str) -> str:
    """Normalize extracted document text."""

    text = text.replace("\x00", " ")

    # Normalize line endings.
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Collapse excessive whitespace while preserving paragraphs.
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def clean_documents(
    documents: list[Document],
) -> list[Document]:
    """Clean document content and remove empty documents."""

    cleaned: list[Document] = []

    for document in documents:
        content = clean_text(document.page_content)

        if not content:
            continue

        cleaned.append(
            Document(
                page_content=content,
                metadata=document.metadata.copy(),
            )
        )

    return cleaned