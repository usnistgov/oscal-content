from pydantic import BaseModel, Field
from typing import List
from uuid import UUID

from .common import *
from oscalic.control import ControlImplementationAssembly

class ComponentAssembly(BaseModel):
    uuid: str | UUID
    type: str
    title: str
    description: str
    props: List[PropsAssembly]
    control_implementations: List[ControlImplementationAssembly] = Field(default=None, alias='control-implementations')
    status: StatusAssembly