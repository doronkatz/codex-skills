# Mermaid Diagram Patterns

Read this reference when choosing a diagram type or shaping Mermaid syntax from prose.

## Selection

| Source shape | Prefer | Notes |
| --- | --- | --- |
| Step-by-step process | `flowchart TD` | Use top-down when order matters. |
| System/data flow | `flowchart LR` | Use left-to-right for pipelines and service flows. |
| API or actor interaction | `sequenceDiagram` | Keep messages short and chronological. |
| Status lifecycle | `stateDiagram-v2` | Model states as nouns and transitions as events. |
| Database model | `erDiagram` | Include only relationships stated or discoverable in schema. |
| Schedule or roadmap | `gantt` | Use only when dates or durations are supplied. |
| Chronological milestones | `timeline` | Use when the text is event history rather than a project plan. |
| Concept hierarchy | `mindmap` | Use for taxonomies, not process flow. |

## Common Shapes

Flowchart:

```mermaid
flowchart LR
  source["Plain text"] --> extract["Extract entities"]
  extract --> choose["Choose diagram type"]
  choose --> insert["Insert Markdown block"]
```

Sequence:

```mermaid
sequenceDiagram
  participant User
  participant API
  participant DB as Database
  User->>API: Submit request
  API->>DB: Read data
  DB-->>API: Return rows
  API-->>User: Return response
```

State:

```mermaid
stateDiagram-v2
  [*] --> Draft
  Draft --> Review: submit
  Review --> Published: approve
  Review --> Draft: request changes
```

Entity relationship:

```mermaid
erDiagram
  CUSTOMER ||--o{ ORDER : places
  ORDER ||--|{ ORDER_ITEM : contains
  PRODUCT ||--o{ ORDER_ITEM : appears_in
```

## Labeling

- Use stable node ids such as `api`, `load_data`, or `feature_store`.
- Quote labels that contain spaces, punctuation, or parentheses: `api["Prediction API"]`.
- Keep labels short. Move details into surrounding Markdown instead of overloading nodes.
- Avoid Mermaid reserved words as ids, including `graph`, `flowchart`, `end`, `subgraph`, `class`, and `state`.
