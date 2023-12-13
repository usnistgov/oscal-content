from pydantic import BaseModel, Field
from typing import List
from uuid import UUID

class RoleAssembly(BaseModel):
    id: str | None
    title: str | None

class PartyAssembly(BaseModel):
    uuid: str | None
    type: str | None

class MetadataAssembly(BaseModel):
    title: str
    last_modified: str = Field(default=None, alias='last-modified')
    version: str
    oscal_version: str = Field(default=None, alias='oscal-version')
    roles: List[RoleAssembly] | None
    parties: List[PartyAssembly] | None

class ImportProfileAssembly(BaseModel):
    href: str | None

class IdAssembly(BaseModel):
    id: str | None

class StatusAssembly(BaseModel):
    state: str

class PropsAssembly(BaseModel):
    name: str
    value: str

class ComponentAssembly(BaseModel):
    uuid: str | UUID
    type: str
    title: str
    description: str
    props: List[PropsAssembly]
    status: StatusAssembly


class ResponsibilitiesAssembly(BaseModel):
    uuid: str | UUID
    description: str | None
    provided_uuid: str | UUID = Field(default=None, alias='provided-uuid')
    satisfied_uuid: str | UUID = Field(default=None, alias='satisfied-uuid')
    
class ProvidedAssembly(BaseModel):
    uuid: str | UUID
    satisfied_uuid: str | UUID = Field(default=None, alias='satisfied-uuid')
    description: str | None

class InheritedAssembly(BaseModel):
    uuid: str | UUID
    description: str | None
    provided_uuid: str | UUID = Field(default=None, alias='provided-uuid')
    satisfied_uuid: str | UUID = Field(default=None, alias='satisfied-uuid')

class SatisfiedAssembly(BaseModel):
    uuid: str | UUID
    responsibility_uuid: str | UUID = Field(default=None, alias='responsibility-uuid')
    description: str | None
