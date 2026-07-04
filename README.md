# LightSpec (Versión 0.1.0)

> Un flujo de trabajo para agentes de programación centrado en backlog, specs y memoria operativa. Convierte ideas vagas o proyectos ya existentes en trabajo verificable: explorar -> formalizar -> especificar cuando haga falta -> implementar una sola feature -> validar y sincronizar.

LightSpec es agnóstico al lenguaje, framework y plataforma: sirve para cualquier proyecto de programación, no solo para proyectos de IA.

---

## ¿Por qué LightSpec?

Muchos flujos asistidos por IA saltan demasiado pronto a escribir código. LightSpec fuerza una disciplina distinta: primero define qué capacidad existe o falta, luego la registra en un backlog formal, exige spec solo cuando la feature lo necesita, y recién después implementa con evidencia explícita de cierre.

La idea central es simple: el trabajo no vive solo en prompts o en la memoria de la sesión. Vive en artefactos persistentes que cualquier agente puede retomar sin reinventar contexto.

**Frase corta**: LightSpec ordena el trabajo alrededor de `feature_list.json`, `specs/` y `memory/`, con estados de backlog explícitos y validación verificable antes de cerrar una feature.

---

## Instalacion

Instala el CLI desde una copia local del repositorio:

```bash
git clone <url-del-repositorio>
cd light-spec
uv tool install .
```

Despues de eso, el comando `lightspec` queda disponible en tu entorno de herramientas de `uv`.

## Actualizacion

Trae los cambios nuevos al repositorio local y reinstala desde esa carpeta:

```bash
git pull
uv tool install . --force
```

Puedes verificar la version instalada con:

```bash
lightspec version
```

## Uso del CLI

Crear un proyecto nuevo:

```bash
lightspec init MiProyecto
```

Instalar LightSpec en el directorio actual para un proyecto ya existente:

```bash
lightspec install
```

Instalar LightSpec en un proyecto existente especificando una ruta:

```bash
lightspec install --path /ruta/al/proyecto
```

Si falta `--agent`, el CLI preguntara interactivamente por la integración.

Si el proyecto ya contiene archivos gestionados por LightSpec y quieres sobrescribirlos, usa:

```bash
lightspec install --force
```

---

## El flujo

```text
/lightspec-init-project -> /lightspec-add-feature -> /lightspec-create-spec -> /lightspec-implement-feature
                            ^                          |
                            |                          v
               /lightspec-explore-ideas      /lightspec-validate-feature-list

/lightspec-adapt-old-project -> /lightspec-sync-docs

/lightspec-validate-standards puede ejecutarse sobre código real en cualquier momento.
```

`/lightspec-create-spec` solo aplica a features con `sdd: true`. Si una feature no requiere spec, puede pasar de `pending` a implementación directa.

| Paso | Comando | Qué hace | Produce |
|------|---------|----------|---------|
| 0 | `/lightspec-init-project` | Inicializa un proyecto nuevo y confirma arquitectura y reglas | Estructura base + `feature_list.json` vacío |
| A | `/lightspec-adapt-old-project` | Adapta un proyecto existente al flujo | Backlog, memoria y specs derivados del código real |
| 1 | `/lightspec-explore-ideas` | Aclara ideas antes de escribir backlog | Features candidatas propuestas en chat |
| 2 | `/lightspec-add-feature` | Agrega, reabre, divide o corrige features | `feature_list.json` actualizado |
| 3 | `/lightspec-create-spec` | Crea specs para features `pending` con `sdd: true` | `specs/<feature>/requirements.md`, `design.md`, `tasks.md` |
| 4 | `/lightspec-implement-feature` | Implementa exactamente una feature | Código + tests + memoria + backlog actualizado |
| 5 | `/lightspec-validate-feature-list` | Audita consistencia y prioridad del backlog | Correcciones aprobadas en `feature_list.json` |
| 6 | `/lightspec-sync-docs` | Reconciliación documental contra el código real | Backlog, memoria y docs permitidas alineadas |
| 7 | `/lightspec-validate-standards` | Revisión del código contra constitution y standards | Hallazgos y recomendaciones, sin editar código |

---

## Comandos

| Comando | Uso principal |
|---------|---------------|
| `lightspec init <ProjectName>` | Crea una carpeta nueva e instala LightSpec dentro de ella |
| `lightspec install` | Instala LightSpec en un proyecto existente |
| `lightspec version` | Muestra la version instalada del CLI |
| `/lightspec-init-project` | Inicializa un proyecto nuevo y crea el backlog base |
| `/lightspec-adapt-old-project` | Formaliza un proyecto existente dentro del flujo |
| `/lightspec-explore-ideas` | Aclara ideas antes de escribir backlog |
| `/lightspec-add-feature` | Agrega, reabre, divide o corrige features |
| `/lightspec-create-spec` | Crea specs para features con `sdd: true` |
| `/lightspec-implement-feature` | Implementa exactamente una feature |
| `/lightspec-sync-docs` | Alinea backlog, specs y memoria con el código real |
| `/lightspec-validate-feature-list` | Audita consistencia y prioridad del backlog |
| `/lightspec-validate-standards` | Revisa el código contra constitution y standards |

---

## Artefactos

| Artefacto | Rol en el flujo |
|-----------|-----------------|
| `feature_list.json` | Backlog formal y fuente de verdad del estado de cada feature |
| `memory/current.md` | Contexto operativo de la feature en curso |
| `memory/history.md` | Historial acumulado de trabajo y validaciones |
| `memory/<feature>.md` | Memoria específica por feature cuando aplica |
| `specs/<feature>/requirements.md` | Requisitos verificables |
| `specs/<feature>/design.md` | Diseño propuesto y alternativas rechazadas |
| `specs/<feature>/tasks.md` | Checklist ejecutable con validación esperada |
| `constitution.md` | Principios no negociables del proyecto |
| `code_standards.md` | Reglas de estructura, nombres, testing, seguridad y observabilidad |
| `workflow_rules.md` | Reglas compartidas del flujo y modelo de estados |

---

## Reglas clave del modelo de trabajo

- Como máximo puede existir una feature `in_progress` a la vez.
- Una feature con `sdd: true` debe pasar por `spec_ready` antes de implementación.
- Una feature bloqueada mantiene su estado principal y registra el bloqueo como metadata.
- Reabrir una feature `done` la devuelve a `pending`; no recupera `spec_ready` automáticamente.
- El cierre requiere validación explícita, no solo código escrito.
- Las decisiones que afecten arquitectura, costo, seguridad, datos u operaciones requieren aprobación humana.
- La arquitectura se sugiere al usuario por proyecto y se confirma antes de crear archivos; no está fijada en los archivos del flujo.
