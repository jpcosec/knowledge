# Intervención Humana Requerida

## Decisiones Pendientes

### 1. Disposición de 18 átomos sin spec

Estos átomos existen pero no tienen spec correspondiente. ¿Qué hacemos con ellos?

| Átomo | Status sugerido |
|-------|----------------|
| `atom-boolean-algebra-and-bitwise-execution-kernel` | legacy? |
| `atom-dimensional-collapse-and-hierarchical-tensor-n-x-n-x-c-k` | legacy? |
| `atom-information-energy-e-r` | legacy? |
| `atom-pure-matrices-vs-block-matrices` | legacy? |
| `atom-meel-engine` | legacy? |
| `atom-s-expression-runtime` | legacy? |
| `atom-universal-grammar-formalization` | legacy? |
| `atom-typestate-typing` | legacy? |
| `atom-wigame-as-local-language-game` | legacy? |
| `atom-asg-projects-multiple-graphs-per-document` | ¿create spec? |
| `atom-omnirepresentacion-block-matrix-for-llm-integration` | ¿create spec? |
| `atom-grafo-indice-g-index-graph-and-collision-detection` | ¿create spec? |
| `atom-searchvector` | ¿create spec? |
| `atom-kernel-symbol-policy` | ¿create spec? |
| `atom-structural-masks-valid-sense-observed-discriminative` | ¿create spec? |
| `atom-logicalsystem-as-aggregate-root` | ¿create spec? |
| `atom-atomic-fact-c-x-d-x-v` | ¿create spec? |
| `atom-don-t-care-rule` | ¿create spec? |
| `atom-canonical-json-as-stable-interchange-format` | ¿consolidate? |

**Decisión:** ¿legacy:true + archivar, o crear specs?

---

### 2. 14 átomos de alta prioridad por crear

Los specs tienen conceptos sin átomos. ¿Priorizamos creación?

- Three-graph model como principio arquitectónico
- Separación index vs retrieval
- Fases de bootstrap (declare→extract→sample→backfill)
- Vocabulario de grounding maturity
- Los 12 namespaces de tags como átomos individuales
- Stable id ≠ location ≠ title
- Proposición debe bajar a ground
- Asimetría Text→Relaciones
- Principio "no orphan atoms"

**Decisión:** ¿Cuáles creamos primero?

---

### 3. Cobertura de NAMESPACE_TREE

100+ namespaces definidos en spec pero solo ~5% tienen átomos.

Opciones:
- Crear átomo por namespace (tarea enorme)
- Crear un átomo genérico "namespace X define Y"
- Dejar los namespaces solo en spec, no atomizar

**Decisión:** ¿Cómo manejamos los namespaces a nivel de átomos?

---

### 4. Vacío: THE_KNOWLEDGE_DATABASE.md

 acabas de escribirlo. Los conceptos centrales (entities indexed, relations registered, S_i, V_i, facets) no tienen átomos correspondientes.

**Decisión:** ¿Creamos átomos que capturen estos principios del nuevo spec?
