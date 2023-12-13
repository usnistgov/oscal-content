from uuid import UUID
from typing import List
from pydantic import BaseModel, Field
from yaml import safe_load,YAMLError,dump

from .validation import Validation

from .control import *
from .common import *

import datetime

class Document(BaseModel):
    uuid: str | UUID
    metadata: MetadataAssembly | None
    components: List[ComponentAssembly] | None

class SharedResponsibility(BaseModel):
    shared_responsibility: Document = Field(default=None, alias='shared-responsibility')

