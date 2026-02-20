from typing import List

from pydantic import BaseModel, Field


class Source(BaseModel):
    """Schema for a source of information"""

    url: str = Field(description="The URL of the source")


class AgentSearchResponse(BaseModel):
    """Schema for a search response"""

    answer: str = Field(description="The answer to the question")
    sources: List[Source] = Field(
        default_factory=list,
        description="The sources used to answer the question",
    )
