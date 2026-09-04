from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    app_name: str = Field(
        default="Agentic RAG Assistant",
        alias="APP_NAME",
    )
    app_env: str = Field(
        default="development",
        alias="APP_ENV",
    )
    debug: bool = Field(
        default=True,
        alias="DEBUG",
    )
    api_v1_prefix: str = Field(
        default="/api/v1",
        alias="API_V1_PREFIX",
    )

    # Server
    host: str = Field(
        default="0.0.0.0",
        alias="HOST",
    )
    port: int = Field(
        default=8000,
        alias="PORT",
    )

    # LLM
    openai_api_key: str = Field(
        default="",
        alias="OPENAI_API_KEY",
    )

    # MongoDB
    mongodb_uri: str = Field(
        default="mongodb://localhost:27017",
        alias="MONGODB_URI",
    )
    mongodb_database: str = Field(
        default="agentic_rag",
        alias="MONGODB_DATABASE",
    )

    # Vector database
    vector_db_provider: str = Field(
        default="mongodb",
        alias="VECTOR_DB_PROVIDER",
    )

    # LangSmith
    langsmith_tracing: bool = Field(
        default=False,
        alias="LANGSMITH_TRACING",
    )
    langsmith_api_key: str = Field(
        default="",
        alias="LANGSMITH_API_KEY",
    )
    langsmith_project: str = Field(
        default="agentic-rag-assistant",
        alias="LANGSMITH_PROJECT",
    )

    # Retrieval
    top_k: int = Field(
        default=5,
        alias="TOP_K",
        ge=1,
    )
    rerank_top_k: int = Field(
        default=3,
        alias="RERANK_TOP_K",
        ge=1,
    )

    # Agent
    max_agent_steps: int = Field(
        default=8,
        alias="MAX_AGENT_STEPS",
        ge=1,
    )


@lru_cache
def get_settings() -> Settings:
    """Return a cached application settings instance."""
    return Settings()


settings = get_settings()