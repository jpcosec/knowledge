# KB

Subproyecto de sistema de manejo de conocimiento dentro del workspace del laboratorio.

## Qué vive aquí

- `spec/` — especificaciones, arquitectura y notas de diseño del sistema KB.
- `desk/` — capa operativa local usada para bootstrap y authoring del proyecto KB.
- `.sldb/` — store e índices SLDB del subproyecto KB.
- `scripts/` — utilidades del proyecto KB.

## Relación con el workspace raíz

La raíz de este repo contiene varios trabajos distintos del laboratorio.
`kb/` agrupa únicamente los artefactos que pertenecen al sistema de manejo de conocimiento.

## Convención práctica

Si trabajas específicamente en este subproyecto, usa `kb/` como raíz operativa:

```bash
cd kb
```

Desde ahí, rutas como `desk/`, `.sldb/` y `spec/` vuelven a ser locales al proyecto KB.
