from typing import List
from pydantic import BaseModel,Field

class SetParameterAssembly(BaseModel):
    param_id: str = Field(alias='param-id')
    values: List[str] = []
