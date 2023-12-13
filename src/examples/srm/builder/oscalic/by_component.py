from uuid import UUID
from pydantic import BaseModel,Field
from .common import *


class ImplementationStatusAssembly(BaseModel):
    state: str | None
    remarks: str | None

class ExportAssembly(BaseModel):
    provided: ProvidedAssembly = Field(default=None, alias='provided')
    responsibilities: ResponsibilitiesAssembly = Field(default=None, alias='responsibilities')

class ByComponentAssembly(BaseModel):
    uuid: str | UUID
    component_uuid: str | UUID = Field(alias='component-uuid')
    description: str | None
    provided: List[ProvidedAssembly] = Field(default=None, alias='provided')
    responsibilities: List[ResponsibilitiesAssembly] = Field(default=None, alias='responsibilities')
    inherited: List[InheritedAssembly] = Field(default=None, alias='inherited')
    satisfied: List[SatisfiedAssembly] = Field(default=None, alias='satisfied')    
    # export: ExportAssembly = Field(default=None, alias='export')




