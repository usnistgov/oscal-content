from uuid import UUID
from typing import List
from pydantic import BaseModel,Field
from .by_component import ByComponentAssembly

class StatementAssembly(BaseModel):
    uuid: str | UUID
    statement_id: str = Field(alias='statement-id')
    by_components: List[ByComponentAssembly] = Field(default=None, alias='by-components')
