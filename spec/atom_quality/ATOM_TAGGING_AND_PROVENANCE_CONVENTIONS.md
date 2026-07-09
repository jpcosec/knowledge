# Atom Tagging and Provenance Conventions

## Estado

Borrador operativo.

## Propósito

Reducir ambigüedad en dos áreas donde la calidad de los átomos suele variar más de la cuenta:

- cómo asignar tags de forma consistente
- cómo declarar `provenance` en frontmatter con suficiente claridad y honestidad

Este documento complementa:

- `ATOM_QUALITY_CHECKLIST.md`
- `ATOM_AUTHORING_STANDARD.md`
- `ATOM_AUTHORING_PROCEDURE.md`
- `ATOM_REVIEW_ROUTINE.md`

---

## 1. Principio general

Los tags del átomo y la procedencia cumplen funciones distintas.

- los **tags del átomo** sirven para recuperación semántica de la afirmación
- la **procedencia** sirve para declarar de dónde sale la afirmación
- la **metadata del átomo** sirve para gobernanza, grounding, contexto de proyecto y estado editorial

No deben confundirse.

- Un tag no reemplaza una explicación de procedencia.
- Una procedencia narrativa no reemplaza tags útiles de recuperación.
- La metadata sobre el átomo no debe vivir mezclada con la semántica del átomo.

Ver `spec/ATOM_METADATA_DOC.md`.

---

## 2. Convención general de tags

### 2.1 Qué deben hacer los tags

Los tags deben ayudar a responder preguntas como:

- ¿de qué sistema o proyecto habla este átomo?
- ¿qué tema principal toca?
- ¿qué capa o entidad afecta?
- ¿qué rol semántico cumple?
- ¿qué nivel de grounding o procedencia tiene?

### 2.2 Qué no deben hacer los tags

Los tags no deben cargar por sí solos con:

- toda la semántica profunda del átomo
- distinciones conceptuales críticas que el answer debería explicitar
- relaciones completas entre entidades
- la justificación principal de la tesis

---

## 3. Mínimo obligatorio de tags

Todo átomo nuevo o refinado debe tener como mínimo:

- un tag de sistema
- al menos un tag de tema

Plantilla mínima:

```yaml
tags:
  - system:...
  - topic:...
```

Los campos como `project:*`, `source:*`, `source_kind:*`, `grounding:*`, `scope:*`, `role:*`, `phase:*` y `bootstrap:*` deben vivir en metadata separada del átomo.

---

## 4. Familias de tags recomendadas

### 4.1 Sistema

Identifica el sistema principal al que pertenece la afirmación.

Ejemplos:

- `system:kb`
- `system:sldb`
- `system:deskops`
- `system:kgdb`
- `system:marcado`
- `system:ontomap`

### 4.2 Proyecto, fuente y grounding

`project:*`, `source:*`, `source_kind:*`, `grounding:*` y namespaces equivalentes ya no deberían vivir en tags del átomo.

Ahora pertenecen al espacio de metadata del átomo, porque describen el contexto, origen o madurez evidencial del conocimiento, no la afirmación de conocimiento misma.

### 4.5 Tema

Nombra el tema principal de recuperación.

Ejemplos:

- `topic:provenance`
- `topic:anchoring`
- `topic:taxonomy`
- `topic:concept_graph`
- `topic:query`
- `topic:sample`
- `topic:migration`

Puede haber más de un `topic:*`, pero conviene que uno sea claramente dominante.

### 4.6 Scope, role y phase

`scope:*`, `role:*`, `phase:*`, `bootstrap:*`, `status:*`, `method:*` y `legacy:*` se tratan mejor como metadata del átomo cuando describen su función editorial, fase de migración o contexto de curación.

No deberían formar parte del núcleo semántico del átomo salvo que en el futuro exista una justificación explícita para volverlos semántica canónica.

---

## 5. Familias de tags opcionales frecuentes

Según el caso, también pueden usarse:

### Layer

- `layer:source`
- `layer:sample`
- `layer:atom`
- `layer:composition`
- `layer:workflow`
- `layer:graph_provenance`
- `layer:graph_concept`
- `layer:graph_structure`

### Entity

- `entity:source`
- `entity:sample`
- `entity:atom`
- `entity:composition`
- `entity:anchor`
- `entity:concept`
- `entity:taxonomy_node`
- `entity:tag_facet`

### Graph

- `graph:provenance`
- `graph:concept`
- `graph:structure`

### Method

- `method:anchor_modeling`
- `method:provenance_analysis`
- `method:concept_modeling`
- `method:view_generation`
- `method:bootstrap_ingestion`

### Bootstrap / phase / cross

- `bootstrap:...`
- `phase:...`
- `cross:...`
- `provenance:...`

Usarlos solo cuando agregan valor real de recuperación o gobernanza.

---

