# Frontend Agent Guidelines — Physio Story

Guidelines for the Cursor agent and contributors working in the **frontend** package only. Follow these rules unless the user explicitly requests otherwise.

> **Scope:** This document applies exclusively to files under `frontend/`. Backend (`backend/`) and infrastructure rules are out of scope here.

## Code language (mandatory)

**All generated code must be written in English.**

This includes:

- File and folder names
- Classes, functions, variables, and constants
- Source code comments
- Technical error messages and logs
- API-related names on the client (props, payloads, route names)
- Commit messages for frontend changes

**Exception:** User-facing UI copy (labels, buttons, validation messages shown on screen) may be in **Spanish** when the product requires it.

| Wrong | Correct |
|-------|---------|
| `pacienteService` | `patientService` |
| `obtenerListaPacientes` | `fetchPatientList` |
| `// validar documento` | `// validate document number` |

## Stack

- **Vue 3** (Composition API), **Vite**, **JavaScript** (ES modules)
- Path alias: `@/` → `src/` (see `vite.config.js`)

## Clean architecture

Organize `src/` in layers. Dependencies point **inward** (UI → application → domain; infrastructure implements ports from application/domain).

```
src/
├── domain/           # Entities, value objects, domain errors (no Vue, no HTTP)
├── application/      # Use cases, ports (interfaces), DTOs
├── infrastructure/   # HTTP clients, mappers, storage adapters
├── presentation/     # Vue components, composables, views, router
│   ├── components/   # Presentational / dumb components
│   ├── views/        # Route-level pages
│   └── composables/  # UI logic wired to use cases
└── shared/           # Cross-cutting utilities (constants, helpers without business rules)
```

### Layer rules

| Layer | May depend on | Must not depend on |
|-------|---------------|-------------------|
| `domain` | nothing external | Vue, Axios/fetch, browser APIs |
| `application` | `domain` | Vue components, HTTP libraries |
| `infrastructure` | `application`, `domain` | Vue components |
| `presentation` | `application`, `domain`, `shared` | Concrete HTTP details inside components |

- **Use cases** orchestrate one user action (e.g. `LoadPatientList`, `CreateEvolution`). Inject dependencies via constructor or factory (ports), not global singletons.
- **Components** stay thin: bind UI state, call composables/use cases, render. No raw `fetch` in `.vue` files.
- **Mappers** convert API JSON ↔ domain entities in `infrastructure`, not in views.

Create this structure incrementally as features grow; do not put all logic in `App.vue` or a flat `components/` folder.

## SOLID principles

1. **Single Responsibility** — One component = one visual concern. One composable = one cohesive behavior.
2. **Open/Closed** — Extend via composition (composables, strategies), not long `if/else` chains in stable components.
3. **Liskov Substitution** — Port implementations (e.g. `PatientRepository`) must be interchangeable without breaking use cases.
4. **Interface Segregation** — Small ports (`findById`, `save`), not one god-object API service.
5. **Dependency Inversion** — Presentation and application depend on abstractions, not `axios` or `fetch` directly.

## Object-oriented design

Use OOP when it clarifies domain rules: **classes** for entities and value objects; **functions or class-based use cases** for application logic.

```javascript
// domain/Patient.js
export class Patient {
  constructor({ id, documentNumber, fullName }) {
    this.id = id
    this.documentNumber = documentNumber
    this.fullName = fullName
  }

  static create(props) {
    if (!props.documentNumber?.trim()) {
      throw new Error('Document number is required')
    }
    return new Patient(props)
  }
}
```

```javascript
// application/ports/PatientRepository.js
export class PatientRepository {
  async findById(_id) {
    throw new Error('Not implemented')
  }
}
```

- Encapsulate validation and invariants in domain types.
- Avoid anemic models: domain behavior lives in `domain/`, not scattered in components.
- Prefer **composition** (composables injecting use cases) over deep inheritance.

## Vue 3 conventions

- Use **`<script setup>`** and Composition API for new components.
- **Presentational components:** `props` in, `defineEmits` out; no direct API calls.
- **Container / view components:** wire composables to the template.
- **PascalCase** for component files (`PatientCard.vue`); **camelCase** for composables (`usePatientList.js`).
- Use **scoped** styles unless global tokens live in `assets/`.
- Register routes in `presentation/router` when routing is added.

## API integration

- Development backend base URL: `http://localhost:8000`. Centralize in `infrastructure/config/apiConfig.js`.
- One low-level HTTP adapter (e.g. `HttpClient`); resource repositories implement application ports.
- Handle errors in infrastructure; map to domain/application errors; show user-friendly messages in presentation.

## Code quality

- No dead code or commented-out blocks in commits.
- No magic strings — use `shared/constants/`.
- Prefer immutable state updates when practical.
- Keep functions small and pure where possible; side effects at the edges (composables, infrastructure).
- Run `npm run build` before considering a feature complete.

## Testing (when added)

- Unit-test **domain** and **application** without mounting Vue.
- Component tests in presentation; mock ports, not the real API.
- Names: `*.spec.js` or `*.test.js`, colocated or under `tests/` mirroring `src/`.

## Avoid

- Business logic in templates or oversized `<script setup>` without extraction.
- Spanish identifiers in code.
- God components (> ~200 lines without splitting).
- Circular imports between layers.
- Coupling frontend code to Adminer, MySQL, or Docker.

## Reference flow for a new feature

Example: list patients

1. `domain/Patient.js` — entity  
2. `application/ports/PatientRepository.js` — port  
3. `application/useCases/ListPatients.js` — use case  
4. `infrastructure/http/PatientApiRepository.js` — adapter  
5. `presentation/composables/usePatientList.js` — wires use case to UI  
6. `presentation/views/PatientListView.vue` — page  
7. `presentation/components/PatientRow.vue` — presentational row  

Follow this flow for new features unless the user specifies otherwise.
