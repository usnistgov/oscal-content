from dataclasses import field
from enum import Enum
from pydantic.dataclasses import dataclass
from typing import List, Optional, Type

__NAMESPACE__ = "http://csrc.nist.gov/ns/oscal/1.0"


class AlignType(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


@dataclass
class ImageType:
    class Meta:
        name = "imageType"

    alt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    src: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class InsertType:
    """An insert can be used to identify a placeholder for dynamically inserting
    text related to a specific object, which is referenced by the object's
    identifier using an <code xmlns="">id-ref</code>.

    This insert mechanism allows the selection of which text value from
    the object to dynamically include based on the application's display
    requirements.

    :ivar type_value: The type of object to include from (e.g.,
        parameter, control, component, role, etc.)
    :ivar id_ref: The identity of the object to insert a value for. The
        identity will be selected from the index of objects of the
        specified <code xmlns="">type</code>. The specific value to
        include is based on the application's display requirements,
        which will likely use a specific data element associated with
        the <code xmlns="">type</code> (e.g., title, identifier, value,
        etc.) that is appropriate for the application.
    """
    class Meta:
        name = "insertType"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "id-ref",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class OscalAssessmentCommonLoggedByAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Logged By</ns1:b>: Used to indicate who created a log entry in what role.

    :ivar party_uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Party UUID
        Reference</ns1:b>: A machine-oriented identifier reference to
        the party who is making the log entry.
    :ivar role_id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Actor
        Role</ns1:b>: A point to the role-id of the role in which the
        party is making the log entry.
    """
    class Meta:
        name = "oscal-assessment-common-logged-by-ASSEMBLY"

    party_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "party-uuid",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    role_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "role-id",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )


@dataclass
class OscalAssessmentCommonSelectControlByIdAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Select Control</ns1:b>: Used to select a control for inclusion/exclusion based on one or more control identifiers. A set of statement identifiers can be used to target the inclusion/exclusion to only specific control statements providing more granularity over the specific statements that are within the asessment scope.

    :ivar statement_id:
    :ivar control_id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Identifier
        Reference</ns1:b>: A reference to a control with a corresponding
        id value. When referencing an externally defined control, the
        Control Identifier Reference must be used in the context of the
        external / imported OSCAL instance (e.g., uri-reference).
    """
    class Meta:
        name = "oscal-assessment-common-select-control-by-id-ASSEMBLY"

    statement_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "statement-id",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    control_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "control-id",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )


@dataclass
class OscalAssessmentCommonSelectObjectiveByIdAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Select Objective</ns1:b>: Used to select a control objective for inclusion/exclusion based on the control objective's identifier.

    :ivar objective_id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Objective
        ID</ns1:b>: Points to an assessment objective.
    """
    class Meta:
        name = "oscal-assessment-common-select-objective-by-id-ASSEMBLY"

    objective_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "objective-id",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )


@dataclass
class OscalAssessmentCommonThreatIdField:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Threat ID</ns1:b>: A pointer, by ID, to an externally-defined threat.

    :ivar value:
    :ivar system: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Threat Type
        Identification System</ns1:b>: Specifies the source of the
        threat information.
    :ivar href: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Threat Information
        Resource Reference</ns1:b>: An optional location for the threat
        data, from which this ID originates.
    """
    class Meta:
        name = "oscal-assessment-common-threat-id-FIELD"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-zA-Z][a-zA-Z0-9+\-.]+:.*\S",
        }
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z][a-zA-Z0-9+\-.]+:.*\S",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\S(.*\S)?",
        }
    )


@dataclass
class OscalComponentDefinitionImportComponentDefinitionAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Import Component Definition</ns1:b>: Loads a component definition from another resource.

    :ivar href: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Hyperlink
        Reference</ns1:b>: A link to a resource that defines a set of
        components and/or capabilities to import into this collection.
    """
    class Meta:
        name = "oscal-component-definition-import-component-definition-ASSEMBLY"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"\S(.*\S)?",
        }
    )


@dataclass
class OscalControlCommonIncludeAllAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Include All</ns1:b>: Include all controls from the imported catalog or profile resources."""
    class Meta:
        name = "oscal-control-common-include-all-ASSEMBLY"


@dataclass
class OscalImplementationCommonPortRangeAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Port Range</ns1:b>: Where applicable this is the IPv4 port range on which the service operates.

    :ivar start: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Start</ns1:b>:
        Indicates the starting port number in a port range
    :ivar end: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">End</ns1:b>:
        Indicates the ending port number in a port range
    :ivar transport: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Transport</ns1:b>:
        Indicates the transport type.
    """
    class Meta:
        name = "oscal-implementation-common-port-range-ASSEMBLY"

    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\S(.*\S)?",
        }
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"\S(.*\S)?",
        }
    )
    transport: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )


@dataclass
class OscalImplementationCommonSystemIdField:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">System Identification</ns1:b>: A human-oriented, globally unique identifier with cross-instance scope that can be used to reference this system identification property elsewhere in this or other OSCAL instances. When referencing an externally defined system identification, the system identification must be used in the context of the external / imported OSCAL instance (e.g., uri-reference). This string should be assigned per-subject, which means it should be consistently used to identify the same system across revisions of the document.

    :ivar value:
    :ivar identifier_type: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Identification
        System Type</ns1:b>: Identifies the identification system from
        which the provided identifier was assigned.
    """
    class Meta:
        name = "oscal-implementation-common-system-id-FIELD"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    identifier_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "identifier-type",
            "type": "Attribute",
            "pattern": r"[a-zA-Z][a-zA-Z0-9+\-.]+:.*\S",
        }
    )


@dataclass
class OscalMetadataAddressAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Address</ns1:b>: A postal address for the location.

    :ivar addr_line:
    :ivar city:
    :ivar state:
    :ivar postal_code:
    :ivar country:
    :ivar type_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Address
        Type</ns1:b>: Indicates the type of address.
    """
    class Meta:
        name = "oscal-metadata-address-ASSEMBLY"

    addr_line: List[str] = field(
        default_factory=list,
        metadata={
            "name": "addr-line",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "postal-code",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )


@dataclass
class OscalMetadataDocumentIdField:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Document Identifier</ns1:b>: A document identifier qualified by an identifier scheme.

    :ivar value:
    :ivar scheme: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Document
        Identification Scheme</ns1:b>: Qualifies the kind of document
        identifier using a URI. If the scheme is not provided the value
        of the element will be interpreted as a string of characters.
    """
    class Meta:
        name = "oscal-metadata-document-id-FIELD"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    scheme: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-zA-Z][a-zA-Z0-9+\-.]+:.*\S",
        }
    )


@dataclass
class OscalMetadataHashField:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Hash</ns1:b>: A representation of a cryptographic digest generated over a resource using a specified hash algorithm.

    :ivar value:
    :ivar algorithm: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Hash
        algorithm</ns1:b>: The digest method by which a hash is derived.
    """
    class Meta:
        name = "oscal-metadata-hash-FIELD"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    algorithm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )


@dataclass
class OscalMetadataTelephoneNumberField:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Telephone Number</ns1:b>: A telephone service number as defined by ITU-T E.164.

    :ivar value:
    :ivar type_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">type flag</ns1:b>:
        Indicates the type of phone number.
    """
    class Meta:
        name = "oscal-metadata-telephone-number-FIELD"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )


