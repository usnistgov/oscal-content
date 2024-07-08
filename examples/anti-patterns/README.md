# OSCAL Model-Specific Negative Examples

This directory contains the source files for examples that are valid according
to the current models but probably should not be. Validation testing, such as
in the CI pipeline, should include both positive and negative tests and flag
occurrences of negative examples reported as valid.

The contents of the anti-patterns directory are as follows:
* [recursive fields](anti-pattern-ap.json) - several assembly definitions contain
fields that are copies of themselves, leading to infinite-depth recursion. Within the
Assessment Plan model, `Assessment-part`, `Part`, and `Task` are self-referencing.
This copy of the IFA AP example contains recursive Task fields several levels deep,
and should fail validation. Assemblies should use references (foreign keys such as
UUIDs) instead of copies for fields that refer to themselves.
