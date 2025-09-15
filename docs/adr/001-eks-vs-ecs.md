
---

```markdown
# ADR-001: Choose Amazon EKS over ECS

## Status
Accepted – 2025-09-15

## Context
Need a container platform supporting polyglot microservices and advanced service-mesh features.

## Decision
Use Amazon Elastic Kubernetes Service (EKS).

## Rationale
- Broad community support and ecosystem.
- Native fit for Istio/Linkerd service mesh.
- Easier portability to other clouds.

## Consequences
+ Portable workloads, richer ecosystem.
– Slightly steeper learning curve and control-plane cost.
