from uuid import UUID
from typing import List
from pydantic import BaseModel, Field
from yaml import safe_load,YAMLError,dump

from .validation import Validation

from .control import *
from .common import *

import datetime

class CategorizationAssembly(BaseModel):
    system: str | None
    information_type_ids: List = Field(default=None, alias='information-type-ids')

class ImpactAssembly(BaseModel):
    base: str | None

class InformationTypeAssembly(BaseModel):
    uuid: str | UUID
    title: str | None
    description: str | None
    categorizations: List[CategorizationAssembly]
    confidentiality_impact: ImpactAssembly = Field(default=None, alias='confidentiality-impact')
    integrity_impact: ImpactAssembly = Field(default=None, alias='integrity-impact')
    availability_impact: ImpactAssembly = Field(default=None, alias='availability-impact')

class SystemInformationAssembly(BaseModel):
    information_types: List[InformationTypeAssembly] = Field(default=None, alias='information-types')

class SecurityImpactLevelAssembly(BaseModel):
    security_objective_confidentiality: str = Field(default=None, alias='security-objective-confidentiality')
    security_objective_integrity: str = Field(default=None, alias='security-objective-integrity')
    security_objective_availability: str = Field(default=None, alias='security-objective-availability')

class AuthorizationBoundaryAssembly(BaseModel):
    description: str

class SystemCharacteristicAssembly(BaseModel):
    system_ids: List[IdAssembly] = Field(default=None, alias='system-ids')
    system_name: str = Field(default=None, alias='system-name')
    description: str
    security_sensitivity_level: str = Field(default=None, alias='security-sensitivity-level')
    system_information: SystemInformationAssembly = Field(default=None, alias='system-information')
    security_impact_level: SecurityImpactLevelAssembly = Field(default=None, alias='security-impact-level')
    status: StatusAssembly
    authorization_boundary: AuthorizationBoundaryAssembly = Field(default=None, alias='authorization-boundary')

class AuthorizedPrivilegeAssembly(BaseModel):
    title: str
    functions_performed: List = Field(default=None, alias='functions-performed')

class UserAssembly(BaseModel):
    uuid: str | UUID
    role_ids: List = Field(default=None, alias="role-ids")
    authorized_privileges: List[AuthorizedPrivilegeAssembly] = Field(default=None, alias='authorized-privileges')

class SystemImplementationAssembly(BaseModel):
    users: List[UserAssembly]
    components: List[ComponentAssembly]

class Document(BaseModel):
    uuid: str | UUID
    controls: List[ControlAssembly] | None
    metadata: MetadataAssembly | None
    import_profile: ImportProfileAssembly = Field(default=None, alias='import-profile')
    system_characteristics: SystemCharacteristicAssembly = Field(default=None, alias='system-characteristics')
    system_implementation: SystemImplementationAssembly = Field(default=None, alias='system-implementation')
    control_implementation: ControlImplementationAssembly = Field(default=None, alias='control-implementation')

class SystemSecurityPlan(BaseModel):
    system_security_plan: Document = Field(default=None, alias='system-security-plan')