@dataclass
class OscalProfileMatchingAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Match Controls by Pattern</ns1:b>: Selecting a set of controls by matching their IDs with a wildcard pattern.

    :ivar pattern: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Pattern</ns1:b>: A
        glob expression matching the IDs of one or more controls to be
        selected.
    """
    class Meta:
        name = "oscal-profile-matching-ASSEMBLY"

    pattern: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )


@dataclass
class OscalSspSecurityImpactLevelAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Security Impact Level</ns1:b>: The overall level of expected impact resulting from unauthorized disclosure, modification, or loss of access to information."""
    class Meta:
        name = "oscal-ssp-security-impact-level-ASSEMBLY"

    security_objective_confidentiality: Optional[str] = field(
        default=None,
        metadata={
            "name": "security-objective-confidentiality",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    security_objective_integrity: Optional[str] = field(
        default=None,
        metadata={
            "name": "security-objective-integrity",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    security_objective_availability: Optional[str] = field(
        default=None,
        metadata={
            "name": "security-objective-availability",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )


@dataclass
class AnchorType:
    class Meta:
        name = "anchorType"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "code",
                    "type": Type["CodeType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "em",
                    "type": Type["InlineMarkupType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "i",
                    "type": Type["InlineMarkupType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "b",
                    "type": Type["InlineMarkupType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "strong",
                    "type": Type["InlineMarkupType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "sub",
                    "type": Type["InlineMarkupType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "sup",
                    "type": Type["InlineMarkupType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "q",
                    "type": Type["InlineMarkupType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "img",
                    "type": ImageType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
            ),
        }
    )


@dataclass
class OscalProfileSelectControlByIdAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Select Control</ns1:b>: Select a control or controls from an imported control set.

    :ivar with_id:
    :ivar matching:
    :ivar with_child_controls: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Include Contained
        Controls with Control</ns1:b>: When a control is included,
        whether its child (dependent) controls are also included.
    """
    class Meta:
        name = "oscal-profile-select-control-by-id-ASSEMBLY"

    with_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "with-id",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    matching: List[OscalProfileMatchingAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    with_child_controls: Optional[str] = field(
        default=None,
        metadata={
            "name": "with-child-controls",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )


@dataclass
class InlineMarkupType:
    class Meta:
        name = "inlineMarkupType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": AnchorType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "insert",
                    "type": InsertType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "code",
                    "type": Type["CodeType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "em",
                    "type": Type["InlineMarkupType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "i",
                    "type": Type["InlineMarkupType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "b",
                    "type": Type["InlineMarkupType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "strong",
                    "type": Type["InlineMarkupType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "sub",
                    "type": Type["InlineMarkupType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "sup",
                    "type": Type["InlineMarkupType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "q",
                    "type": Type["InlineMarkupType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "img",
                    "type": ImageType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
            ),
        }
    )


@dataclass
class OscalProfileImportAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Import Resource</ns1:b>: Designates a referenced source catalog or profile that provides a source of control information for use in creating a new overlay or baseline.

    :ivar include_all:
    :ivar include_controls:
    :ivar exclude_controls:
    :ivar href: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Catalog or Profile
        Reference</ns1:b>: A resolvable URL reference to the base
        catalog or profile that this profile is tailoring.
    """
    class Meta:
        name = "oscal-profile-import-ASSEMBLY"

    include_all: Optional[OscalControlCommonIncludeAllAssembly] = field(
        default=None,
        metadata={
            "name": "include-all",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    include_controls: List[OscalProfileSelectControlByIdAssembly] = field(
        default_factory=list,
        metadata={
            "name": "include-controls",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    exclude_controls: List[OscalProfileSelectControlByIdAssembly] = field(
        default_factory=list,
        metadata={
            "name": "exclude-controls",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"\S(.*\S)?",
        }
    )


@dataclass
class OscalProfileInsertControlsAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Insert Controls</ns1:b>: Specifies which controls to use in the containing context.

    :ivar include_all:
    :ivar include_controls:
    :ivar exclude_controls:
    :ivar order: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Order</ns1:b>: A
        designation of how a selection of controls in a profile is to be
        ordered.
    """
    class Meta:
        name = "oscal-profile-insert-controls-ASSEMBLY"

    include_all: Optional[OscalControlCommonIncludeAllAssembly] = field(
        default=None,
        metadata={
            "name": "include-all",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    include_controls: List[OscalProfileSelectControlByIdAssembly] = field(
        default_factory=list,
        metadata={
            "name": "include-controls",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    exclude_controls: List[OscalProfileSelectControlByIdAssembly] = field(
        default_factory=list,
        metadata={
            "name": "exclude-controls",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    order: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )


@dataclass
class MarkupLineDatatype(InlineMarkupType):
    pass


@dataclass
class CodeType(InlineMarkupType):
    class Meta:
        name = "codeType"

    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
        }
    )


@dataclass
class PreformattedType(InlineMarkupType):
    class Meta:
        name = "preformattedType"


@dataclass
class TableCellType(InlineMarkupType):
    class Meta:
        name = "tableCellType"

    align: AlignType = field(
        default=AlignType.LEFT,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class OscalControlCommonParameterSelectionAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Selection</ns1:b>: Presenting a choice among alternatives.

    :ivar choice:
    :ivar how_many: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Parameter
        Cardinality</ns1:b>: Describes the number of selections that
        must occur. Without this setting, only one value should be
        assumed to be permitted.
    """
    class Meta:
        name = "oscal-control-common-parameter-selection-ASSEMBLY"

    choice: List[MarkupLineDatatype] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    how_many: Optional[str] = field(
        default=None,
        metadata={
            "name": "how-many",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )


@dataclass
class OscalImplementationCommonProtocolAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Service Protocol Information</ns1:b>: Information about the protocol used to provide a service.

    :ivar title:
    :ivar port_range:
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Service Protocol
        Information Universally Unique Identifier</ns1:b>: A machine-
        oriented, globally unique identifier with cross-instance scope
        that can be used to reference this service protocol information
        elsewhere in this or other OSCAL instances. The locally defined
        UUID of the service protocol can be used to reference the data
        item locally or globally (e.g., in an imported OSCAL instance).
        This UUID should be assigned per-subject, which means it should
        be consistently used to identify the same subject across
        revisions of the document.
    :ivar name: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Protocol
        Name</ns1:b>: The common name of the protocol, which should be
        the appropriate "service name" from the IANA Service Name and
        Transport Protocol Port Number Registry.
    """
    class Meta:
        name = "oscal-implementation-common-protocol-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    port_range: List[OscalImplementationCommonPortRangeAssembly] = field(
        default_factory=list,
        metadata={
            "name": "port-range",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )


@dataclass
class OscalMetadataLinkAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Link</ns1:b>: A reference to a local or remote resource, that has a specific relation to the containing object.

    :ivar text:
    :ivar href: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Hypertext
        Reference</ns1:b>: A resolvable URL reference to a resource.
    :ivar rel: <ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Link
        Relation Type</ns1:b>: Describes the type of relationship
        provided by the link's hypertext reference. This can be an
        indicator of the link's purpose.
    :ivar media_type: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Media
        Type</ns1:b>: A label that indicates the nature of a resource,
        as a data serialization or format.
    :ivar resource_fragment: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Resource
        Fragment</ns1:b>: In case where the href points to a back-
        matter/resource, this value will indicate the URI fragment to
        append to any rlink associated with the resource. This value
        MUST be URI encoded.
    """
    class Meta:
        name = "oscal-metadata-link-ASSEMBLY"

    text: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"\S(.*\S)?",
        }
    )
    rel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    media_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "media-type",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    resource_fragment: Optional[str] = field(
        default=None,
        metadata={
            "name": "resource-fragment",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )


@dataclass
class TableRowType:
    class Meta:
        name = "tableRowType"

    td: List[TableCellType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    th: List[TableCellType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )


@dataclass
class TableType:
    class Meta:
        name = "tableType"

    tr: List[TableRowType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )


@dataclass
class BlockQuoteType:
    class Meta:
        name = "blockQuoteType"

    h1: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h2: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h3: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h4: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h5: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h6: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    ul: List["ListType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    ol: List["OrderedListType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    pre: List[PreformattedType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    hr: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    blockquote: List["BlockQuoteType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    p: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    table: List[TableType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    img: List[ImageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )


@dataclass
class ListItemType:
    class Meta:
        name = "listItemType"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "a",
                    "type": AnchorType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "insert",
                    "type": InsertType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "code",
                    "type": CodeType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "em",
                    "type": InlineMarkupType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "i",
                    "type": InlineMarkupType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "b",
                    "type": InlineMarkupType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "strong",
                    "type": InlineMarkupType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "sub",
                    "type": InlineMarkupType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "sup",
                    "type": InlineMarkupType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "q",
                    "type": InlineMarkupType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "img",
                    "type": ImageType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "ul",
                    "type": Type["ListType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "ol",
                    "type": Type["OrderedListType"],
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "pre",
                    "type": PreformattedType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "blockquote",
                    "type": BlockQuoteType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "h1",
                    "type": InlineMarkupType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "h2",
                    "type": InlineMarkupType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "h3",
                    "type": InlineMarkupType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "h4",
                    "type": InlineMarkupType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "h5",
                    "type": InlineMarkupType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "h6",
                    "type": InlineMarkupType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
                {
                    "name": "p",
                    "type": InlineMarkupType,
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                },
            ),
        }
    )


@dataclass
class ListType:
    class Meta:
        name = "listType"

    li: List[ListItemType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )


@dataclass
class OrderedListType(ListType):
    class Meta:
        name = "orderedListType"

    start: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class MarkupMultilineDatatype:
    h1: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h2: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h3: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h4: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h5: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h6: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    ul: List[ListType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    ol: List[OrderedListType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    pre: List[PreformattedType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    hr: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    blockquote: List[BlockQuoteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    p: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    table: List[TableType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    img: List[ImageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )


@dataclass
class OscalArImportApAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Import Assessment Plan</ns1:b>: Used by assessment-results to import information about the original plan for assessing the system.

    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar href: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Plan
        Reference</ns1:b>: A resolvable URL reference to the assessment
        plan governing the assessment activities.
    """
    class Meta:
        name = "oscal-ar-import-ap-ASSEMBLY"

    remarks: Optional["OscalArImportApAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"\S(.*\S)?",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalAssessmentCommonImportSspAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Import System Security Plan</ns1:b>: Used by the assessment plan and POA&amp;M to import information about the system.

    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar href: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">System Security
        Plan Reference</ns1:b>: A resolvable URL reference to the system
        security plan for the system being assessed.
    """
    class Meta:
        name = "oscal-assessment-common-import-ssp-ASSEMBLY"

    remarks: Optional["OscalAssessmentCommonImportSspAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"\S(.*\S)?",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalControlCommonParameterGuidelineAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Guideline</ns1:b>: A prose statement that provides a recommendation for the use of a parameter."""
    class Meta:
        name = "oscal-control-common-parameter-guideline-ASSEMBLY"

    h1: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h2: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h3: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h4: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h5: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h6: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    ul: List[ListType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    ol: List[OrderedListType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    pre: List[PreformattedType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    hr: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    blockquote: List[BlockQuoteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    p: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    table: List[TableType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    img: List[ImageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )


@dataclass
class OscalImplementationCommonImplementationStatusAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Implementation Status</ns1:b>: Indicates the degree to which the a given control is implemented.

    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar state: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Implementation
        State</ns1:b>: Identifies the implementation status of the
        control or control objective.
    """
    class Meta:
        name = "oscal-implementation-common-implementation-status-ASSEMBLY"

    remarks: Optional["OscalImplementationCommonImplementationStatusAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalImplementationCommonSetParameterAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Set Parameter Value</ns1:b>: Identifies the parameter that will be set by the enclosed value.

    :ivar value:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar param_id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Parameter
        ID</ns1:b>: A human-oriented reference to a parameter within a
        control, who's catalog has been imported into the current
        implementation context.
    """
    class Meta:
        name = "oscal-implementation-common-set-parameter-ASSEMBLY"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    remarks: Optional["OscalImplementationCommonSetParameterAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    param_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "param-id",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalMappingCommonMappingProvenanceAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Mapping Provenance</ns1:b>: Describes requirements, incompatibilities and gaps that are identified between a target and source in a mapping item.

    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar method: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Method</ns1:b>:
        The method used to complete the overall mapping.
    :ivar matching: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Matching</ns1:b>:
        The method used for relating controls within the mapping.
    :ivar status: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Status</ns1:b>:
        The focus of the qualifier.
    """
    class Meta:
        name = "oscal-mapping-common-mapping-provenance-ASSEMBLY"

    remarks: Optional["OscalMappingCommonMappingProvenanceAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    method: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    matching: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalMappingCommonQualifierItemAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Relationship Qualifier</ns1:b>: Describes requirements, incompatibilities and gaps that are identified between a target and source in a mapping item.

    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar subject: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Subject</ns1:b>:
        The focus of the qualifier.
    :ivar predicate: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Predicate</ns1:b>:
        The predicate describes how the qualifer applies to the subject.
    :ivar category: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Category</ns1:b>:
        The category expresses the resolvable nature of the predicate.
    """
    class Meta:
        name = "oscal-mapping-common-qualifier-item-ASSEMBLY"

    remarks: Optional["OscalMappingCommonQualifierItemAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    subject: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    predicate: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    category: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalMetadataPropertyAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Property</ns1:b>: An attribute, characteristic, or quality of the containing object expressed as a namespace qualified name/value pair.

    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar name: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Property
        Name</ns1:b>: A textual label, within a namespace, that uniquely
        identifies a specific attribute, characteristic, or quality of
        the property's containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Property
        Universally Unique Identifier</ns1:b>: A unique identifier for a
        property.
    :ivar ns: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Property
        Namespace</ns1:b>: A namespace qualifying the property's name.
        This allows different organizations to associate distinct
        semantics with the same name.
    :ivar value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Property
        Value</ns1:b>: Indicates the value of the attribute,
        characteristic, or quality.
    :ivar class_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Property
        Class</ns1:b>: A textual label that provides a sub-type or
        characterization of the property's name.
    :ivar group: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Property
        Group</ns1:b>: An identifier for relating distinct sets of
        properties.
    """
    class Meta:
        name = "oscal-metadata-property-ASSEMBLY"

    remarks: Optional["OscalMetadataPropertyAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    ns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-zA-Z][a-zA-Z0-9+\-.]+:.*\S",
        }
    )
    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    group: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalSspImportProfileAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Import Profile</ns1:b>: Used to import the OSCAL profile representing the system's control baseline.

    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar href: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Profile
        Reference</ns1:b>: A resolvable URL reference to the profile or
        catalog to use as the system's control baseline.
    """
    class Meta:
        name = "oscal-ssp-import-profile-ASSEMBLY"

    remarks: Optional["OscalSspImportProfileAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"\S(.*\S)?",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalSspStatusAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Status</ns1:b>: Describes the operational status of the system.

    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar state: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">State</ns1:b>: The
        current operating status.
    """
    class Meta:
        name = "oscal-ssp-status-ASSEMBLY"

    remarks: Optional["OscalSspStatusAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalAssessmentCommonAssessmentPartAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Part</ns1:b>: A partition of an assessment plan or results or a child of another part.

    :ivar title:
    :ivar prop:
    :ivar h1:
    :ivar h2:
    :ivar h3:
    :ivar h4:
    :ivar h5:
    :ivar h6:
    :ivar ul:
    :ivar ol:
    :ivar pre:
    :ivar hr:
    :ivar blockquote:
    :ivar p:
    :ivar table:
    :ivar img:
    :ivar part:
    :ivar link:
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Part
        Identifier</ns1:b>: A machine-oriented, globally unique
        identifier with cross-instance scope that can be used to
        reference this part elsewhere in this or other OSCAL instances.
        The locally defined UUID of the part can be used to reference
        the data item locally or globally (e.g., in an ported OSCAL
        instance). This UUID should be assigned per-subject, which means
        it should be consistently used to identify the same subject
        across revisions of the document.
    :ivar name: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Part Name</ns1:b>:
        A textual label that uniquely identifies the part's semantic
        type.
    :ivar ns: <ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Part
        Namespace</ns1:b>: A namespace qualifying the part's name. This
        allows different organizations to associate distinct semantics
        with the same name.
    :ivar class_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Part
        Class</ns1:b>: A textual label that provides a sub-type or
        characterization of the part's name. This can be used to further
        distinguish or discriminate between the semantics of multiple
        parts of the same control with the same name and ns.
    """
    class Meta:
        name = "oscal-assessment-common-assessment-part-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h1: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h2: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h3: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h4: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h5: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h6: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    ul: List[ListType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    ol: List[OrderedListType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    pre: List[PreformattedType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    hr: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    blockquote: List[BlockQuoteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    p: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    table: List[TableType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    img: List[ImageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    part: List["OscalAssessmentCommonAssessmentPartAssembly"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    ns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-zA-Z][a-zA-Z0-9+\-.]+:.*\S",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )


@dataclass
class OscalAssessmentCommonAssessmentSubjectPlaceholderAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Subject Placeholder</ns1:b>: Used when the assessment subjects will be determined as part of one or more other assessment activities. These assessment subjects will be recorded in the assessment results in the assessment log.

    :ivar description:
    :ivar source:
    :ivar prop:
    :ivar link:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Subject
        Placeholder Universally Unique Identifier</ns1:b>: A machine-
        oriented, globally unique identifier for a set of assessment
        subjects that will be identified by a task or an activity that
        is part of a task. The locally defined UUID of the assessment
        subject placeholder can be used to reference the data item
        locally or globally (e.g., in an imported OSCAL instance). This
        UUID should be assigned per-subject, which means it should be
        consistently used to identify the same subject across revisions
        of the document.
    """
    class Meta:
        name = "oscal-assessment-common-assessment-subject-placeholder-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    source: List["OscalAssessmentCommonAssessmentSubjectPlaceholderAssembly.Source"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalAssessmentCommonAssessmentSubjectPlaceholderAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class Source:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Subject Source</ns1:b>: Assessment subjects will be identified while conducting the referenced activity-instance.

        :ivar task_uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Task
            Universally Unique Identifier</ns1:b>: A machine-oriented,
            globally unique identifier with cross-instance scope that
            can be used to reference (in this or other OSCAL instances)
            an assessment activity to be performed as part of the event.
            The locally defined UUID of the task can be used to
            reference the data item locally or globally (e.g., in an
            imported OSCAL instance). This UUID should be assigned per-
            subject, which means it should be consistently used to
            identify the same subject across revisions of the document.
        """
        task_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "task-uuid",
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalAssessmentCommonFindingTargetAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Objective Status</ns1:b>: Captures an assessor's conclusions regarding the degree to which an objective is satisfied.

    :ivar title:
    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar status:
    :ivar implementation_status:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar type_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Finding Target
        Type</ns1:b>: Identifies the type of the target.
    :ivar target_id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Finding Target
        Identifier Reference</ns1:b>: A machine-oriented identifier
        reference for a specific target qualified by the type.
    """
    class Meta:
        name = "oscal-assessment-common-finding-target-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    status: Optional["OscalAssessmentCommonFindingTargetAssembly.Status"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    implementation_status: Optional[OscalImplementationCommonImplementationStatusAssembly] = field(
        default=None,
        metadata={
            "name": "implementation-status",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalAssessmentCommonFindingTargetAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    target_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "target-id",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Status:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Objective Status</ns1:b>: A determination of if the objective is satisfied or not within a given system.

        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar state: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Objective
            Status State</ns1:b>: An indication as to whether the
            objective is satisfied or not.
        :ivar reason: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Objective
            Status Reason</ns1:b>: The reason the objective was given
            it's status.
        """
        remarks: Optional["OscalAssessmentCommonFindingTargetAssembly.Status.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        state: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
            }
        )
        reason: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "white_space": "preserve",
                "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalAssessmentCommonOriginActorAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Originating Actor</ns1:b>: The actor that produces an observation, a finding, or a risk. One or more actor type can be used to specify a person that is using a tool.

    :ivar prop:
    :ivar link:
    :ivar type_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Actor
        Type</ns1:b>: The kind of actor.
    :ivar actor_uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Actor Universally
        Unique Identifier Reference</ns1:b>: A machine-oriented
        identifier reference to the tool or person based on the
        associated type.
    :ivar role_id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Actor
        Role</ns1:b>: For a party, this can optionally be used to
        specify the role the actor was performing.
    """
    class Meta:
        name = "oscal-assessment-common-origin-actor-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    actor_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "actor-uuid",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    role_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "role-id",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )


@dataclass
class OscalAssessmentCommonReviewedControlsAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Reviewed Controls and Control Objectives</ns1:b>: Identifies the controls being assessed and their control objectives.

    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar control_selection:
    :ivar control_objective_selection:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    """
    class Meta:
        name = "oscal-assessment-common-reviewed-controls-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    control_selection: List["OscalAssessmentCommonReviewedControlsAssembly.ControlSelection"] = field(
        default_factory=list,
        metadata={
            "name": "control-selection",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    control_objective_selection: List["OscalAssessmentCommonReviewedControlsAssembly.ControlObjectiveSelection"] = field(
        default_factory=list,
        metadata={
            "name": "control-objective-selection",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalAssessmentCommonReviewedControlsAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )

    @dataclass
    class ControlSelection:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessed Controls</ns1:b>: Identifies the controls being assessed. In the assessment plan, these are the planned controls. In the assessment results, these are the actual controls, and reflects any changes from the plan.

        :ivar description:
        :ivar prop:
        :ivar link:
        :ivar include_all:
        :ivar include_control:
        :ivar exclude_control:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        """
        description: Optional[MarkupMultilineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        include_all: Optional[OscalControlCommonIncludeAllAssembly] = field(
            default=None,
            metadata={
                "name": "include-all",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        include_control: List[OscalAssessmentCommonSelectControlByIdAssembly] = field(
            default_factory=list,
            metadata={
                "name": "include-control",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        exclude_control: List[OscalAssessmentCommonSelectControlByIdAssembly] = field(
            default_factory=list,
            metadata={
                "name": "exclude-control",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalAssessmentCommonReviewedControlsAssembly.ControlSelection.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class ControlObjectiveSelection:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Referenced Control Objectives</ns1:b>: Identifies the control objectives of the assessment. In the assessment plan, these are the planned objectives. In the assessment results, these are the assessed objectives, and reflects any changes from the plan.

        :ivar description:
        :ivar prop:
        :ivar link:
        :ivar include_all:
        :ivar include_objective:
        :ivar exclude_objective:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        """
        description: Optional[MarkupMultilineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        include_all: Optional[OscalControlCommonIncludeAllAssembly] = field(
            default=None,
            metadata={
                "name": "include-all",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        include_objective: List[OscalAssessmentCommonSelectObjectiveByIdAssembly] = field(
            default_factory=list,
            metadata={
                "name": "include-objective",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        exclude_objective: List[OscalAssessmentCommonSelectObjectiveByIdAssembly] = field(
            default_factory=list,
            metadata={
                "name": "exclude-objective",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalAssessmentCommonReviewedControlsAssembly.ControlObjectiveSelection.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalAssessmentCommonSelectSubjectByIdAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Select Assessment Subject</ns1:b>: Identifies a set of assessment subjects to include/exclude by UUID.

    :ivar prop:
    :ivar link:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar subject_uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Subject
        Universally Unique Identifier Reference</ns1:b>: A machine-
        oriented identifier reference to a component, inventory-item,
        location, party, user, or resource using it's UUID.
    :ivar type_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Subject
        Universally Unique Identifier Reference Type</ns1:b>: Used to
        indicate the type of object pointed to by the uuid-ref within a
        subject.
    """
    class Meta:
        name = "oscal-assessment-common-select-subject-by-id-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalAssessmentCommonSelectSubjectByIdAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    subject_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "subject-uuid",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalAssessmentCommonSubjectReferenceAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Identifies the Subject</ns1:b>: A human-oriented identifier reference to a resource. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.

    :ivar title:
    :ivar prop:
    :ivar link:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar subject_uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Subject
        Universally Unique Identifier Reference</ns1:b>: A machine-
        oriented identifier reference to a component, inventory-item,
        location, party, user, or resource using it's UUID.
    :ivar type_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Subject
        Universally Unique Identifier Reference Type</ns1:b>: Used to
        indicate the type of object pointed to by the uuid-ref within a
        subject.
    """
    class Meta:
        name = "oscal-assessment-common-subject-reference-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalAssessmentCommonSubjectReferenceAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    subject_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "subject-uuid",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalComponentDefinitionIncorporatesComponentAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Incorporates Component</ns1:b>: The collection of components comprising this capability.

    :ivar description:
    :ivar component_uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Component
        Reference</ns1:b>: A machine-oriented identifier reference to a
        component.
    """
    class Meta:
        name = "oscal-component-definition-incorporates-component-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    component_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "component-uuid",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )


@dataclass
class OscalControlCommonParameterConstraintAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Constraint</ns1:b>: A formal or informal expression of a constraint or test."""
    class Meta:
        name = "oscal-control-common-parameter-constraint-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    test: List["OscalControlCommonParameterConstraintAssembly.Test"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )

    @dataclass
    class Test:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Constraint Test</ns1:b>: A test expression which is expected to be evaluated by a tool.

        :ivar expression:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        """
        expression: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "required": True,
                "white_space": "preserve",
                "pattern": r"\S(.*\S)?",
            }
        )
        remarks: Optional["OscalControlCommonParameterConstraintAssembly.Test.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )


@dataclass
class OscalControlCommonPartAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Part</ns1:b>: An annotated, markup-based textual element of a control's or catalog group's definition, or a child of another part.

    :ivar title:
    :ivar prop:
    :ivar h1:
    :ivar h2:
    :ivar h3:
    :ivar h4:
    :ivar h5:
    :ivar h6:
    :ivar ul:
    :ivar ol:
    :ivar pre:
    :ivar hr:
    :ivar blockquote:
    :ivar p:
    :ivar table:
    :ivar img:
    :ivar part:
    :ivar link:
    :ivar id: <ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Part
        Identifier</ns1:b>: A unique identifier for the part.
    :ivar name: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Part Name</ns1:b>:
        A textual label that uniquely identifies the part's semantic
        type, which exists in a value space qualified by the ns.
    :ivar ns: <ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Part
        Namespace</ns1:b>: An optional namespace qualifying the part's
        name. This allows different organizations to associate distinct
        semantics with the same name.
    :ivar class_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Part
        Class</ns1:b>: An optional textual providing a sub-type or
        characterization of the part's name, or a category to which the
        part belongs.
    """
    class Meta:
        name = "oscal-control-common-part-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h1: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h2: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h3: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h4: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h5: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    h6: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    ul: List[ListType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    ol: List[OrderedListType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    pre: List[PreformattedType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    hr: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    blockquote: List[BlockQuoteType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    p: List[InlineMarkupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    table: List[TableType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    img: List[ImageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    part: List["OscalControlCommonPartAssembly"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    ns: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-zA-Z][a-zA-Z0-9+\-.]+:.*\S",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )


@dataclass
class OscalImplementationCommonAuthorizedPrivilegeAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Privilege</ns1:b>: Identifies a specific system privilege held by the user, along with an associated description and/or rationale for the privilege."""
    class Meta:
        name = "oscal-implementation-common-authorized-privilege-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    function_performed: List[str] = field(
        default_factory=list,
        metadata={
            "name": "function-performed",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )


@dataclass
class OscalMappingCommonMappingItemAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Mapping Entry Item (source or target)</ns1:b>: Identifies a specific edge within a source or target that is the subject of a mapping.

    :ivar prop:
    :ivar link:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar type_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Subject
        Type</ns1:b>: The semantic type of the subject.
    :ivar id_ref: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Subject Identifier
        Reference</ns1:b>: A reference to an identified subject that is
        of the specified type.
    """
    class Meta:
        name = "oscal-mapping-common-mapping-item-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalMappingCommonMappingItemAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    id_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "id-ref",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalMappingCommonMappingResourceReferenceAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Mapped Resource Reference</ns1:b>: A reference to a resource that is either the source or target of a mapping.

    :ivar prop:
    :ivar link:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar type_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Resource
        Type</ns1:b>: The semantic type of the resource.
    :ivar href: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Catalog or Profile
        Reference</ns1:b>: A resolvable URL reference to the base
        catalog or profile that this profile is tailoring.
    """
    class Meta:
        name = "oscal-mapping-common-mapping-resource-reference-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalMappingCommonMappingResourceReferenceAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"\S(.*\S)?",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalMetadataBackMatterAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Back matter</ns1:b>: A collection of resources that may be referenced from within the OSCAL document instance."""
    class Meta:
        name = "oscal-metadata-back-matter-ASSEMBLY"

    resource: List["OscalMetadataBackMatterAssembly.Resource"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )

    @dataclass
    class Resource:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Resource</ns1:b>: A resource associated with content in the containing document instance. A resource may be directly included in the document using base64 encoding or may point to one or more equivalent internet resources.

        :ivar title:
        :ivar description:
        :ivar prop:
        :ivar document_id:
        :ivar citation:
        :ivar rlink:
        :ivar base64:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Resource
            Universally Unique Identifier</ns1:b>: A unique identifier
            for a resource.
        """
        title: Optional[MarkupLineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        description: Optional[MarkupMultilineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        document_id: List[OscalMetadataDocumentIdField] = field(
            default_factory=list,
            metadata={
                "name": "document-id",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        citation: Optional["OscalMetadataBackMatterAssembly.Resource.Citation"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        rlink: List["OscalMetadataBackMatterAssembly.Resource.Rlink"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        base64: Optional["OscalMetadataBackMatterAssembly.Resource.Base64"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalMetadataBackMatterAssembly.Resource.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

        @dataclass
        class Citation:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Citation</ns1:b>: An optional citation consisting of end note text using structured markup."""
            text: Optional[MarkupLineDatatype] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    "required": True,
                }
            )
            prop: List[OscalMetadataPropertyAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            link: List[OscalMetadataLinkAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

        @dataclass
        class Rlink:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Resource link</ns1:b>: A URL-based pointer to an external resource with an optional hash for verification and change detection.

            :ivar hash:
            :ivar href: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Hypertext
                Reference</ns1:b>: A resolvable URL pointing to the
                referenced resource.
            :ivar media_type: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Media
                Type</ns1:b>: A label that indicates the nature of a
                resource, as a data serialization or format.
            """
            hash: List[OscalMetadataHashField] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            href: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"\S(.*\S)?",
                }
            )
            media_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "media-type",
                    "type": "Attribute",
                    "white_space": "preserve",
                    "pattern": r"\S(.*\S)?",
                }
            )

        @dataclass
        class Base64:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Base64</ns1:b>: A resource encoded using the Base64 alphabet defined by RFC 2045.

            :ivar value:
            :ivar filename: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">File
                Name</ns1:b>: Name of the file before it was encoded as
                Base64 to be embedded in a resource. This is the name
                that will be assigned to the file when the file is
                decoded.
            :ivar media_type: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Media
                Type</ns1:b>: A label that indicates the nature of a
                resource, as a data serialization or format.
            """
            value: str = field(
                default="",
                metadata={
                    "required": True,
                    "pattern": r"[0-9A-Za-z+/]+={0,2}",
                }
            )
            filename: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "white_space": "preserve",
                    "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
                }
            )
            media_type: Optional[str] = field(
                default=None,
                metadata={
                    "name": "media-type",
                    "type": "Attribute",
                    "white_space": "preserve",
                    "pattern": r"\S(.*\S)?",
                }
            )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )


@dataclass
class OscalMetadataRemarksField(MarkupMultilineDatatype):
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>: Additional commentary about the containing object."""
    class Meta:
        name = "oscal-metadata-remarks-FIELD"


@dataclass
class OscalMetadataResponsiblePartyAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Responsible Party</ns1:b>: A reference to a set of persons and/or organizations that have responsibility for performing the referenced role in the context of the containing object.

    :ivar party_uuid:
    :ivar prop:
    :ivar link:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar role_id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Responsible
        Role</ns1:b>: A reference to a role performed by a party.
    """
    class Meta:
        name = "oscal-metadata-responsible-party-ASSEMBLY"

    party_uuid: List[str] = field(
        default_factory=list,
        metadata={
            "name": "party-uuid",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalMetadataResponsiblePartyAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    role_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "role-id",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalMetadataResponsibleRoleAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Responsible Role</ns1:b>: A reference to a role with responsibility for performing a function relative to the containing object, optionally associated with a set of persons and/or organizations that perform that role.

    :ivar prop:
    :ivar link:
    :ivar party_uuid:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar role_id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Responsible Role
        ID</ns1:b>: A human-oriented identifier reference to a role
        performed.
    """
    class Meta:
        name = "oscal-metadata-responsible-role-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    party_uuid: List[str] = field(
        default_factory=list,
        metadata={
            "name": "party-uuid",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    remarks: Optional["OscalMetadataResponsibleRoleAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    role_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "role-id",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalSspAdjustmentJustificationField(MarkupMultilineDatatype):
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Adjustment Justification</ns1:b>: If the selected security level is different from the base security level, this contains the justification for the change."""
    class Meta:
        name = "oscal-ssp-adjustment-justification-FIELD"


@dataclass
class OscalSspDiagramAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Diagram</ns1:b>: A graphic that provides a visual representation the system, or some aspect of it.

    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar caption:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Diagram
        ID</ns1:b>: A machine-oriented, globally unique identifier with
        cross-instance scope that can be used to reference this diagram
        elsewhere in this or other OSCAL instances. The locally defined
        UUID of the diagram can be used to reference the data item
        locally or globally (e.g., in an imported OSCAL instance). This
        UUID should be assigned per-subject, which means it should be
        consistently used to identify the same subject across revisions
        of the document.
    """
    class Meta:
        name = "oscal-ssp-diagram-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    caption: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalSspDiagramAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalSspImpactAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Impact Level</ns1:b>: The expected level of impact resulting from the described information.

    :ivar prop:
    :ivar link:
    :ivar base:
    :ivar selected:
    :ivar adjustment_justification: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Adjustment
        Justification</ns1:b>: If the selected security level is
        different from the base security level, this contains the
        justification for the change.
    """
    class Meta:
        name = "oscal-ssp-impact-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    base: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    selected: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    adjustment_justification: Optional["OscalSspImpactAssembly.AdjustmentJustification"] = field(
        default=None,
        metadata={
            "name": "adjustment-justification",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )

    @dataclass
    class AdjustmentJustification:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalAssessmentCommonActivityAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Activity</ns1:b>: Identifies an assessment or related process that can be performed. In the assessment plan, this is an intended activity which may be associated with an assessment task. In the assessment results, this an activity that was actually performed as part of an assessment.

    :ivar title:
    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar step:
    :ivar related_controls:
    :ivar responsible_role:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment
        Activity Universally Unique Identifier</ns1:b>: A machine-
        oriented, globally unique identifier with cross-instance scope
        that can be used to reference this assessment activity elsewhere
        in this or other OSCAL instances. The locally defined UUID of
        the activity can be used to reference the data item locally or
        globally (e.g., in an imported OSCAL instance). This UUID should
        be assigned per-subject, which means it should be consistently
        used to identify the same subject across revisions of the
        document.
    """
    class Meta:
        name = "oscal-assessment-common-activity-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    step: List["OscalAssessmentCommonActivityAssembly.Step"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    related_controls: Optional[OscalAssessmentCommonReviewedControlsAssembly] = field(
        default=None,
        metadata={
            "name": "related-controls",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
        default_factory=list,
        metadata={
            "name": "responsible-role",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalAssessmentCommonActivityAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class Step:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Step</ns1:b>: Identifies an individual step in a series of steps related to an activity, such as an assessment test or examination procedure.

        :ivar title:
        :ivar description:
        :ivar prop:
        :ivar link:
        :ivar reviewed_controls:
        :ivar responsible_role:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Step
            Universally Unique Identifier</ns1:b>: A machine-oriented,
            globally unique identifier with cross-instance scope that
            can be used to reference this step elsewhere in this or
            other OSCAL instances. The locally defined UUID of the step
            (in a series of steps) can be used to reference the data
            item locally or globally (e.g., in an imported OSCAL
            instance). This UUID should be assigned per-subject, which
            means it should be consistently used to identify the same
            subject across revisions of the document.
        """
        title: Optional[MarkupLineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        description: Optional[MarkupMultilineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "required": True,
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        reviewed_controls: Optional[OscalAssessmentCommonReviewedControlsAssembly] = field(
            default=None,
            metadata={
                "name": "reviewed-controls",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
            default_factory=list,
            metadata={
                "name": "responsible-role",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalAssessmentCommonActivityAssembly.Step.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalAssessmentCommonAssessmentMethodAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Method</ns1:b>: A local definition of a control objective. Uses catalog syntax for control objective and assessment activities.

    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar part:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Method
        Universally Unique Identifier</ns1:b>: A machine-oriented,
        globally unique identifier with cross-instance scope that can be
        used to reference this assessment method elsewhere in this or
        other OSCAL instances. The locally defined UUID of the
        assessment method can be used to reference the data item locally
        or globally (e.g., in an imported OSCAL instance). This UUID
        should be assigned per-subject, which means it should be
        consistently used to identify the same subject across revisions
        of the document.
    """
    class Meta:
        name = "oscal-assessment-common-assessment-method-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    part: Optional[OscalAssessmentCommonAssessmentPartAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    remarks: Optional["OscalAssessmentCommonAssessmentMethodAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalAssessmentCommonAssessmentSubjectAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Subject of Assessment</ns1:b>: Identifies system elements being assessed, such as components, inventory items, and locations. In the assessment plan, this identifies a planned assessment subject. In the assessment results this is an actual assessment subject, and reflects any changes from the plan. exactly what will be the focus of this assessment. Any subjects not identified in this way are out-of-scope.

    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar include_all:
    :ivar include_subject:
    :ivar exclude_subject:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar type_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Subject
        Type</ns1:b>: Indicates the type of assessment subject, such as
        a component, inventory, item, location, or party represented by
        this selection statement.
    """
    class Meta:
        name = "oscal-assessment-common-assessment-subject-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    include_all: Optional[OscalControlCommonIncludeAllAssembly] = field(
        default=None,
        metadata={
            "name": "include-all",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    include_subject: List[OscalAssessmentCommonSelectSubjectByIdAssembly] = field(
        default_factory=list,
        metadata={
            "name": "include-subject",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    exclude_subject: List[OscalAssessmentCommonSelectSubjectByIdAssembly] = field(
        default_factory=list,
        metadata={
            "name": "exclude-subject",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalAssessmentCommonAssessmentSubjectAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalAssessmentCommonLocalObjectiveAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment-Specific Control Objective</ns1:b>: A local definition of a control objective for this assessment. Uses catalog syntax for control objective and assessment actions.

    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar part:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar control_id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Identifier
        Reference</ns1:b>: A reference to a control with a corresponding
        id value. When referencing an externally defined control, the
        Control Identifier Reference must be used in the context of the
        external / imported OSCAL instance (e.g., uri-reference).
    """
    class Meta:
        name = "oscal-assessment-common-local-objective-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    part: List[OscalControlCommonPartAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    remarks: Optional["OscalAssessmentCommonLocalObjectiveAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    control_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "control-id",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalComponentDefinitionStatementAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Statement Implementation</ns1:b>: Identifies which statements within a control are addressed.

    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar responsible_role:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar statement_id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Statement
        Reference</ns1:b>: A human-oriented identifier reference to a
        control statement.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Statement
        Reference Universally Unique Identifier</ns1:b>: A machine-
        oriented, globally unique identifier with cross-instance scope
        that can be used to reference this control statement elsewhere
        in this or other OSCAL instances. The UUID of the control
        statement in the source OSCAL instance is sufficient to
        reference the data item locally or globally (e.g., in an
        imported OSCAL instance).
    """
    class Meta:
        name = "oscal-component-definition-statement-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
        default_factory=list,
        metadata={
            "name": "responsible-role",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalComponentDefinitionStatementAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    statement_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "statement-id",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalControlCommonParameterAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Parameter</ns1:b>: Parameters provide a mechanism for the dynamic assignment of value(s) in a control.

    :ivar prop:
    :ivar link:
    :ivar label:
    :ivar usage:
    :ivar constraint:
    :ivar guideline:
    :ivar value:
    :ivar select:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Parameter
        Identifier</ns1:b>: A unique identifier for the parameter.
    :ivar class_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Parameter
        Class</ns1:b>: A textual label that provides a characterization
        of the type, purpose, use or scope of the parameter.
    :ivar depends_on: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Depends
        on</ns1:b>: (deprecated) Another parameter invoking this one.
        This construct has been deprecated and should not be used.
    """
    class Meta:
        name = "oscal-control-common-parameter-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    label: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    usage: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    constraint: List[OscalControlCommonParameterConstraintAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    guideline: List[OscalControlCommonParameterGuidelineAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    value: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    select: Optional[OscalControlCommonParameterSelectionAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalControlCommonParameterAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    depends_on: Optional[str] = field(
        default=None,
        metadata={
            "name": "depends-on",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalImplementationCommonInventoryItemAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Inventory Item</ns1:b>: A single managed inventory item within the system.

    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar responsible_party:
    :ivar implemented_component:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Inventory Item
        Universally Unique Identifier</ns1:b>: A machine-oriented,
        globally unique identifier with cross-instance scope that can be
        used to reference this inventory item elsewhere in this or other
        OSCAL instances. The locally defined UUID of the inventory item
        can be used to reference the data item locally or globally
        (e.g., in an imported OSCAL instance). This UUID should be
        assigned per-subject, which means it should be consistently used
        to identify the same subject across revisions of the document.
    """
    class Meta:
        name = "oscal-implementation-common-inventory-item-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    responsible_party: List[OscalMetadataResponsiblePartyAssembly] = field(
        default_factory=list,
        metadata={
            "name": "responsible-party",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    implemented_component: List["OscalImplementationCommonInventoryItemAssembly.ImplementedComponent"] = field(
        default_factory=list,
        metadata={
            "name": "implemented-component",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalImplementationCommonInventoryItemAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class ImplementedComponent:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Implemented Component</ns1:b>: The set of components that are implemented in a given system inventory item.

        :ivar prop:
        :ivar link:
        :ivar responsible_party:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar component_uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Component
            Universally Unique Identifier Reference</ns1:b>: A machine-
            oriented identifier reference to a component that is
            implemented as part of an inventory item.
        """
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        responsible_party: List[OscalMetadataResponsiblePartyAssembly] = field(
            default_factory=list,
            metadata={
                "name": "responsible-party",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalImplementationCommonInventoryItemAssembly.ImplementedComponent.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        component_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "component-uuid",
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalImplementationCommonSystemComponentAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Component</ns1:b>: A defined component that can be part of an implemented system.

    :ivar title:
    :ivar description:
    :ivar purpose:
    :ivar prop:
    :ivar link:
    :ivar status:
    :ivar responsible_role:
    :ivar protocol:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Component
        Identifier</ns1:b>: A machine-oriented, globally unique
        identifier with cross-instance scope that can be used to
        reference this component elsewhere in this or other OSCAL
        instances. The locally defined UUID of the component can be used
        to reference the data item locally or globally (e.g., in an
        imported OSCAL instance). This UUID should be assigned per-
        subject, which means it should be consistently used to identify
        the same subject across revisions of the document.
    :ivar type_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Component
        Type</ns1:b>: A category describing the purpose of the
        component.
    """
    class Meta:
        name = "oscal-implementation-common-system-component-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    purpose: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    status: Optional["OscalImplementationCommonSystemComponentAssembly.Status"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
        default_factory=list,
        metadata={
            "name": "responsible-role",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    protocol: List[OscalImplementationCommonProtocolAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalImplementationCommonSystemComponentAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )

    @dataclass
    class Status:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Status</ns1:b>: Describes the operational status of the system component.

        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar state: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">State</ns1:b>:
            The operational status.
        """
        remarks: Optional["OscalImplementationCommonSystemComponentAssembly.Status.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        state: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalImplementationCommonSystemUserAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">System User</ns1:b>: A type of user that interacts with the system based on an associated role.

    :ivar title:
    :ivar short_name:
    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar role_id:
    :ivar authorized_privilege:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">User Universally
        Unique Identifier</ns1:b>: A machine-oriented, globally unique
        identifier with cross-instance scope that can be used to
        reference this user class elsewhere in this or other OSCAL
        instances. The locally defined UUID of the system user can be
        used to reference the data item locally or globally (e.g., in an
        imported OSCAL instance). This UUID should be assigned per-
        subject, which means it should be consistently used to identify
        the same subject across revisions of the document.
    """
    class Meta:
        name = "oscal-implementation-common-system-user-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    short_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "short-name",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    role_id: List[str] = field(
        default_factory=list,
        metadata={
            "name": "role-id",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    authorized_privilege: List[OscalImplementationCommonAuthorizedPrivilegeAssembly] = field(
        default_factory=list,
        metadata={
            "name": "authorized-privilege",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalImplementationCommonSystemUserAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalMappingCommonMapAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Mapping Entry</ns1:b>: A relationship-based mapping between a source and target set consisting of members (i.e., controls, control statements) from the respective source and target.

    :ivar prop:
    :ivar link:
    :ivar relationship:
    :ivar source:
    :ivar target:
    :ivar qualifier:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Mapping Entry
        Identifier</ns1:b>: The unique identifier for the mapping entry.
    """
    class Meta:
        name = "oscal-mapping-common-map-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    relationship: Optional["OscalMappingCommonMapAssembly.Relationship"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    source: List[OscalMappingCommonMappingItemAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    target: List[OscalMappingCommonMappingItemAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    qualifier: List[OscalMappingCommonQualifierItemAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalMappingCommonMapAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class Relationship:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Mapping Entry Relationship</ns1:b>: The relationship type for the mapping entry, which describes the relationship between the effective requirements of the specified source and target sets.

        :ivar value:
        :ivar ns: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Relationship
            Value Namespace</ns1:b>: A namespace qualifying the
            relationship's value. This allows different organizations to
            associate distinct semantics for relationships with the same
            name.
        """
        value: str = field(
            default="",
            metadata={
                "required": True,
                "white_space": "preserve",
                "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
            }
        )
        ns: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "pattern": r"[a-zA-Z][a-zA-Z0-9+\-.]+:.*\S",
            }
        )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalMetadataActionAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Action</ns1:b>: An action applied by a role within a given party to the content.

    :ivar prop:
    :ivar link:
    :ivar responsible_party:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Action Universally
        Unique Identifier</ns1:b>: A unique identifier that can be used
        to reference this defined action elsewhere in an OSCAL document.
        A UUID should be consistently used for a given location across
        revisions of the document.
    :ivar date: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Action Occurrence
        Date</ns1:b>: The date and time when the action occurred.
    :ivar type_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Action
        Type</ns1:b>: The type of action documented by the assembly,
        such as an approval.
    :ivar system: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Action Type
        System</ns1:b>: Specifies the action type system used.
    """
    class Meta:
        name = "oscal-metadata-action-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    responsible_party: List[OscalMetadataResponsiblePartyAssembly] = field(
        default_factory=list,
        metadata={
            "name": "responsible-party",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalMetadataActionAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    date: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-zA-Z][a-zA-Z0-9+\-.]+:.*\S",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalPoamPoamItemAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">POA&amp;M Item</ns1:b>: Describes an individual POA&amp;M item.

    :ivar title:
    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar origin:
    :ivar related_finding:
    :ivar related_observation:
    :ivar associated_risk:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">POA&amp;M Item
        Universally Unique Identifier</ns1:b>: A machine-oriented,
        globally unique identifier with instance scope that can be used
        to reference this POA&amp;M item entry in this OSCAL instance.
        This UUID should be assigned per-subject, which means it should
        be consistently used to identify the same subject across
        revisions of the document.
    """
    class Meta:
        name = "oscal-poam-poam-item-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    origin: List["OscalPoamPoamItemAssembly.Origin"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    related_finding: List["OscalPoamPoamItemAssembly.RelatedFinding"] = field(
        default_factory=list,
        metadata={
            "name": "related-finding",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    related_observation: List["OscalPoamPoamItemAssembly.RelatedObservation"] = field(
        default_factory=list,
        metadata={
            "name": "related-observation",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    associated_risk: List["OscalPoamPoamItemAssembly.AssociatedRisk"] = field(
        default_factory=list,
        metadata={
            "name": "associated-risk",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalPoamPoamItemAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class Origin:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Origin</ns1:b>: Identifies the source of the finding, such as a tool or person."""
        actor: List[OscalAssessmentCommonOriginActorAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "min_occurs": 1,
            }
        )

    @dataclass
    class RelatedFinding:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Related Finding</ns1:b>: Relates the poam-item to referenced finding(s).

        :ivar finding_uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Finding
            Universally Unique Identifier Reference</ns1:b>: A machine-
            oriented identifier reference to a finding defined in the
            list of findings.
        """
        finding_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "finding-uuid",
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

    @dataclass
    class RelatedObservation:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Related Observation</ns1:b>: Relates the poam-item to a set of referenced observations that were used to determine the finding.

        :ivar observation_uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Observation
            Universally Unique Identifier Reference</ns1:b>: A machine-
            oriented identifier reference to an observation defined in
            the list of observations.
        """
        observation_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "observation-uuid",
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

    @dataclass
    class AssociatedRisk:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Associated Risk</ns1:b>: Relates the finding to a set of referenced risks that were used to determine the finding.

        :ivar risk_uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Risk
            Universally Unique Identifier Reference</ns1:b>: A machine-
            oriented identifier reference to a risk defined in the list
            of risks.
        """
        risk_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "risk-uuid",
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalSspAuthorizationBoundaryAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Authorization Boundary</ns1:b>: A description of this system's authorization boundary, optionally supplemented by diagrams that illustrate the authorization boundary.

    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar diagram:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    """
    class Meta:
        name = "oscal-ssp-authorization-boundary-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    diagram: List[OscalSspDiagramAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalSspAuthorizationBoundaryAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalSspByComponentAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Component Control Implementation</ns1:b>: Defines how the referenced component implements a set of controls.

    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar set_parameter:
    :ivar implementation_status:
    :ivar export:
    :ivar inherited:
    :ivar satisfied:
    :ivar responsible_role:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar component_uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Component
        Universally Unique Identifier Reference</ns1:b>: A machine-
        oriented identifier reference to the component that is
        implemeting a given control.
    :ivar uuid: <ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">By-
        Component Universally Unique Identifier</ns1:b>: A machine-
        oriented, globally unique identifier with cross-instance scope
        that can be used to reference this by-component entry elsewhere
        in this or other OSCAL instances. The locally defined UUID of
        the by-component entry can be used to reference the data item
        locally or globally (e.g., in an imported OSCAL instance). This
        UUID should be assigned per-subject, which means it should be
        consistently used to identify the same subject across revisions
        of the document.
    """
    class Meta:
        name = "oscal-ssp-by-component-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    set_parameter: List[OscalImplementationCommonSetParameterAssembly] = field(
        default_factory=list,
        metadata={
            "name": "set-parameter",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    implementation_status: Optional[OscalImplementationCommonImplementationStatusAssembly] = field(
        default=None,
        metadata={
            "name": "implementation-status",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    export: Optional["OscalSspByComponentAssembly.Export"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    inherited: List["OscalSspByComponentAssembly.Inherited"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    satisfied: List["OscalSspByComponentAssembly.Satisfied"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
        default_factory=list,
        metadata={
            "name": "responsible-role",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalSspByComponentAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    component_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "component-uuid",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class Export:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Export</ns1:b>: Identifies content intended for external consumption, such as with leveraged organizations.

        :ivar description:
        :ivar prop:
        :ivar link:
        :ivar provided:
        :ivar responsibility:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        """
        description: Optional[MarkupMultilineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        provided: List["OscalSspByComponentAssembly.Export.Provided"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        responsibility: List["OscalSspByComponentAssembly.Export.Responsibility"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalSspByComponentAssembly.Export.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )

        @dataclass
        class Provided:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Provided Control Implementation</ns1:b>: Describes a capability which may be inherited by a leveraging system.

            :ivar description:
            :ivar prop:
            :ivar link:
            :ivar responsible_role:
            :ivar remarks: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
                Additional commentary about the containing object.
            :ivar uuid: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Provided
                Universally Unique Identifier</ns1:b>: A machine-
                oriented, globally unique identifier with cross-instance
                scope that can be used to reference this provided entry
                elsewhere in this or other OSCAL instances. The locally
                defined UUID of the provided entry can be used to
                reference the data item locally or globally (e.g., in an
                imported OSCAL instance). This UUID should be assigned
                per-subject, which means it should be consistently used
                to identify the same subject across revisions of the
                document.
            """
            description: Optional[MarkupMultilineDatatype] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    "required": True,
                }
            )
            prop: List[OscalMetadataPropertyAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            link: List[OscalMetadataLinkAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
                default_factory=list,
                metadata={
                    "name": "responsible-role",
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            remarks: Optional["OscalSspByComponentAssembly.Export.Provided.Remarks"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            uuid: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
                }
            )

            @dataclass
            class Remarks:
                h1: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h2: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h3: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h4: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h5: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h6: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                ul: List[ListType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                ol: List[OrderedListType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                pre: List[PreformattedType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                hr: List[object] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                blockquote: List[BlockQuoteType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                p: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                table: List[TableType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                img: List[ImageType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )

        @dataclass
        class Responsibility:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Implementation Responsibility</ns1:b>: Describes a control implementation responsibility imposed on a leveraging system.

            :ivar description:
            :ivar prop:
            :ivar link:
            :ivar responsible_role:
            :ivar remarks: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
                Additional commentary about the containing object.
            :ivar uuid: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Responsibility
                Universally Unique Identifier</ns1:b>: A machine-
                oriented, globally unique identifier with cross-instance
                scope that can be used to reference this responsibility
                elsewhere in this or other OSCAL instances. The locally
                defined UUID of the responsibility can be used to
                reference the data item locally or globally (e.g., in an
                imported OSCAL instance). This UUID should be assigned
                per-subject, which means it should be consistently used
                to identify the same subject across revisions of the
                document.
            :ivar provided_uuid: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Provided
                UUID</ns1:b>: A machine-oriented identifier reference to
                an inherited control implementation that a leveraging
                system is inheriting from a leveraged system.
            """
            description: Optional[MarkupMultilineDatatype] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    "required": True,
                }
            )
            prop: List[OscalMetadataPropertyAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            link: List[OscalMetadataLinkAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
                default_factory=list,
                metadata={
                    "name": "responsible-role",
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            remarks: Optional["OscalSspByComponentAssembly.Export.Responsibility.Remarks"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            uuid: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
                }
            )
            provided_uuid: Optional[str] = field(
                default=None,
                metadata={
                    "name": "provided-uuid",
                    "type": "Attribute",
                    "white_space": "preserve",
                    "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
                }
            )

            @dataclass
            class Remarks:
                h1: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h2: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h3: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h4: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h5: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h6: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                ul: List[ListType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                ol: List[OrderedListType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                pre: List[PreformattedType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                hr: List[object] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                blockquote: List[BlockQuoteType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                p: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                table: List[TableType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                img: List[ImageType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class Inherited:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Inherited Control Implementation</ns1:b>: Describes a control implementation inherited by a leveraging system.

        :ivar description:
        :ivar prop:
        :ivar link:
        :ivar responsible_role:
        :ivar uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Inherited
            Universally Unique Identifier</ns1:b>: A machine-oriented,
            globally unique identifier with cross-instance scope that
            can be used to reference this inherited entry elsewhere in
            this or other OSCAL instances. The locally defined UUID of
            the inherited control implementation can be used to
            reference the data item locally or globally (e.g., in an
            imported OSCAL instance). This UUID should be assigned per-
            subject, which means it should be consistently used to
            identify the same subject across revisions of the document.
        :ivar provided_uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Provided
            UUID</ns1:b>: A machine-oriented identifier reference to an
            inherited control implementation that a leveraging system is
            inheriting from a leveraged system.
        """
        description: Optional[MarkupMultilineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "required": True,
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
            default_factory=list,
            metadata={
                "name": "responsible-role",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )
        provided_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "provided-uuid",
                "type": "Attribute",
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

    @dataclass
    class Satisfied:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Satisfied Control Implementation Responsibility</ns1:b>: Describes how this system satisfies a responsibility imposed by a leveraged system.

        :ivar description:
        :ivar prop:
        :ivar link:
        :ivar responsible_role:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Satisfied
            Universally Unique Identifier</ns1:b>: A machine-oriented,
            globally unique identifier with cross-instance scope that
            can be used to reference this satisfied control
            implementation entry elsewhere in this or other OSCAL
            instances. The locally defined UUID of the control
            implementation can be used to reference the data item
            locally or globally (e.g., in an imported OSCAL instance).
            This UUID should be assigned per-subject, which means it
            should be consistently used to identify the same subject
            across revisions of the document.
        :ivar responsibility_uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Responsibility
            UUID</ns1:b>: A machine-oriented identifier reference to a
            control implementation that satisfies a responsibility
            imposed by a leveraged system.
        """
        description: Optional[MarkupMultilineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "required": True,
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
            default_factory=list,
            metadata={
                "name": "responsible-role",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalSspByComponentAssembly.Satisfied.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )
        responsibility_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "responsibility-uuid",
                "type": "Attribute",
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalSspDataFlowAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Data Flow</ns1:b>: A description of the logical flow of information within the system and across its boundaries, optionally supplemented by diagrams that illustrate these flows.

    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar diagram:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    """
    class Meta:
        name = "oscal-ssp-data-flow-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    diagram: List[OscalSspDiagramAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalSspDataFlowAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalSspNetworkArchitectureAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Network Architecture</ns1:b>: A description of the system's network architecture, optionally supplemented by diagrams that illustrate the network architecture.

    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar diagram:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    """
    class Meta:
        name = "oscal-ssp-network-architecture-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    diagram: List[OscalSspDiagramAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalSspNetworkArchitectureAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalSspSystemInformationAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">System Information</ns1:b>: Contains details about all information types that are stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60."""
    class Meta:
        name = "oscal-ssp-system-information-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    information_type: List["OscalSspSystemInformationAssembly.InformationType"] = field(
        default_factory=list,
        metadata={
            "name": "information-type",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )

    @dataclass
    class InformationType:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Information Type</ns1:b>: Contains details about one information type that is stored, processed, or transmitted by the system, such as privacy information, and those defined in NIST SP 800-60.

        :ivar title:
        :ivar description:
        :ivar categorization:
        :ivar prop:
        :ivar link:
        :ivar confidentiality_impact:
        :ivar integrity_impact:
        :ivar availability_impact:
        :ivar uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Information
            Type Universally Unique Identifier</ns1:b>: A machine-
            oriented, globally unique identifier with cross-instance
            scope that can be used to reference this information type
            elsewhere in this or other OSCAL instances. The locally
            defined UUID of the information type can be used to
            reference the data item locally or globally (e.g., in an
            imported OSCAL instance). This UUID should be assigned per-
            subject, which means it should be consistently used to
            identify the same subject across revisions of the document.
        """
        title: Optional[MarkupLineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "required": True,
            }
        )
        description: Optional[MarkupMultilineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "required": True,
            }
        )
        categorization: List["OscalSspSystemInformationAssembly.InformationType.Categorization"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        confidentiality_impact: Optional[OscalSspImpactAssembly] = field(
            default=None,
            metadata={
                "name": "confidentiality-impact",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        integrity_impact: Optional[OscalSspImpactAssembly] = field(
            default=None,
            metadata={
                "name": "integrity-impact",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        availability_impact: Optional[OscalSspImpactAssembly] = field(
            default=None,
            metadata={
                "name": "availability-impact",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

        @dataclass
        class Categorization:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Information Type Categorization</ns1:b>: A set of information type identifiers qualified by the given identification system used, such as NIST SP 800-60.

            :ivar information_type_id:
            :ivar system: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Information
                Type Identification System</ns1:b>: Specifies the
                information type identification system used.
            """
            information_type_id: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "information-type-id",
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    "white_space": "preserve",
                    "pattern": r"\S(.*\S)?",
                }
            )
            system: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[a-zA-Z][a-zA-Z0-9+\-.]+:.*\S",
                }
            )


@dataclass
class OscalAssessmentCommonAssessmentAssetsAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Assets</ns1:b>: Identifies the assets used to perform this assessment, such as the assessment team, scanning tools, and assumptions."""
    class Meta:
        name = "oscal-assessment-common-assessment-assets-ASSEMBLY"

    component: List[OscalImplementationCommonSystemComponentAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    assessment_platform: List["OscalAssessmentCommonAssessmentAssetsAssembly.AssessmentPlatform"] = field(
        default_factory=list,
        metadata={
            "name": "assessment-platform",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )

    @dataclass
    class AssessmentPlatform:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Platform</ns1:b>: Used to represent the toolset used to perform aspects of the assessment.

        :ivar title:
        :ivar prop:
        :ivar link:
        :ivar uses_component:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment
            Platform Universally Unique Identifier</ns1:b>: A machine-
            oriented, globally unique identifier with cross-instance
            scope that can be used to reference this assessment platform
            elsewhere in this or other OSCAL instances. The locally
            defined UUID of the assessment platform can be used to
            reference the data item locally or globally (e.g., in an
            imported OSCAL instance). This UUID should be assigned per-
            subject, which means it should be consistently used to
            identify the same subject across revisions of the document.
        """
        title: Optional[MarkupLineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        uses_component: List["OscalAssessmentCommonAssessmentAssetsAssembly.AssessmentPlatform.UsesComponent"] = field(
            default_factory=list,
            metadata={
                "name": "uses-component",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalAssessmentCommonAssessmentAssetsAssembly.AssessmentPlatform.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

        @dataclass
        class UsesComponent:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Uses Component</ns1:b>: The set of components that are used by the assessment platform.

            :ivar prop:
            :ivar link:
            :ivar responsible_party:
            :ivar remarks: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
                Additional commentary about the containing object.
            :ivar component_uuid: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Component
                Universally Unique Identifier Reference</ns1:b>: A
                machine-oriented identifier reference to a component
                that is implemented as part of an inventory item.
            """
            prop: List[OscalMetadataPropertyAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            link: List[OscalMetadataLinkAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            responsible_party: List[OscalMetadataResponsiblePartyAssembly] = field(
                default_factory=list,
                metadata={
                    "name": "responsible-party",
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            remarks: Optional["OscalAssessmentCommonAssessmentAssetsAssembly.AssessmentPlatform.UsesComponent.Remarks"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            component_uuid: Optional[str] = field(
                default=None,
                metadata={
                    "name": "component-uuid",
                    "type": "Attribute",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
                }
            )

            @dataclass
            class Remarks:
                h1: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h2: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h3: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h4: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h5: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h6: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                ul: List[ListType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                ol: List[OrderedListType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                pre: List[PreformattedType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                hr: List[object] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                blockquote: List[BlockQuoteType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                p: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                table: List[TableType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                img: List[ImageType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )


@dataclass
class OscalAssessmentCommonRelatedTaskAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Task Reference</ns1:b>: Identifies an individual task for which the containing object is a consequence of.

    :ivar prop:
    :ivar link:
    :ivar responsible_party:
    :ivar subject:
    :ivar identified_subject:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar task_uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Task Universally
        Unique Identifier Reference</ns1:b>: A machine-oriented
        identifier reference to a unique task.
    """
    class Meta:
        name = "oscal-assessment-common-related-task-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    responsible_party: List[OscalMetadataResponsiblePartyAssembly] = field(
        default_factory=list,
        metadata={
            "name": "responsible-party",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    subject: List[OscalAssessmentCommonAssessmentSubjectAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    identified_subject: Optional["OscalAssessmentCommonRelatedTaskAssembly.IdentifiedSubject"] = field(
        default=None,
        metadata={
            "name": "identified-subject",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalAssessmentCommonRelatedTaskAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    task_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "task-uuid",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class IdentifiedSubject:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Identified Subject</ns1:b>: Used to detail assessment subjects that were identfied by this task.

        :ivar subject:
        :ivar subject_placeholder_uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment
            Subject Placeholder Universally Unique Identifier
            Reference</ns1:b>: A machine-oriented identifier reference
            to a unique assessment subject placeholder defined by this
            task.
        """
        subject: List[OscalAssessmentCommonAssessmentSubjectAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "min_occurs": 1,
            }
        )
        subject_placeholder_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "subject-placeholder-uuid",
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalAssessmentCommonTaskAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Task</ns1:b>: Represents a scheduled event or milestone, which may be associated with a series of assessment actions.

    :ivar title:
    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar timing:
    :ivar dependency:
    :ivar task:
    :ivar associated_activity:
    :ivar subject:
    :ivar responsible_role:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Task Universally
        Unique Identifier</ns1:b>
    :ivar type_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Task Type</ns1:b>:
        The type of task.
    """
    class Meta:
        name = "oscal-assessment-common-task-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    timing: Optional["OscalAssessmentCommonTaskAssembly.Timing"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    dependency: List["OscalAssessmentCommonTaskAssembly.Dependency"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    task: List["OscalAssessmentCommonTaskAssembly"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    associated_activity: List["OscalAssessmentCommonTaskAssembly.AssociatedActivity"] = field(
        default_factory=list,
        metadata={
            "name": "associated-activity",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    subject: List[OscalAssessmentCommonAssessmentSubjectAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
        default_factory=list,
        metadata={
            "name": "responsible-role",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalAssessmentCommonTaskAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Timing:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Event Timing</ns1:b>: The timing under which the task is intended to occur."""
        on_date: Optional["OscalAssessmentCommonTaskAssembly.Timing.OnDate"] = field(
            default=None,
            metadata={
                "name": "on-date",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        within_date_range: Optional["OscalAssessmentCommonTaskAssembly.Timing.WithinDateRange"] = field(
            default=None,
            metadata={
                "name": "within-date-range",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        at_frequency: Optional["OscalAssessmentCommonTaskAssembly.Timing.AtFrequency"] = field(
            default=None,
            metadata={
                "name": "at-frequency",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )

        @dataclass
        class OnDate:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">On Date Condition</ns1:b>: The task is intended to occur on the specified date.

            :ivar date: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">On Date
                Condition</ns1:b>: The task must occur on the specified
                date.
            """
            date: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
                }
            )

        @dataclass
        class WithinDateRange:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">On Date Range Condition</ns1:b>: The task is intended to occur within the specified date range.

            :ivar start: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Start Date
                Condition</ns1:b>: The task must occur on or after the
                specified date.
            :ivar end: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">End Date
                Condition</ns1:b>: The task must occur on or before the
                specified date.
            """
            start: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
                }
            )
            end: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
                }
            )

        @dataclass
        class AtFrequency:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Frequency Condition</ns1:b>: The task is intended to occur at the specified frequency.

            :ivar period: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Period</ns1:b>:
                The task must occur after the specified period has
                elapsed.
            :ivar unit: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Time
                Unit</ns1:b>: The unit of time for the period.
            """
            period: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"\S(.*\S)?",
                }
            )
            unit: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"\S(.*\S)?",
                }
            )

    @dataclass
    class Dependency:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Task Dependency</ns1:b>: Used to indicate that a task is dependent on another task.

        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar task_uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Task
            Universally Unique Identifier Reference</ns1:b>: A machine-
            oriented identifier reference to a unique task.
        """
        remarks: Optional["OscalAssessmentCommonTaskAssembly.Dependency.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        task_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "task-uuid",
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class AssociatedActivity:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Associated Activity</ns1:b>: Identifies an individual activity to be performed as part of a task.

        :ivar prop:
        :ivar link:
        :ivar responsible_role:
        :ivar subject:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar activity_uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Activity
            Universally Unique Identifier Reference</ns1:b>: A machine-
            oriented identifier reference to an activity defined in the
            list of activities.
        """
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
            default_factory=list,
            metadata={
                "name": "responsible-role",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        subject: List[OscalAssessmentCommonAssessmentSubjectAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "min_occurs": 1,
            }
        )
        remarks: Optional["OscalAssessmentCommonTaskAssembly.AssociatedActivity.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        activity_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "activity-uuid",
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalCatalogControlAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control</ns1:b>: A structured object representing a requirement or guideline, which when implemented will reduce an aspect of risk related to an information system and its information.

    :ivar title:
    :ivar param:
    :ivar prop:
    :ivar link:
    :ivar part:
    :ivar mapping:
    :ivar control:
    :ivar id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control
        Identifier</ns1:b>: Identifies a control such that it can be
        referenced in the defining catalog and other OSCAL instances
        (e.g., profiles).
    :ivar class_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control
        Class</ns1:b>: A textual label that provides a sub-type or
        characterization of the control.
    """
    class Meta:
        name = "oscal-catalog-control-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    param: List[OscalControlCommonParameterAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    part: List[OscalControlCommonPartAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    mapping: Optional["OscalCatalogControlAssembly.Mapping"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    control: List["OscalCatalogControlAssembly"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Mapping:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Mapping</ns1:b>: A mapping between the containing control and another resource.

        :ivar target_resource:
        :ivar map:
        :ivar uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Mapping
            Identifier</ns1:b>: The unique identifier for the mapping.
        """
        target_resource: Optional[OscalMappingCommonMappingResourceReferenceAssembly] = field(
            default=None,
            metadata={
                "name": "target-resource",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "required": True,
            }
        )
        map: List[OscalMappingCommonMapAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "min_occurs": 1,
            }
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )


@dataclass
class OscalComponentDefinitionImplementedRequirementAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Implementation</ns1:b>: Describes how the containing component or capability implements an individual control.

    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar set_parameter:
    :ivar responsible_role:
    :ivar statement:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control
        Implementation Identifier</ns1:b>: Provides a globally unique
        means to identify a given control implementation by a component.
    :ivar control_id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Identifier
        Reference</ns1:b>: A reference to a control with a corresponding
        id value. When referencing an externally defined control, the
        Control Identifier Reference must be used in the context of the
        external / imported OSCAL instance (e.g., uri-reference).
    """
    class Meta:
        name = "oscal-component-definition-implemented-requirement-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    set_parameter: List[OscalImplementationCommonSetParameterAssembly] = field(
        default_factory=list,
        metadata={
            "name": "set-parameter",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
        default_factory=list,
        metadata={
            "name": "responsible-role",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    statement: List[OscalComponentDefinitionStatementAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalComponentDefinitionImplementedRequirementAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    control_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "control-id",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalMappingMappingAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Mapping</ns1:b>: A mapping between two target resources.

    :ivar source_resource:
    :ivar target_resource:
    :ivar map:
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Mapping
        Universally Unique Identifier</ns1:b>: A machine-oriented,
        globally unique identifier with cross-instance scope that can be
        used to reference this mapping definition elsewhere in this or
        other OSCAL instances. The locally defined UUID of the mapping
        can be used to reference the data item locally or globally
        (e.g., in an imported OSCAL instance). This UUID should be
        assigned per-subject, which means it should be consistently used
        to identify the same mapping across revisions of the document.
    """
    class Meta:
        name = "oscal-mapping-mapping-ASSEMBLY"

    source_resource: Optional[OscalMappingCommonMappingResourceReferenceAssembly] = field(
        default=None,
        metadata={
            "name": "source-resource",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    target_resource: Optional[OscalMappingCommonMappingResourceReferenceAssembly] = field(
        default=None,
        metadata={
            "name": "target-resource",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    map: List[OscalMappingCommonMapAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )


@dataclass
class OscalMetadataMetadataAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Document Metadata</ns1:b>: Provides information about the containing document, and defines concepts that are shared across the document.

    :ivar title:
    :ivar published:
    :ivar last_modified:
    :ivar version:
    :ivar oscal_version:
    :ivar revisions: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">revisions</ns1:b>:
        A group of 'revision' elements
    :ivar document_id:
    :ivar prop:
    :ivar link:
    :ivar role:
    :ivar location:
    :ivar party:
    :ivar responsible_party:
    :ivar action:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    """
    class Meta:
        name = "oscal-metadata-metadata-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    published: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
        }
    )
    last_modified: Optional[str] = field(
        default=None,
        metadata={
            "name": "last-modified",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
            "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    oscal_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "oscal-version",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    revisions: Optional["OscalMetadataMetadataAssembly.Revisions"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    document_id: List[OscalMetadataDocumentIdField] = field(
        default_factory=list,
        metadata={
            "name": "document-id",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    role: List["OscalMetadataMetadataAssembly.Role"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    location: List["OscalMetadataMetadataAssembly.Location"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    party: List["OscalMetadataMetadataAssembly.Party"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    responsible_party: List[OscalMetadataResponsiblePartyAssembly] = field(
        default_factory=list,
        metadata={
            "name": "responsible-party",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    action: List[OscalMetadataActionAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalMetadataMetadataAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )

    @dataclass
    class Revisions:
        revision: List["OscalMetadataMetadataAssembly.Revisions.Revision"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )

        @dataclass
        class Revision:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Revision History Entry</ns1:b>: An entry in a sequential list of revisions to the containing document, expected to be in reverse chronological order (i.e. latest first).

            :ivar title:
            :ivar published:
            :ivar last_modified:
            :ivar version:
            :ivar oscal_version:
            :ivar prop:
            :ivar link:
            :ivar remarks: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
                Additional commentary about the containing object.
            """
            title: Optional[MarkupLineDatatype] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            published: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
                }
            )
            last_modified: Optional[str] = field(
                default=None,
                metadata={
                    "name": "last-modified",
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
                }
            )
            version: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"\S(.*\S)?",
                }
            )
            oscal_version: Optional[str] = field(
                default=None,
                metadata={
                    "name": "oscal-version",
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    "white_space": "preserve",
                    "pattern": r"\S(.*\S)?",
                }
            )
            prop: List[OscalMetadataPropertyAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            link: List[OscalMetadataLinkAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            remarks: Optional["OscalMetadataMetadataAssembly.Revisions.Revision.Remarks"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

            @dataclass
            class Remarks:
                h1: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h2: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h3: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h4: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h5: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h6: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                ul: List[ListType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                ol: List[OrderedListType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                pre: List[PreformattedType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                hr: List[object] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                blockquote: List[BlockQuoteType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                p: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                table: List[TableType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                img: List[ImageType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )

    @dataclass
    class Role:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Role</ns1:b>: Defines a function, which might be assigned to a party in a specific situation.

        :ivar title:
        :ivar short_name:
        :ivar description:
        :ivar prop:
        :ivar link:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar id: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Role
            Identifier</ns1:b>: A unique identifier for the role.
        """
        title: Optional[MarkupLineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "required": True,
            }
        )
        short_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "short-name",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "white_space": "preserve",
                "pattern": r"\S(.*\S)?",
            }
        )
        description: Optional[MarkupMultilineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalMetadataMetadataAssembly.Role.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class Location:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Location</ns1:b>: A physical point of presence, which may be associated with people, organizations, or other concepts within the current or linked OSCAL document.

        :ivar title:
        :ivar address:
        :ivar email_address:
        :ivar telephone_number:
        :ivar url:
        :ivar prop:
        :ivar link:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Location
            Universally Unique Identifier</ns1:b>: A unique ID for the
            location, for reference.
        """
        title: Optional[MarkupLineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        address: Optional[OscalMetadataAddressAssembly] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        email_address: List[str] = field(
            default_factory=list,
            metadata={
                "name": "email-address",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "white_space": "preserve",
                "pattern": r".+@.+",
            }
        )
        telephone_number: List[OscalMetadataTelephoneNumberField] = field(
            default_factory=list,
            metadata={
                "name": "telephone-number",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        url: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "pattern": r"[a-zA-Z][a-zA-Z0-9+\-.]+:.*\S",
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalMetadataMetadataAssembly.Location.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class Party:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Party</ns1:b>: An organization or person, which may be associated with roles or other concepts within the current or linked OSCAL document.

        :ivar name:
        :ivar short_name:
        :ivar external_id:
        :ivar prop:
        :ivar link:
        :ivar email_address:
        :ivar telephone_number:
        :ivar address:
        :ivar location_uuid:
        :ivar member_of_organization:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Party
            Universally Unique Identifier</ns1:b>: A unique identifier
            for the party.
        :ivar type_value: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Party
            Type</ns1:b>: A category describing the kind of party the
            object describes.
        """
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "white_space": "preserve",
                "pattern": r"\S(.*\S)?",
            }
        )
        short_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "short-name",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "white_space": "preserve",
                "pattern": r"\S(.*\S)?",
            }
        )
        external_id: List["OscalMetadataMetadataAssembly.Party.ExternalId"] = field(
            default_factory=list,
            metadata={
                "name": "external-id",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        email_address: List[str] = field(
            default_factory=list,
            metadata={
                "name": "email-address",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "white_space": "preserve",
                "pattern": r".+@.+",
            }
        )
        telephone_number: List[OscalMetadataTelephoneNumberField] = field(
            default_factory=list,
            metadata={
                "name": "telephone-number",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        address: List[OscalMetadataAddressAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        location_uuid: List[str] = field(
            default_factory=list,
            metadata={
                "name": "location-uuid",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )
        member_of_organization: List[str] = field(
            default_factory=list,
            metadata={
                "name": "member-of-organization",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )
        remarks: Optional["OscalMetadataMetadataAssembly.Party.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )
        type_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "type",
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"\S(.*\S)?",
            }
        )

        @dataclass
        class ExternalId:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Party External Identifier</ns1:b>: An identifier for a person or organization using a designated scheme. e.g. an Open Researcher and Contributor ID (ORCID).

            :ivar value:
            :ivar scheme: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">External
                Identifier Schema</ns1:b>: Indicates the type of
                external identifier.
            """
            value: str = field(
                default="",
                metadata={
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"\S(.*\S)?",
                }
            )
            scheme: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[a-zA-Z][a-zA-Z0-9+\-.]+:.*\S",
                }
            )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalProfileGroupAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Group</ns1:b>: A group of (selected) controls or of groups of controls.

    :ivar title:
    :ivar param:
    :ivar prop:
    :ivar link:
    :ivar part:
    :ivar group:
    :ivar insert_controls:
    :ivar id: <ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Group
        Identifier</ns1:b>: Identifies the group.
    :ivar class_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Group
        Class</ns1:b>: A textual label that provides a sub-type or
        characterization of the group.
    """
    class Meta:
        name = "oscal-profile-group-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    param: List[OscalControlCommonParameterAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    part: List[OscalControlCommonPartAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    group: List["OscalProfileGroupAssembly"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    insert_controls: List[OscalProfileInsertControlsAssembly] = field(
        default_factory=list,
        metadata={
            "name": "insert-controls",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )


@dataclass
class OscalProfileModifyAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Modify Controls</ns1:b>: Set parameters or amend controls in resolution."""
    class Meta:
        name = "oscal-profile-modify-ASSEMBLY"

    set_parameter: List["OscalProfileModifyAssembly.SetParameter"] = field(
        default_factory=list,
        metadata={
            "name": "set-parameter",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    alter: List["OscalProfileModifyAssembly.Alter"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )

    @dataclass
    class SetParameter:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Parameter Setting</ns1:b>: A parameter setting, to be propagated to points of insertion.

        :ivar prop:
        :ivar link:
        :ivar label:
        :ivar usage:
        :ivar constraint:
        :ivar guideline:
        :ivar value:
        :ivar select:
        :ivar param_id: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Parameter
            ID</ns1:b>: An identifier for the parameter.
        :ivar class_value: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Parameter
            Class</ns1:b>: A textual label that provides a
            characterization of the parameter.
        :ivar depends_on: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Depends
            On</ns1:b>: **(deprecated)** Another parameter invoking this
            one. This construct has been deprecated and should not be
            used.
        """
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        label: Optional[MarkupLineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        usage: Optional[MarkupMultilineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        constraint: List[OscalControlCommonParameterConstraintAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        guideline: List[OscalControlCommonParameterGuidelineAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        value: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "white_space": "preserve",
                "pattern": r"\S(.*\S)?",
            }
        )
        select: Optional[OscalControlCommonParameterSelectionAssembly] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        param_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "param-id",
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
            }
        )
        class_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "class",
                "type": "Attribute",
                "white_space": "preserve",
                "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
            }
        )
        depends_on: Optional[str] = field(
            default=None,
            metadata={
                "name": "depends-on",
                "type": "Attribute",
                "white_space": "preserve",
                "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
            }
        )

    @dataclass
    class Alter:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Alteration</ns1:b>: Specifies changes to be made to an included control when a profile is resolved.

        :ivar remove:
        :ivar add:
        :ivar control_id: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control
            Identifier Reference</ns1:b>: A reference to a control with
            a corresponding id value. When referencing an externally
            defined control, the Control Identifier Reference must be
            used in the context of the external / imported OSCAL
            instance (e.g., uri-reference).
        """
        remove: List["OscalProfileModifyAssembly.Alter.Remove"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        add: List["OscalProfileModifyAssembly.Alter.Add"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        control_id: Optional[str] = field(
            default=None,
            metadata={
                "name": "control-id",
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
            }
        )

        @dataclass
        class Remove:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Removal</ns1:b>: Specifies objects to be removed from a control based on specific aspects of the object that must all match.

            :ivar by_name: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Reference
                by (assigned) name</ns1:b>: Identify items remove by
                matching their assigned name.
            :ivar by_class: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Reference
                by class</ns1:b>: Identify items to remove by matching
                their class.
            :ivar by_id: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Reference
                by ID</ns1:b>: Identify items to remove indicated by
                their id.
            :ivar by_item_name: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Item Name
                Reference</ns1:b>: Identify items to remove by the name
                of the item's information object name, e.g. title or
                prop.
            :ivar by_ns: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Item
                Namespace Reference</ns1:b>: Identify items to remove by
                the item's ns, which is the namespace associated with a
                part, or prop.
            """
            by_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "by-name",
                    "type": "Attribute",
                    "white_space": "preserve",
                    "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
                }
            )
            by_class: Optional[str] = field(
                default=None,
                metadata={
                    "name": "by-class",
                    "type": "Attribute",
                    "white_space": "preserve",
                    "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
                }
            )
            by_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "by-id",
                    "type": "Attribute",
                    "white_space": "preserve",
                    "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
                }
            )
            by_item_name: Optional[str] = field(
                default=None,
                metadata={
                    "name": "by-item-name",
                    "type": "Attribute",
                    "white_space": "preserve",
                    "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
                }
            )
            by_ns: Optional[str] = field(
                default=None,
                metadata={
                    "name": "by-ns",
                    "type": "Attribute",
                    "white_space": "preserve",
                    "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
                }
            )

        @dataclass
        class Add:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Addition</ns1:b>: Specifies contents to be added into controls, in resolution.

            :ivar title:
            :ivar param:
            :ivar prop:
            :ivar link:
            :ivar part:
            :ivar position: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Position</ns1:b>:
                Where to add the new content with respect to the
                targeted element (beside it or inside it).
            :ivar by_id: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Reference
                by ID</ns1:b>: Target location of the addition.
            """
            title: Optional[MarkupLineDatatype] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            param: List[OscalControlCommonParameterAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            prop: List[OscalMetadataPropertyAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            link: List[OscalMetadataLinkAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            part: List[OscalControlCommonPartAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            position: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "white_space": "preserve",
                    "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
                }
            )
            by_id: Optional[str] = field(
                default=None,
                metadata={
                    "name": "by-id",
                    "type": "Attribute",
                    "white_space": "preserve",
                    "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
                }
            )


@dataclass
class OscalSspStatementAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Specific Control Statement</ns1:b>: Identifies which statements within a control are addressed.

    :ivar prop:
    :ivar link:
    :ivar responsible_role:
    :ivar by_component:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar statement_id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Statement
        Reference</ns1:b>: A human-oriented identifier reference to a
        control statement.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Statement
        Reference Universally Unique Identifier</ns1:b>: A machine-
        oriented, globally unique identifier with cross-instance scope
        that can be used to reference this control statement elsewhere
        in this or other OSCAL instances. The UUID of the control
        statement in the source OSCAL instance is sufficient to
        reference the data item locally or globally (e.g., in an
        imported OSCAL instance).
    """
    class Meta:
        name = "oscal-ssp-statement-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
        default_factory=list,
        metadata={
            "name": "responsible-role",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    by_component: List[OscalSspByComponentAssembly] = field(
        default_factory=list,
        metadata={
            "name": "by-component",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalSspStatementAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    statement_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "statement-id",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalSspSystemCharacteristicsAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">System Characteristics</ns1:b>: Contains the characteristics of the system, such as its name, purpose, and security impact level.

    :ivar system_id:
    :ivar system_name:
    :ivar system_name_short:
    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar date_authorized:
    :ivar security_sensitivity_level:
    :ivar system_information:
    :ivar security_impact_level:
    :ivar status:
    :ivar authorization_boundary:
    :ivar network_architecture:
    :ivar data_flow:
    :ivar responsible_party:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    """
    class Meta:
        name = "oscal-ssp-system-characteristics-ASSEMBLY"

    system_id: List[OscalImplementationCommonSystemIdField] = field(
        default_factory=list,
        metadata={
            "name": "system-id",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    system_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "system-name",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    system_name_short: Optional[str] = field(
        default=None,
        metadata={
            "name": "system-name-short",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    date_authorized: Optional[str] = field(
        default=None,
        metadata={
            "name": "date-authorized",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))(Z|[+-][0-9]{2}:[0-9]{2})?",
        }
    )
    security_sensitivity_level: Optional[str] = field(
        default=None,
        metadata={
            "name": "security-sensitivity-level",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    system_information: Optional[OscalSspSystemInformationAssembly] = field(
        default=None,
        metadata={
            "name": "system-information",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    security_impact_level: Optional[OscalSspSecurityImpactLevelAssembly] = field(
        default=None,
        metadata={
            "name": "security-impact-level",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    status: Optional[OscalSspStatusAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    authorization_boundary: Optional[OscalSspAuthorizationBoundaryAssembly] = field(
        default=None,
        metadata={
            "name": "authorization-boundary",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    network_architecture: Optional[OscalSspNetworkArchitectureAssembly] = field(
        default=None,
        metadata={
            "name": "network-architecture",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    data_flow: Optional[OscalSspDataFlowAssembly] = field(
        default=None,
        metadata={
            "name": "data-flow",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    responsible_party: List[OscalMetadataResponsiblePartyAssembly] = field(
        default_factory=list,
        metadata={
            "name": "responsible-party",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalSspSystemCharacteristicsAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalSspSystemImplementationAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">System Implementation</ns1:b>: Provides information as to how the system is implemented.

    :ivar prop:
    :ivar link:
    :ivar leveraged_authorization:
    :ivar user:
    :ivar component:
    :ivar inventory_item:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    """
    class Meta:
        name = "oscal-ssp-system-implementation-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    leveraged_authorization: List["OscalSspSystemImplementationAssembly.LeveragedAuthorization"] = field(
        default_factory=list,
        metadata={
            "name": "leveraged-authorization",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    user: List[OscalImplementationCommonSystemUserAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    component: List[OscalImplementationCommonSystemComponentAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    inventory_item: List[OscalImplementationCommonInventoryItemAssembly] = field(
        default_factory=list,
        metadata={
            "name": "inventory-item",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalSspSystemImplementationAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )

    @dataclass
    class LeveragedAuthorization:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Leveraged Authorization</ns1:b>: A description of another authorized system from which this system inherits capabilities that satisfy security requirements. Another term for this concept is a common control provider.

        :ivar title:
        :ivar prop:
        :ivar link:
        :ivar party_uuid:
        :ivar date_authorized:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Leveraged
            Authorization Universally Unique Identifier</ns1:b>: A
            machine-oriented, globally unique identifier with cross-
            instance scope and can be used to reference this leveraged
            authorization elsewhere in this or other OSCAL instances.
            The locally defined UUID of the leveraged authorization can
            be used to reference the data item locally or globally
            (e.g., in an imported OSCAL instance). This UUID should be
            assigned per-subject, which means it should be consistently
            used to identify the same subject across revisions of the
            document.
        """
        title: Optional[MarkupLineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "required": True,
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        party_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "party-uuid",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )
        date_authorized: Optional[str] = field(
            default=None,
            metadata={
                "name": "date-authorized",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "required": True,
                "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))(Z|[+-][0-9]{2}:[0-9]{2})?",
            }
        )
        remarks: Optional["OscalSspSystemImplementationAssembly.LeveragedAuthorization.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalApAssessmentPlanAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Security Assessment Plan (SAP)</ns1:b>: An assessment plan, such as those provided by a FedRAMP assessor.

    :ivar metadata:
    :ivar import_ssp:
    :ivar local_definitions:
    :ivar terms_and_conditions:
    :ivar reviewed_controls:
    :ivar assessment_subject:
    :ivar assessment_assets:
    :ivar task:
    :ivar back_matter:
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Plan
        Universally Unique Identifier</ns1:b>: A machine-oriented,
        globally unique identifier with cross-instance scope that can be
        used to reference this assessment plan in this or other OSCAL
        instances. The locally defined UUID of the assessment plan can
        be used to reference the data item locally or globally (e.g., in
        an imported OSCAL instance). This UUID should be assigned per-
        subject, which means it should be consistently used to identify
        the same subject across revisions of the document.
    """
    class Meta:
        name = "oscal-ap-assessment-plan-ASSEMBLY"

    metadata: Optional[OscalMetadataMetadataAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    import_ssp: Optional[OscalAssessmentCommonImportSspAssembly] = field(
        default=None,
        metadata={
            "name": "import-ssp",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    local_definitions: Optional["OscalApAssessmentPlanAssembly.LocalDefinitions"] = field(
        default=None,
        metadata={
            "name": "local-definitions",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    terms_and_conditions: Optional["OscalApAssessmentPlanAssembly.TermsAndConditions"] = field(
        default=None,
        metadata={
            "name": "terms-and-conditions",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    reviewed_controls: Optional[OscalAssessmentCommonReviewedControlsAssembly] = field(
        default=None,
        metadata={
            "name": "reviewed-controls",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    assessment_subject: List[OscalAssessmentCommonAssessmentSubjectAssembly] = field(
        default_factory=list,
        metadata={
            "name": "assessment-subject",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    assessment_assets: Optional[OscalAssessmentCommonAssessmentAssetsAssembly] = field(
        default=None,
        metadata={
            "name": "assessment-assets",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    task: List[OscalAssessmentCommonTaskAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    back_matter: Optional[OscalMetadataBackMatterAssembly] = field(
        default=None,
        metadata={
            "name": "back-matter",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class LocalDefinitions:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Local Definitions</ns1:b>: Used to define data objects that are used in the assessment plan, that do not appear in the referenced SSP.

        :ivar component:
        :ivar inventory_item:
        :ivar user:
        :ivar objectives_and_methods:
        :ivar activity:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        """
        component: List[OscalImplementationCommonSystemComponentAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        inventory_item: List[OscalImplementationCommonInventoryItemAssembly] = field(
            default_factory=list,
            metadata={
                "name": "inventory-item",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        user: List[OscalImplementationCommonSystemUserAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        objectives_and_methods: List[OscalAssessmentCommonLocalObjectiveAssembly] = field(
            default_factory=list,
            metadata={
                "name": "objectives-and-methods",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        activity: List[OscalAssessmentCommonActivityAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalApAssessmentPlanAssembly.LocalDefinitions.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class TermsAndConditions:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Plan Terms and Conditions</ns1:b>: Used to define various terms and conditions under which an assessment, described by the plan, can be performed. Each child part defines a different type of term or condition."""
        part: List[OscalAssessmentCommonAssessmentPartAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalAssessmentCommonOriginAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Origin</ns1:b>: Identifies the source of the finding, such as a tool, interviewed person, or activity."""
    class Meta:
        name = "oscal-assessment-common-origin-ASSEMBLY"

    actor: List[OscalAssessmentCommonOriginActorAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    related_task: List[OscalAssessmentCommonRelatedTaskAssembly] = field(
        default_factory=list,
        metadata={
            "name": "related-task",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )


@dataclass
class OscalCatalogGroupAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Group</ns1:b>: A group of controls, or of groups of controls.

    :ivar title:
    :ivar param:
    :ivar prop:
    :ivar link:
    :ivar part:
    :ivar group:
    :ivar control:
    :ivar id: <ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Group
        Identifier</ns1:b>: Identifies the group for the purpose of
        cross-linking within the defining instance or from other
        instances that reference the catalog.
    :ivar class_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Group
        Class</ns1:b>: A textual label that provides a sub-type or
        characterization of the group.
    """
    class Meta:
        name = "oscal-catalog-group-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    param: List[OscalControlCommonParameterAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    part: List[OscalControlCommonPartAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    group: List["OscalCatalogGroupAssembly"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    control: List[OscalCatalogControlAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "class",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )


@dataclass
class OscalComponentDefinitionControlImplementationAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Implementation Set</ns1:b>: Defines how the component or capability supports a set of controls.

    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar set_parameter:
    :ivar implemented_requirement:
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control
        Implementation Set Identifier</ns1:b>: Provides a means to
        identify a set of control implementations that are supported by
        a given component or capability.
    :ivar source: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Source Resource
        Reference</ns1:b>: A reference to an OSCAL catalog or profile
        providing the referenced control or subcontrol definition.
    """
    class Meta:
        name = "oscal-component-definition-control-implementation-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    set_parameter: List[OscalImplementationCommonSetParameterAssembly] = field(
        default_factory=list,
        metadata={
            "name": "set-parameter",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    implemented_requirement: List[OscalComponentDefinitionImplementedRequirementAssembly] = field(
        default_factory=list,
        metadata={
            "name": "implemented-requirement",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"\S(.*\S)?",
        }
    )


@dataclass
class OscalMappingMappingCollectionAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Mapping Collection</ns1:b>: A collection of relationship-based control and/or control statement mappings.

    :ivar metadata:
    :ivar provenance:
    :ivar mapping:
    :ivar back_matter:
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Mapping Collection
        Universally Unique Identifier</ns1:b>: A globally unique
        identifier with cross-instance scope for this catalog instance.
        This UUID should be changed when this document is revised.
    """
    class Meta:
        name = "oscal-mapping-mapping-collection-ASSEMBLY"

    metadata: Optional[OscalMetadataMetadataAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    provenance: Optional[OscalMappingCommonMappingProvenanceAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    mapping: List[OscalMappingMappingAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    back_matter: Optional[OscalMetadataBackMatterAssembly] = field(
        default=None,
        metadata={
            "name": "back-matter",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )


@dataclass
class OscalPoamLocalDefinitionsAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Local Definitions</ns1:b>: Allows components, and inventory-items to be defined within the POA&amp;M for circumstances where no OSCAL-based SSP exists, or is not delivered with the POA&amp;M.

    :ivar component:
    :ivar inventory_item:
    :ivar assessment_assets:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    """
    class Meta:
        name = "oscal-poam-local-definitions-ASSEMBLY"

    component: List[OscalImplementationCommonSystemComponentAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    inventory_item: List[OscalImplementationCommonInventoryItemAssembly] = field(
        default_factory=list,
        metadata={
            "name": "inventory-item",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    assessment_assets: Optional[OscalAssessmentCommonAssessmentAssetsAssembly] = field(
        default=None,
        metadata={
            "name": "assessment-assets",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalPoamLocalDefinitionsAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalProfileMergeAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Merge Controls</ns1:b>: Provides structuring directives that instruct how controls are organized after profile resolution."""
    class Meta:
        name = "oscal-profile-merge-ASSEMBLY"

    combine: Optional["OscalProfileMergeAssembly.Combine"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    flat: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    as_is: Optional[str] = field(
        default=None,
        metadata={
            "name": "as-is",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "pattern": r"true|1|false|0",
        }
    )
    custom: Optional["OscalProfileMergeAssembly.Custom"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )

    @dataclass
    class Combine:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Combination Rule</ns1:b>: A Combine element defines how to resolve duplicate instances of the same control (e.g., controls with the same ID).

        :ivar method: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Combination
            Method</ns1:b>: Declare how clashing controls should be
            handled.
        """
        method: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "white_space": "preserve",
                "pattern": r"\S(.*\S)?",
            }
        )

    @dataclass
    class Custom:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Custom Grouping</ns1:b>: Provides an alternate grouping structure that selected controls will be placed in."""
        group: List[OscalProfileGroupAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        insert_controls: List[OscalProfileInsertControlsAssembly] = field(
            default_factory=list,
            metadata={
                "name": "insert-controls",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalSspImplementedRequirementAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control-based Requirement</ns1:b>: Describes how the system satisfies the requirements of an individual control.

    :ivar prop:
    :ivar link:
    :ivar set_parameter:
    :ivar responsible_role:
    :ivar statement:
    :ivar by_component:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control
        Requirement Universally Unique Identifier</ns1:b>: A machine-
        oriented, globally unique identifier with cross-instance scope
        that can be used to reference this control requirement elsewhere
        in this or other OSCAL instances. The locally defined UUID of
        the control requirement can be used to reference the data item
        locally or globally (e.g., in an imported OSCAL instance). This
        UUID should be assigned per-subject, which means it should be
        consistently used to identify the same subject across revisions
        of the document.
    :ivar control_id: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Identifier
        Reference</ns1:b>: A reference to a control with a corresponding
        id value. When referencing an externally defined control, the
        Control Identifier Reference must be used in the context of the
        external / imported OSCAL instance (e.g., uri-reference).
    """
    class Meta:
        name = "oscal-ssp-implemented-requirement-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    set_parameter: List[OscalImplementationCommonSetParameterAssembly] = field(
        default_factory=list,
        metadata={
            "name": "set-parameter",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
        default_factory=list,
        metadata={
            "name": "responsible-role",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    statement: List[OscalSspStatementAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    by_component: List[OscalSspByComponentAssembly] = field(
        default_factory=list,
        metadata={
            "name": "by-component",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalSspImplementedRequirementAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    control_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "control-id",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class AssessmentPlan(OscalApAssessmentPlanAssembly):
    class Meta:
        name = "assessment-plan"
        namespace = "http://csrc.nist.gov/ns/oscal/1.0"


@dataclass
class MappingCollection(OscalMappingMappingCollectionAssembly):
    class Meta:
        name = "mapping-collection"
        namespace = "http://csrc.nist.gov/ns/oscal/1.0"


@dataclass
class OscalAssessmentCommonCharacterizationAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Characterization</ns1:b>: A collection of descriptive data about the containing object from a specific origin."""
    class Meta:
        name = "oscal-assessment-common-characterization-ASSEMBLY"

    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    origin: Optional[OscalAssessmentCommonOriginAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    facet: List["OscalAssessmentCommonCharacterizationAssembly.Facet"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Facet:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Facet</ns1:b>: An individual characteristic that is part of a larger set produced by the same actor.

        :ivar prop:
        :ivar link:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar name: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Facet
            Name</ns1:b>: The name of the risk metric within the
            specified system.
        :ivar system: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Naming
            System</ns1:b>: Specifies the naming system under which this
            risk metric is organized, which allows for the same names to
            be used in different systems controlled by different
            parties. This avoids the potential of a name clash.
        :ivar value: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Facet
            Value</ns1:b>: Indicates the value of the facet.
        """
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalAssessmentCommonCharacterizationAssembly.Facet.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        name: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
            }
        )
        system: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[a-zA-Z][a-zA-Z0-9+\-.]+:.*\S",
            }
        )
        value: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"\S(.*\S)?",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )


@dataclass
class OscalAssessmentCommonFindingAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Finding</ns1:b>: Describes an individual finding.

    :ivar title:
    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar origin:
    :ivar target:
    :ivar implementation_statement_uuid:
    :ivar related_observation:
    :ivar associated_risk:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Finding
        Universally Unique Identifier</ns1:b>: A machine-oriented,
        globally unique identifier with cross-instance scope that can be
        used to reference this finding in this or other OSCAL instances.
        The locally defined UUID of the finding can be used to reference
        the data item locally or globally (e.g., in an imported OSCAL
        instance). This UUID should be assigned per-subject, which means
        it should be consistently used to identify the same subject
        across revisions of the document.
    """
    class Meta:
        name = "oscal-assessment-common-finding-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    origin: List[OscalAssessmentCommonOriginAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    target: Optional[OscalAssessmentCommonFindingTargetAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    implementation_statement_uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "implementation-statement-uuid",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    related_observation: List["OscalAssessmentCommonFindingAssembly.RelatedObservation"] = field(
        default_factory=list,
        metadata={
            "name": "related-observation",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    associated_risk: List["OscalAssessmentCommonFindingAssembly.AssociatedRisk"] = field(
        default_factory=list,
        metadata={
            "name": "associated-risk",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalAssessmentCommonFindingAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class RelatedObservation:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Related Observation</ns1:b>: Relates the finding to a set of referenced observations that were used to determine the finding.

        :ivar observation_uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Observation
            Universally Unique Identifier Reference</ns1:b>: A machine-
            oriented identifier reference to an observation defined in
            the list of observations.
        """
        observation_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "observation-uuid",
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

    @dataclass
    class AssociatedRisk:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Associated Risk</ns1:b>: Relates the finding to a set of referenced risks that were used to determine the finding.

        :ivar risk_uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Risk
            Universally Unique Identifier Reference</ns1:b>: A machine-
            oriented identifier reference to a risk defined in the list
            of risks.
        """
        risk_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "risk-uuid",
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalAssessmentCommonObservationAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Observation</ns1:b>: Describes an individual observation.

    :ivar title:
    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar method:
    :ivar type_value:
    :ivar origin:
    :ivar subject:
    :ivar relevant_evidence:
    :ivar collected:
    :ivar expires:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Observation
        Universally Unique Identifier</ns1:b>: A machine-oriented,
        globally unique identifier with cross-instance scope that can be
        used to reference this observation elsewhere in this or other
        OSCAL instances. The locally defined UUID of the observation can
        be used to reference the data item locally or globally (e.g., in
        an imorted OSCAL instance). This UUID should be assigned per-
        subject, which means it should be consistently used to identify
        the same subject across revisions of the document.
    """
    class Meta:
        name = "oscal-assessment-common-observation-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    method: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )
    type_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "type",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    origin: List[OscalAssessmentCommonOriginAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    subject: List[OscalAssessmentCommonSubjectReferenceAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    relevant_evidence: List["OscalAssessmentCommonObservationAssembly.RelevantEvidence"] = field(
        default_factory=list,
        metadata={
            "name": "relevant-evidence",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    collected: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
            "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
        }
    )
    expires: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
        }
    )
    remarks: Optional["OscalAssessmentCommonObservationAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class RelevantEvidence:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Relevant Evidence</ns1:b>: Links this observation to relevant evidence.

        :ivar description:
        :ivar prop:
        :ivar link:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar href: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Relevant
            Evidence Reference</ns1:b>
        """
        description: Optional[MarkupMultilineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "required": True,
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalAssessmentCommonObservationAssembly.RelevantEvidence.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        href: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "pattern": r"\S(.*\S)?",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalAssessmentCommonResponseAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Risk Response</ns1:b>: Describes either recommended or an actual plan for addressing the risk.

    :ivar title:
    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar origin:
    :ivar required_asset:
    :ivar task:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remediation
        Universally Unique Identifier</ns1:b>: A machine-oriented,
        globally unique identifier with cross-instance scope that can be
        used to reference this remediation elsewhere in this or other
        OSCAL instances. The locally defined UUID of the risk response
        can be used to reference the data item locally or globally
        (e.g., in an imported OSCAL instance). This UUID should be
        assigned per-subject, which means it should be consistently used
        to identify the same subject across revisions of the document.
    :ivar lifecycle: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remediation
        Intent</ns1:b>: Identifies whether this is a recommendation,
        such as from an assessor or tool, or an actual plan accepted by
        the system owner.
    """
    class Meta:
        name = "oscal-assessment-common-response-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    origin: List[OscalAssessmentCommonOriginAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    required_asset: List["OscalAssessmentCommonResponseAssembly.RequiredAsset"] = field(
        default_factory=list,
        metadata={
            "name": "required-asset",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    task: List[OscalAssessmentCommonTaskAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalAssessmentCommonResponseAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    lifecycle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )

    @dataclass
    class RequiredAsset:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Required Asset</ns1:b>: Identifies an asset required to achieve remediation.

        :ivar subject:
        :ivar title:
        :ivar description:
        :ivar prop:
        :ivar link:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        :ivar uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Required
            Universally Unique Identifier</ns1:b>: A machine-oriented,
            globally unique identifier with cross-instance scope that
            can be used to reference this required asset elsewhere in
            this or other OSCAL instances. The locally defined UUID of
            the asset can be used to reference the data item locally or
            globally (e.g., in an imported OSCAL instance). This UUID
            should be assigned per-subject, which means it should be
            consistently used to identify the same subject across
            revisions of the document.
        """
        subject: List[OscalAssessmentCommonSubjectReferenceAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        title: Optional[MarkupLineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        description: Optional[MarkupMultilineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "required": True,
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalAssessmentCommonResponseAssembly.RequiredAsset.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalCatalogCatalogAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Catalog</ns1:b>: A structured, organized collection of control information.

    :ivar metadata:
    :ivar param:
    :ivar control:
    :ivar group:
    :ivar back_matter:
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Catalog
        Universally Unique Identifier</ns1:b>: Provides a globally
        unique means to identify a given catalog instance.
    """
    class Meta:
        name = "oscal-catalog-catalog-ASSEMBLY"

    metadata: Optional[OscalMetadataMetadataAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    param: List[OscalControlCommonParameterAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    control: List[OscalCatalogControlAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    group: List[OscalCatalogGroupAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    back_matter: Optional[OscalMetadataBackMatterAssembly] = field(
        default=None,
        metadata={
            "name": "back-matter",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )


@dataclass
class OscalComponentDefinitionCapabilityAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Capability</ns1:b>: A grouping of other components and/or capabilities.

    :ivar description:
    :ivar prop:
    :ivar link:
    :ivar incorporates_component:
    :ivar control_implementation:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Capability
        Identifier</ns1:b>: Provides a globally unique means to identify
        a given capability.
    :ivar name: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Capability
        Name</ns1:b>: The capability's human-readable name.
    """
    class Meta:
        name = "oscal-component-definition-capability-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    incorporates_component: List[OscalComponentDefinitionIncorporatesComponentAssembly] = field(
        default_factory=list,
        metadata={
            "name": "incorporates-component",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    control_implementation: List[OscalComponentDefinitionControlImplementationAssembly] = field(
        default_factory=list,
        metadata={
            "name": "control-implementation",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalComponentDefinitionCapabilityAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalComponentDefinitionDefinedComponentAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Component</ns1:b>: A defined component that can be part of an implemented system.

    :ivar title:
    :ivar description:
    :ivar purpose:
    :ivar prop:
    :ivar link:
    :ivar responsible_role:
    :ivar protocol:
    :ivar control_implementation:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Component
        Identifier</ns1:b>: Provides a globally unique means to identify
        a given component.
    :ivar type_value: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Component
        Type</ns1:b>: A category describing the purpose of the
        component.
    """
    class Meta:
        name = "oscal-component-definition-defined-component-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    purpose: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    responsible_role: List[OscalMetadataResponsibleRoleAssembly] = field(
        default_factory=list,
        metadata={
            "name": "responsible-role",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    protocol: List[OscalImplementationCommonProtocolAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    control_implementation: List[OscalComponentDefinitionControlImplementationAssembly] = field(
        default_factory=list,
        metadata={
            "name": "control-implementation",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalComponentDefinitionDefinedComponentAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"\S(.*\S)?",
        }
    )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalProfileProfileAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Profile</ns1:b>: Each OSCAL profile is defined by a profile element.

    :ivar metadata:
    :ivar import_value:
    :ivar merge:
    :ivar modify:
    :ivar back_matter:
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Profile
        Universally Unique Identifier</ns1:b>: Provides a globally
        unique means to identify a given profile instance.
    """
    class Meta:
        name = "oscal-profile-profile-ASSEMBLY"

    metadata: Optional[OscalMetadataMetadataAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    import_value: List[OscalProfileImportAssembly] = field(
        default_factory=list,
        metadata={
            "name": "import",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    merge: Optional[OscalProfileMergeAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    modify: Optional[OscalProfileModifyAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    back_matter: Optional[OscalMetadataBackMatterAssembly] = field(
        default=None,
        metadata={
            "name": "back-matter",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )


@dataclass
class OscalSspControlImplementationAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Control Implementation</ns1:b>: Describes how the system satisfies a set of controls."""
    class Meta:
        name = "oscal-ssp-control-implementation-ASSEMBLY"

    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    set_parameter: List[OscalImplementationCommonSetParameterAssembly] = field(
        default_factory=list,
        metadata={
            "name": "set-parameter",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    implemented_requirement: List[OscalSspImplementedRequirementAssembly] = field(
        default_factory=list,
        metadata={
            "name": "implemented-requirement",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )


@dataclass
class Catalog(OscalCatalogCatalogAssembly):
    class Meta:
        name = "catalog"
        namespace = "http://csrc.nist.gov/ns/oscal/1.0"


@dataclass
class OscalAssessmentCommonRiskAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Identified Risk</ns1:b>: An identified risk.

    :ivar title:
    :ivar description:
    :ivar statement:
    :ivar prop:
    :ivar link:
    :ivar status:
    :ivar origin:
    :ivar threat_id:
    :ivar characterization:
    :ivar mitigating_factor:
    :ivar deadline:
    :ivar response:
    :ivar risk_log:
    :ivar related_observation:
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Risk Universally
        Unique Identifier</ns1:b>: A machine-oriented, globally unique
        identifier with cross-instance scope that can be used to
        reference this risk elsewhere in this or other OSCAL instances.
        The locally defined UUID of the risk can be used to reference
        the data item locally or globally (e.g., in an imported OSCAL
        instance). This UUID should be assigned per-subject, which means
        it should be consistently used to identify the same subject
        across revisions of the document.
    """
    class Meta:
        name = "oscal-assessment-common-risk-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    statement: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
        }
    )
    origin: List[OscalAssessmentCommonOriginAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    threat_id: List[OscalAssessmentCommonThreatIdField] = field(
        default_factory=list,
        metadata={
            "name": "threat-id",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    characterization: List[OscalAssessmentCommonCharacterizationAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    mitigating_factor: List["OscalAssessmentCommonRiskAssembly.MitigatingFactor"] = field(
        default_factory=list,
        metadata={
            "name": "mitigating-factor",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    deadline: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
        }
    )
    response: List[OscalAssessmentCommonResponseAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    risk_log: Optional["OscalAssessmentCommonRiskAssembly.RiskLog"] = field(
        default=None,
        metadata={
            "name": "risk-log",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    related_observation: List["OscalAssessmentCommonRiskAssembly.RelatedObservation"] = field(
        default_factory=list,
        metadata={
            "name": "related-observation",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class MitigatingFactor:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Mitigating Factor</ns1:b>: Describes an existing mitigating factor that may affect the overall determination of the risk, with an optional link to an implementation statement in the SSP.

        :ivar description:
        :ivar prop:
        :ivar link:
        :ivar subject:
        :ivar uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Mitigating
            Factor Universally Unique Identifier</ns1:b>: A machine-
            oriented, globally unique identifier with cross-instance
            scope that can be used to reference this mitigating factor
            elsewhere in this or other OSCAL instances. The locally
            defined UUID of the mitigating factor can be used to
            reference the data item locally or globally (e.g., in an
            imported OSCAL instance). This UUID should be assigned per-
            subject, which means it should be consistently used to
            identify the same subject across revisions of the document.
        :ivar implementation_uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Implementation
            UUID</ns1:b>: A machine-oriented, globally unique identifier
            with cross-instance scope that can be used to reference this
            implementation statement elsewhere in this or other OSCAL
            instancess. The locally defined UUID of the implementation
            statement can be used to reference the data item locally or
            globally (e.g., in an imported OSCAL instance). This UUID
            should be assigned per-subject, which means it should be
            consistently used to identify the same subject across
            revisions of the document.
        """
        description: Optional[MarkupMultilineDatatype] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "required": True,
            }
        )
        prop: List[OscalMetadataPropertyAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        link: List[OscalMetadataLinkAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        subject: List[OscalAssessmentCommonSubjectReferenceAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )
        implementation_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "implementation-uuid",
                "type": "Attribute",
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )

    @dataclass
    class RiskLog:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Risk Log</ns1:b>: A log of all risk-related tasks taken."""
        entry: List["OscalAssessmentCommonRiskAssembly.RiskLog.Entry"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "min_occurs": 1,
            }
        )

        @dataclass
        class Entry:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Risk Log Entry</ns1:b>: Identifies an individual risk response that occurred as part of managing an identified risk.

            :ivar title:
            :ivar description:
            :ivar start:
            :ivar end:
            :ivar prop:
            :ivar link:
            :ivar logged_by:
            :ivar status_change:
            :ivar related_response:
            :ivar remarks: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
                Additional commentary about the containing object.
            :ivar uuid: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Risk Log
                Entry Universally Unique Identifier</ns1:b>: A machine-
                oriented, globally unique identifier with cross-instance
                scope that can be used to reference this risk log entry
                elsewhere in this or other OSCAL instances. The locally
                defined UUID of the risk log entry can be used to
                reference the data item locally or globally (e.g., in an
                imported OSCAL instance). This UUID should be assigned
                per-subject, which means it should be consistently used
                to identify the same subject across revisions of the
                document.
            """
            title: Optional[MarkupLineDatatype] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            description: Optional[MarkupMultilineDatatype] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            start: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    "required": True,
                    "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
                }
            )
            end: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
                }
            )
            prop: List[OscalMetadataPropertyAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            link: List[OscalMetadataLinkAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            logged_by: List[OscalAssessmentCommonLoggedByAssembly] = field(
                default_factory=list,
                metadata={
                    "name": "logged-by",
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            status_change: Optional[str] = field(
                default=None,
                metadata={
                    "name": "status-change",
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    "white_space": "preserve",
                    "pattern": r"(\p{L}|_)(\p{L}|\p{N}|[.\-_])*",
                }
            )
            related_response: List["OscalAssessmentCommonRiskAssembly.RiskLog.Entry.RelatedResponse"] = field(
                default_factory=list,
                metadata={
                    "name": "related-response",
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            remarks: Optional["OscalAssessmentCommonRiskAssembly.RiskLog.Entry.Remarks"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            uuid: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
                }
            )

            @dataclass
            class RelatedResponse:
                """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Risk Response Reference</ns1:b>: Identifies an individual risk response that this log entry is for.

                :ivar prop:
                :ivar link:
                :ivar related_task:
                :ivar remarks: <ns1:b
                    xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
                    Additional commentary about the containing object.
                :ivar response_uuid: <ns1:b
                    xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Response
                    Universally Unique Identifier Reference</ns1:b>: A
                    machine-oriented identifier reference to a unique
                    risk response.
                """
                prop: List[OscalMetadataPropertyAssembly] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                link: List[OscalMetadataLinkAssembly] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                related_task: List[OscalAssessmentCommonRelatedTaskAssembly] = field(
                    default_factory=list,
                    metadata={
                        "name": "related-task",
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                remarks: Optional["OscalAssessmentCommonRiskAssembly.RiskLog.Entry.RelatedResponse.Remarks"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                response_uuid: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "response-uuid",
                        "type": "Attribute",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
                    }
                )

                @dataclass
                class Remarks:
                    h1: List[InlineMarkupType] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                        }
                    )
                    h2: List[InlineMarkupType] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                        }
                    )
                    h3: List[InlineMarkupType] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                        }
                    )
                    h4: List[InlineMarkupType] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                        }
                    )
                    h5: List[InlineMarkupType] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                        }
                    )
                    h6: List[InlineMarkupType] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                        }
                    )
                    ul: List[ListType] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                        }
                    )
                    ol: List[OrderedListType] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                        }
                    )
                    pre: List[PreformattedType] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                        }
                    )
                    hr: List[object] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                        }
                    )
                    blockquote: List[BlockQuoteType] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                        }
                    )
                    p: List[InlineMarkupType] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                        }
                    )
                    table: List[TableType] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                        }
                    )
                    img: List[ImageType] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                        }
                    )

            @dataclass
            class Remarks:
                h1: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h2: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h3: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h4: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h5: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h6: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                ul: List[ListType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                ol: List[OrderedListType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                pre: List[PreformattedType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                hr: List[object] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                blockquote: List[BlockQuoteType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                p: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                table: List[TableType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                img: List[ImageType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )

    @dataclass
    class RelatedObservation:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Related Observation</ns1:b>: Relates the finding to a set of referenced observations that were used to determine the finding.

        :ivar observation_uuid: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Observation
            Universally Unique Identifier Reference</ns1:b>: A machine-
            oriented identifier reference to an observation defined in
            the list of observations.
        """
        observation_uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "observation-uuid",
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
            }
        )


@dataclass
class OscalComponentDefinitionComponentDefinitionAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Component Definition</ns1:b>: A collection of component descriptions, which may optionally be grouped by capability.

    :ivar metadata:
    :ivar import_component_definition:
    :ivar component:
    :ivar capability:
    :ivar back_matter:
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Component
        Definition Universally Unique Identifier</ns1:b>: Provides a
        globally unique means to identify a given component definition
        instance.
    """
    class Meta:
        name = "oscal-component-definition-component-definition-ASSEMBLY"

    metadata: Optional[OscalMetadataMetadataAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    import_component_definition: List[OscalComponentDefinitionImportComponentDefinitionAssembly] = field(
        default_factory=list,
        metadata={
            "name": "import-component-definition",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    component: List[OscalComponentDefinitionDefinedComponentAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    capability: List[OscalComponentDefinitionCapabilityAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    back_matter: Optional[OscalMetadataBackMatterAssembly] = field(
        default=None,
        metadata={
            "name": "back-matter",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )


@dataclass
class OscalSspSystemSecurityPlanAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">System Security Plan (SSP)</ns1:b>: A system security plan, such as those described in NIST SP 800-18.

    :ivar metadata:
    :ivar import_profile:
    :ivar system_characteristics:
    :ivar system_implementation:
    :ivar control_implementation:
    :ivar back_matter:
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">System Security
        Plan Universally Unique Identifier</ns1:b>: A machine-oriented,
        globally unique identifier with cross-instance scope that can be
        used to reference this system security plan (SSP) elsewhere in
        this or other OSCAL instances. The locally defined UUID of the
        SSP can be used to reference the data item locally or globally
        (e.g., in an imported OSCAL instance).This UUID should be
        assigned per-subject, which means it should be consistently used
        to identify the same subject across revisions of the document.
    """
    class Meta:
        name = "oscal-ssp-system-security-plan-ASSEMBLY"

    metadata: Optional[OscalMetadataMetadataAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    import_profile: Optional[OscalSspImportProfileAssembly] = field(
        default=None,
        metadata={
            "name": "import-profile",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    system_characteristics: Optional[OscalSspSystemCharacteristicsAssembly] = field(
        default=None,
        metadata={
            "name": "system-characteristics",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    system_implementation: Optional[OscalSspSystemImplementationAssembly] = field(
        default=None,
        metadata={
            "name": "system-implementation",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    control_implementation: Optional[OscalSspControlImplementationAssembly] = field(
        default=None,
        metadata={
            "name": "control-implementation",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    back_matter: Optional[OscalMetadataBackMatterAssembly] = field(
        default=None,
        metadata={
            "name": "back-matter",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )


@dataclass
class Profile(OscalProfileProfileAssembly):
    class Meta:
        name = "profile"
        namespace = "http://csrc.nist.gov/ns/oscal/1.0"


@dataclass
class ComponentDefinition(OscalComponentDefinitionComponentDefinitionAssembly):
    class Meta:
        name = "component-definition"
        namespace = "http://csrc.nist.gov/ns/oscal/1.0"


@dataclass
class OscalArResultAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Result</ns1:b>: Used by the assessment results and POA&amp;M. In the assessment results, this identifies all of the assessment observations and findings, initial and residual risks, deviations, and disposition. In the POA&amp;M, this identifies initial and residual risks, deviations, and disposition.

    :ivar title:
    :ivar description:
    :ivar start:
    :ivar end:
    :ivar prop:
    :ivar link:
    :ivar local_definitions:
    :ivar reviewed_controls:
    :ivar attestation:
    :ivar assessment_log:
    :ivar observation:
    :ivar risk:
    :ivar finding:
    :ivar remarks: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
        Additional commentary about the containing object.
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Results
        Universally Unique Identifier</ns1:b>: A machine-oriented,
        globally unique identifier with cross-instance scope that can be
        used to reference this set of results in this or other OSCAL
        instances. The locally defined UUID of the assessment result can
        be used to reference the data item locally or globally (e.g., in
        an imported OSCAL instance). This UUID should be assigned per-
        subject, which means it should be consistently used to identify
        the same subject across revisions of the document.
    """
    class Meta:
        name = "oscal-ar-result-ASSEMBLY"

    title: Optional[MarkupLineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    description: Optional[MarkupMultilineDatatype] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    start: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
            "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
        }
    )
    end: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
        }
    )
    prop: List[OscalMetadataPropertyAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    link: List[OscalMetadataLinkAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    local_definitions: Optional["OscalArResultAssembly.LocalDefinitions"] = field(
        default=None,
        metadata={
            "name": "local-definitions",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    reviewed_controls: Optional[OscalAssessmentCommonReviewedControlsAssembly] = field(
        default=None,
        metadata={
            "name": "reviewed-controls",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    attestation: List["OscalArResultAssembly.Attestation"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    assessment_log: Optional["OscalArResultAssembly.AssessmentLog"] = field(
        default=None,
        metadata={
            "name": "assessment-log",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    observation: List[OscalAssessmentCommonObservationAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    risk: List[OscalAssessmentCommonRiskAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    finding: List[OscalAssessmentCommonFindingAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    remarks: Optional["OscalArResultAssembly.Remarks"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class LocalDefinitions:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Local Definitions</ns1:b>: Used to define data objects that are used in the assessment plan, that do not appear in the referenced SSP."""
        component: List[OscalImplementationCommonSystemComponentAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        inventory_item: List[OscalImplementationCommonInventoryItemAssembly] = field(
            default_factory=list,
            metadata={
                "name": "inventory-item",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        user: List[OscalImplementationCommonSystemUserAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        assessment_assets: Optional[OscalAssessmentCommonAssessmentAssetsAssembly] = field(
            default=None,
            metadata={
                "name": "assessment-assets",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        assessment_task: List[OscalAssessmentCommonTaskAssembly] = field(
            default_factory=list,
            metadata={
                "name": "assessment-task",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )

    @dataclass
    class Attestation:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Attestation Statements</ns1:b>: A set of textual statements, typically written by the assessor."""
        responsible_party: List[OscalMetadataResponsiblePartyAssembly] = field(
            default_factory=list,
            metadata={
                "name": "responsible-party",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        part: List[OscalAssessmentCommonAssessmentPartAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "min_occurs": 1,
            }
        )

    @dataclass
    class AssessmentLog:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Log</ns1:b>: A log of all assessment-related actions taken."""
        entry: List["OscalArResultAssembly.AssessmentLog.Entry"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                "min_occurs": 1,
            }
        )

        @dataclass
        class Entry:
            """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Log Entry</ns1:b>: Identifies the result of an action and/or task that occurred as part of executing an assessment plan or an assessment event that occurred in producing the assessment results.

            :ivar title:
            :ivar description:
            :ivar start:
            :ivar end:
            :ivar prop:
            :ivar link:
            :ivar logged_by:
            :ivar related_task:
            :ivar remarks: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
                Additional commentary about the containing object.
            :ivar uuid: <ns1:b
                xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment
                Log Entry Universally Unique Identifier</ns1:b>: A
                machine-oriented, globally unique identifier with cross-
                instance scope that can be used to reference an
                assessment event in this or other OSCAL instances. The
                locally defined UUID of the assessment log entry can be
                used to reference the data item locally or globally
                (e.g., in an imported OSCAL instance). This UUID should
                be assigned per-subject, which means it should be
                consistently used to identify the same subject across
                revisions of the document.
            """
            title: Optional[MarkupLineDatatype] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            description: Optional[MarkupMultilineDatatype] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            start: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    "required": True,
                    "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
                }
            )
            end: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    "pattern": r"(((2000|2400|2800|(19|2[0-9](0[48]|[2468][048]|[13579][26])))-02-29)|(((19|2[0-9])[0-9]{2})-02-(0[1-9]|1[0-9]|2[0-8]))|(((19|2[0-9])[0-9]{2})-(0[13578]|10|12)-(0[1-9]|[12][0-9]|3[01]))|(((19|2[0-9])[0-9]{2})-(0[469]|11)-(0[1-9]|[12][0-9]|30)))T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|(-((0[0-9]|1[0-2]):00|0[39]:30)|\+((0[0-9]|1[0-4]):00|(0[34569]|10):30|(0[58]|12):45)))",
                }
            )
            prop: List[OscalMetadataPropertyAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            link: List[OscalMetadataLinkAssembly] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            logged_by: List[OscalAssessmentCommonLoggedByAssembly] = field(
                default_factory=list,
                metadata={
                    "name": "logged-by",
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            related_task: List[OscalAssessmentCommonRelatedTaskAssembly] = field(
                default_factory=list,
                metadata={
                    "name": "related-task",
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            remarks: Optional["OscalArResultAssembly.AssessmentLog.Entry.Remarks"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            uuid: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
                }
            )

            @dataclass
            class Remarks:
                h1: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h2: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h3: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h4: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h5: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                h6: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                ul: List[ListType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                ol: List[OrderedListType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                pre: List[PreformattedType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                hr: List[object] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                blockquote: List[BlockQuoteType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                p: List[InlineMarkupType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                table: List[TableType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )
                img: List[ImageType] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                    }
                )

    @dataclass
    class Remarks:
        h1: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h2: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h3: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h4: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h5: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        h6: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ul: List[ListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        ol: List[OrderedListType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        pre: List[PreformattedType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        hr: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        blockquote: List[BlockQuoteType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        p: List[InlineMarkupType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        table: List[TableType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        img: List[ImageType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )


@dataclass
class OscalPoamPlanOfActionAndMilestonesAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Plan of Action and Milestones (POA&amp;M)</ns1:b>: A plan of action and milestones which identifies initial and residual risks, deviations, and disposition, such as those required by FedRAMP.

    :ivar metadata:
    :ivar import_ssp:
    :ivar system_id:
    :ivar local_definitions:
    :ivar observation:
    :ivar risk:
    :ivar finding:
    :ivar poam_item:
    :ivar back_matter:
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">POA&amp;M
        Universally Unique Identifier</ns1:b>: A machine-oriented,
        globally unique identifier with instancescope that can be used
        to reference this POA&amp;M instance in this OSCAL instance.
        This UUID should be assigned per-subject, which means it should
        be consistently used to identify the same subject across
        revisions of the document.
    """
    class Meta:
        name = "oscal-poam-plan-of-action-and-milestones-ASSEMBLY"

    metadata: Optional[OscalMetadataMetadataAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    import_ssp: Optional[OscalAssessmentCommonImportSspAssembly] = field(
        default=None,
        metadata={
            "name": "import-ssp",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    system_id: Optional[OscalImplementationCommonSystemIdField] = field(
        default=None,
        metadata={
            "name": "system-id",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    local_definitions: Optional[OscalPoamLocalDefinitionsAssembly] = field(
        default=None,
        metadata={
            "name": "local-definitions",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    observation: List[OscalAssessmentCommonObservationAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    risk: List[OscalAssessmentCommonRiskAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    finding: List[OscalAssessmentCommonFindingAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    poam_item: List[OscalPoamPoamItemAssembly] = field(
        default_factory=list,
        metadata={
            "name": "poam-item",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    back_matter: Optional[OscalMetadataBackMatterAssembly] = field(
        default=None,
        metadata={
            "name": "back-matter",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )


@dataclass
class SystemSecurityPlan(OscalSspSystemSecurityPlanAssembly):
    class Meta:
        name = "system-security-plan"
        namespace = "http://csrc.nist.gov/ns/oscal/1.0"


@dataclass
class OscalArAssessmentResultsAssembly:
    """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Security Assessment Results (SAR)</ns1:b>: Security assessment results, such as those provided by a FedRAMP assessor in the FedRAMP Security Assessment Report.

    :ivar metadata:
    :ivar import_ap:
    :ivar local_definitions:
    :ivar result:
    :ivar back_matter:
    :ivar uuid: <ns1:b
        xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Assessment Results
        Universally Unique Identifier</ns1:b>: A machine-oriented,
        globally unique identifier with cross-instance scope that can be
        used to reference this assessment results instance in this or
        other OSCAL instances. The locally defined UUID of the
        assessment result can be used to reference the data item locally
        or globally (e.g., in an imported OSCAL instance). This UUID
        should be assigned per-subject, which means it should be
        consistently used to identify the same subject across revisions
        of the document.
    """
    class Meta:
        name = "oscal-ar-assessment-results-ASSEMBLY"

    metadata: Optional[OscalMetadataMetadataAssembly] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    import_ap: Optional[OscalArImportApAssembly] = field(
        default=None,
        metadata={
            "name": "import-ap",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "required": True,
        }
    )
    local_definitions: Optional["OscalArAssessmentResultsAssembly.LocalDefinitions"] = field(
        default=None,
        metadata={
            "name": "local-definitions",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    result: List[OscalArResultAssembly] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            "min_occurs": 1,
        }
    )
    back_matter: Optional[OscalMetadataBackMatterAssembly] = field(
        default=None,
        metadata={
            "name": "back-matter",
            "type": "Element",
            "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[45][0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}",
        }
    )

    @dataclass
    class LocalDefinitions:
        """<ns1:b xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Local Definitions</ns1:b>: Used to define data objects that are used in the assessment plan, that do not appear in the referenced SSP.

        :ivar objectives_and_methods:
        :ivar activity:
        :ivar remarks: <ns1:b
            xmlns:ns1="http://csrc.nist.gov/ns/oscal/1.0">Remarks</ns1:b>:
            Additional commentary about the containing object.
        """
        objectives_and_methods: List[OscalAssessmentCommonLocalObjectiveAssembly] = field(
            default_factory=list,
            metadata={
                "name": "objectives-and-methods",
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        activity: List[OscalAssessmentCommonActivityAssembly] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )
        remarks: Optional["OscalArAssessmentResultsAssembly.LocalDefinitions.Remarks"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
            }
        )

        @dataclass
        class Remarks:
            h1: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h2: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h3: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h4: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h5: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            h6: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ul: List[ListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            ol: List[OrderedListType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            pre: List[PreformattedType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            hr: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            blockquote: List[BlockQuoteType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            p: List[InlineMarkupType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            table: List[TableType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )
            img: List[ImageType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://csrc.nist.gov/ns/oscal/1.0",
                }
            )


@dataclass
class PlanOfActionAndMilestones(OscalPoamPlanOfActionAndMilestonesAssembly):
    class Meta:
        name = "plan-of-action-and-milestones"
        namespace = "http://csrc.nist.gov/ns/oscal/1.0"


@dataclass
class AssessmentResults(OscalArAssessmentResultsAssembly):
    class Meta:
        name = "assessment-results"
        namespace = "http://csrc.nist.gov/ns/oscal/1.0"
