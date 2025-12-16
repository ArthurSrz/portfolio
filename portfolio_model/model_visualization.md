# Arthur Sarazin Portfolio Graph Model

## Model Schema (Mermaid)

```mermaid
graph TD
%% Core Entity
Person(("Person<br/>Arthur Sarazin"))

%% First-level Categories
Experience("Experience<br/>Professional roles")
Employer("Employer<br/>Organizations")
Prototype("Prototype<br/>Data products")
Skill("Skill<br/>Competencies")
Technology("Technology<br/>Tech stack")
Education("Education<br/>Degrees")
ResearchTheme("ResearchTheme<br/>Scientific directions")
Publication("Publication<br/>Papers & articles")

%% Person to Categories
Person -->|HAS_EXPERIENCE| Experience
Person -->|BUILT| Prototype
Person -->|HAS_EDUCATION| Education
Person -->|PUBLISHED| Publication

%% Experience relationships
Experience -->|EMPLOYED_AT| Employer
Experience -->|REQUIRES_SKILL| Skill

%% Prototype relationships
Prototype -->|BUILT_DURING| Experience
Prototype -->|BUILT_FOR| Employer
Prototype -->|USES_TECHNOLOGY| Technology
Prototype -->|DEMONSTRATES_SKILL| Skill
Prototype -->|EXPLORES_THEME| ResearchTheme
Prototype -->|DERIVED_FROM| Prototype

%% Education relationships
Education -->|EDUCATED_AT| Employer

%% Publication relationships
Publication -->|ADDRESSES_THEME| ResearchTheme

%% Cross-connections (inter-entity zones)
Skill -->|RELATED_TO| Technology

%% Styling
classDef person fill:#4299e1,stroke:#2b6cb0,stroke-width:3px,color:#fff
classDef experience fill:#68d391,stroke:#38a169,stroke-width:2px
classDef employer fill:#9f7aea,stroke:#6b46c1,stroke-width:2px
classDef prototype fill:#f687b3,stroke:#d53f8c,stroke-width:2px
classDef skill fill:#38b2ac,stroke:#2c7a7b,stroke-width:2px
classDef technology fill:#48bb78,stroke:#2f855a,stroke-width:2px
classDef education fill:#805ad5,stroke:#553c9a,stroke-width:2px
classDef theme fill:#ed8936,stroke:#c05621,stroke-width:2px
classDef publication fill:#e53e3e,stroke:#c53030,stroke-width:2px

class Person person
class Experience experience
class Employer employer
class Prototype prototype
class Skill skill
class Technology technology
class Education education
class ResearchTheme theme
class Publication publication
```

## Design Constraints Applied

1. **No orphan nodes**: Every node has at least one relationship
2. **Core entity centered**: Person (Arthur Sarazin) is at the center of all queries
3. **Inter-entity zones prioritized**: Skill-Technology and Prototype-ResearchTheme connections enable discovery
4. **Space for relationships**: Graph layout designed for visual clarity
5. **End-to-end interpretability**: Navigation from Publications through ResearchThemes to Prototypes

## Instance Counts (Current Portfolio)

| Node Type | Count |
|-----------|-------|
| Person | 1 |
| Experience | 4 |
| Employer | 7 |
| Prototype | 25+ |
| Skill | 5 |
| Technology | 5 |
| Education | 2 |
| ResearchTheme | 3 |
| Publication | 3 |

## Key Traversal Patterns

### "What skills led to this prototype?"
```cypher
MATCH (p:Prototype {name: "Inside LLMs Mind"})
      -[:DEMONSTRATES_SKILL]->(s:Skill)
RETURN s.name
```

### "What research themes connect these prototypes?"
```cypher
MATCH (p1:Prototype)-[:EXPLORES_THEME]->(t:ResearchTheme)
      <-[:EXPLORES_THEME]-(p2:Prototype)
WHERE p1 <> p2
RETURN p1.name, t.name, p2.name
```

### "Show career progression through technology adoption"
```cypher
MATCH (e:Experience)-[:EMPLOYED_AT]->(emp:Employer),
      (proto:Prototype)-[:BUILT_DURING]->(e),
      (proto)-[:USES_TECHNOLOGY]->(tech:Technology)
RETURN e.title, emp.name, collect(tech.name) as technologies
ORDER BY e.startDate
```
