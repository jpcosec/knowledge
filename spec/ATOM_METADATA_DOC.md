# Atom Metadata Doc

## Purpose

Keep atoms as pure knowledge units.

Move knowledge-about-knowledge into a separate metadata space.

That includes things like:

- project context
- immediate source surface
- source kind
- grounding state
- editorial role
- scope
- phase
- bootstrap status
- migration or legacy lineage

## Rule

An atom should contain:

- its knowledge claim
- its question type
- semantic retrieval tags that describe the claim itself

An atom should not carry governance or provenance-status tags as if they were part of the claim.

## Proposed document kind

`AtomMetadataDoc`

Minimum shape:

```yaml
id: atom-metadata-registry
title: Atom metadata registry
document_kind: atom_metadata_registry
records:
  - atom_id: atom-...
    path: desk/atoms/atom-....md
    provenance_statement: Derived from `...`.
    metadata_tags:
      project:
        - project:...
      source:
        - source:...
      source_kind:
        - source_kind:...
      grounding:
        - grounding:...
      scope:
        - scope:...
      role:
        - role:...
      phase:
        - phase:...
      bootstrap:
        - bootstrap:...
      method:
        - method:...
      legacy:
        - legacy:...
```

## Current implementation

Current registry:

- `metadata/atoms/atom-metadata-registry.yaml`

Current atom-side semantic tags remain focused on claim content, such as:

- `system:*`
- `topic:*`
- `layer:*`
- `entity:*`
- `domain:*`
- `graph:*`
- `cross:*`

## Migration rule

When a tag mainly answers any of these questions, it belongs in metadata rather than in the atom:

- where did this atom come from?
- in which project was it curated?
- how grounded is it?
- what editorial/governance role does it currently play?
- what migration/bootstrap phase is it in?

## Compatibility note

The current `AtomDoc` model still carries frontmatter `provenance`.
That field remains for compatibility and traceability, but the broader governance metadata now lives in the metadata registry.