## 6. Regla para elegir `source:`

Esta es una de las zonas más ambiguas y conviene normalizarla.

### 6.1 Regla base

`source:` debe nombrar la **fuente principal inmediata** desde la que se redactó el átomo.

### 6.2 Si el átomo depende sobre todo de una fuente

Usar un `source:` específico.

Ejemplo:

- `source:spec/KB_SYSTEM_SPEC.md`

### 6.3 Si el átomo es síntesis de varias specs del mismo conjunto

Usar una fuente agrupadora simple y dejar el detalle en `provenance`.

Ejemplo:

- `source:kb_spec_docs`

### 6.4 Si el átomo es cruce entre proyectos o documentos heterogéneos

Usar una etiqueta agrupadora clara.

Ejemplos:

- `source:cross_project_docs`
- `source:legacy_and_kb_specs`

### 6.5 Regla práctica

No usar varios `source:*` salvo que realmente aporten recuperación útil. En general:

- **un `source:` principal**
- **el detalle fino en `provenance`**

---

## 7. Convención de `source_kind:`

`source_kind:` no describe el tema del átomo; describe el tipo de fuente usada.

### Casos frecuentes

- `source_kind:spec` → una spec puntual del proyecto actual
- `source_kind:generated_spec` → una spec sintetizada o producida como artefacto de diseño
- `source_kind:legacy_doc` → documentación de sistemas previos
- `source_kind:cross_project_doc` → documentación externa o de otros proyectos usada para síntesis
- `source_kind:sample` → cuando el átomo ya está fundado directamente en samples

---

## 8. Convención general de procedencia

Todo átomo debe tener un campo de frontmatter:

```yaml
provenance: ...
```

Su trabajo es responder con honestidad:

- de dónde salió esta afirmación
- si es derivación simple o síntesis
- qué tipo de grounding representa hoy

---

## 9. Formatos canónicos de `provenance`

### 9.1 Procedencia simple desde una sola fuente

Usar cuando la afirmación proviene principalmente de un documento concreto.

```yaml
provenance: Derived from `spec/KB_SYSTEM_SPEC.md`.
```

### 9.2 Procedencia de síntesis entre varias fuentes del mismo proyecto

```yaml
provenance: Derived from `spec/GRAPH_ARCHITECTURE.md` and `spec/ATOM_CONCEPT_GRAPH.md` as a synthesis.
```

### 9.3 Procedencia de cruce entre proyecto actual y legado

```yaml
provenance: Derived from `spec/MULTI_SOURCE_ANCHORING.md` and legacy ecosystem documentation as a synthesis.
```

### 9.4 Procedencia con aclaración epistémica

Usar cuando conviene explicitar que todavía no hay grounding fuerte.

```yaml
provenance: Derived from `spec/BOOTSTRAP_KB_WITH_CURRENT_DESKOPS.md` as a bootstrap synthesis. This atom is currently spec-derived rather than sample-validated.
```

---

## 10. Vocabulario recomendado para honestidad epistemológica

Cuando haga falta, usar wording explícito como:

- `Derived from ...`
- `Derived from ... as a synthesis`
- `Currently spec-derived rather than sample-validated`
- `Inferred from ...`
- `Backed by current project specs, pending sample-level grounding`

Evitar fórmulas que sugieran más certeza de la disponible.

No decir implícitamente que un átomo está validado si en realidad solo está:

- inferido desde specs
- sintetizado desde docs
- pendiente de samples

---

## 11. Relación entre `grounding:*` y `provenance`

Conviene que ambos sean coherentes.

Ejemplos:

- si `grounding:derived`, la procedencia debería sonar a derivación documental
- si `grounding:cross_inferred`, la procedencia debería mencionar síntesis o inferencia entre fuentes
- si `grounding:sample_linked`, la procedencia debería poder nombrar samples o soporte directo
- si `grounding:validated`, la procedencia no debería sonar meramente especulativa

---

## 12. Anti-patrones frecuentes

### En tags

- `tags: []`
- tags demasiado genéricos que no recuperan nada útil
- demasiados tags casi equivalentes
- esconder una relación estructural importante solo en un tag

### En procedencia

- no tener `provenance` en frontmatter
- decir solo “derived from docs” sin nombrar cuáles
- mezclar procedencia con justificación conceptual larga
- exagerar validación o grounding

---

## 13. Regla de cierre práctica

Antes de cerrar un átomo, verificar:

- ¿los tags mínimos están presentes?
- ¿`source:` nombra la fuente principal inmediata o una agrupación justificada?
- ¿`source_kind:` describe bien el tipo de fuente?
- ¿`role:` está claro?
- ¿`grounding:` es honesto?
- ¿`provenance` nombra explícitamente las fuentes y el tipo de derivación?

Si alguna de estas respuestas es no, el átomo todavía necesita refinamiento.
