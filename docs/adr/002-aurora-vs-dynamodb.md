# ADR-002: Choose Amazon Aurora over DynamoDB

## Status
Accepted – 2025-09-15

## Context
The migrated retail-analytics platform must support:
- Complex transactional queries and ad-hoc reporting
- Multi-AZ high availability
- Smooth migration from an on-prem Oracle schema
- Strict financial-grade ACID compliance

We considered **Amazon Aurora (PostgreSQL)** and **Amazon DynamoDB** as the primary data store.

## Decision
Adopt **Amazon Aurora (PostgreSQL compatible)** as the main transactional database.

## Rationale
- **SQL & Schema Compatibility**  
  Directly supports existing Oracle schema and SQL joins/aggregations.
- **ACID Transactions**  
  Full relational consistency for analytics workloads.
- **Managed Service**  
  Serverless v2 option for auto-scaling without manual capacity planning.
- **Read Scaling**  
  Reader endpoints + global database for cross-region DR.

## Alternatives
- **DynamoDB**: Great for key-value/NoSQL workloads but limited for complex joins, 
  requires heavy redesign of relational schema.
- Hybrid: Aurora for OLTP + DynamoDB for high-velocity key-value data (possible future enhancement).

## Consequences
**Pros**
- Easier migration from Oracle
- Rich analytics support
- High availability and strong consistency

**Cons**
- Higher cost per write compared to DynamoDB at extreme scale
- Needs index and query tuning to avoid unexpected cost spikes
