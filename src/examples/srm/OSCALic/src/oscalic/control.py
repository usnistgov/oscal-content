from uuid import UUID
from typing import List
from pydantic import BaseModel,Field

from yaml import safe_load,YAMLError,dump

from .validation import Validation
from .by_component import ByComponentAssembly
from .set_parameter import SetParameterAssembly
from .statement import StatementAssembly
from .common import *

class ControlAssembly(BaseModel):
    uuid: str | UUID
    control_id: str = Field(alias='control-id')
    set_parameters: List[SetParameterAssembly] = Field(default=None, alias='set-parameters')
    statements: List[StatementAssembly] | None
    by_components: List[ByComponentAssembly] = Field(default=None, alias='by-components')


class ControlAssembly_Component(BaseModel):
    uuid: str | UUID
    control_id: str = Field(alias='control-id')
    set_parameters: List[SetParameterAssembly] = Field(default=None, alias='set-parameters')
    statements: List[StatementAssembly] | None
    provided: List[ProvidedAssembly] = Field(default=None, alias='provided')
    responsibilities: List[ResponsibilitiesAssembly] = Field(default=None, alias='responsibilities')
    inherited: List[InheritedAssembly] = Field(default=None, alias='inherited')
    satisfied: List[SatisfiedAssembly] = Field(default=None, alias='satisfied')    

class ControlImplementationAssembly(BaseModel):
    description: str
    implemented_requirements: List[ControlAssembly] = Field(default=None, alias='implemented-requirements')

class ControlImplementationAssembly_Component(BaseModel):
    description: str
    implemented_requirements: List[ControlAssembly_Component] = Field(default=None, alias='implemented-requirements')