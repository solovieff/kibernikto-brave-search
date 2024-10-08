from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Query(BaseModel):
    """A model representing information gathered around the requested query."""

    original: str = Field(description="The original query that was requested.")
    altered: Optional[str] = Field(
        description="The altered query by the spellchecker. This is the query that is used to search.", default=None
    )
    spellcheck_off: bool = Field(description="Whether the spell checker is enabled or disabled.", default=True)
    show_strict_warning: Optional[bool] = Field(
        description="The value is True if the lack of results is due to a 'strict' safesearch setting. Adult content "
                    "relevant to the query was found, but was blocked by safesearch.",
        default=False
    )
