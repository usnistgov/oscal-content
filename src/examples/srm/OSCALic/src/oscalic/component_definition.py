from uuid import UUID
from typing import List
from pydantic import BaseModel, Field
from yaml import safe_load,YAMLError,dump

from .validation import Validation

from .control import *
from .common import *

import datetime

class AuthorizationBoundaryAssembly(BaseModel):
    description: str

class AuthorizedPrivilegeAssembly(BaseModel):
    title: str
    functions_performed: List = Field(default=None, alias='functions-performed')

class UserAssembly(BaseModel):
    uuid: str | UUID
    role_ids: List = Field(default=None, alias="role-ids")
    authorized_privileges: List[AuthorizedPrivilegeAssembly] = Field(default=None, alias='authorized-privileges')

class CapabilityAssembly(BaseModel):
    uuid: str | UUID
    title: str | None
    description: str | None
    control_implementation: ControlImplementationAssembly_Component = Field(default=None, alias='control-implementation')

class Document(BaseModel):
    uuid: str | UUID
    controls: List[ControlAssembly] | None
    metadata: MetadataAssembly | None
    import_component_definitions: ComponentAssembly = Field(default=None, alias='import-component-definition')
    components: List[ComponentAssembly] | None
    capabilities: List[CapabilityAssembly] | None

class ComponentDefinition(BaseModel):
    component_definition: Document = Field(default=None, alias='component-definition')

