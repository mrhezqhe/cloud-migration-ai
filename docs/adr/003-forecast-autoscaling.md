
---

# ADR-003: Introduce AI-Driven Forecast Service for Autoscaling

## Status
Accepted – 2025-09-15

## Context
Current HPA reacts to CPU usage, causing 2–5 minute lag during flash sales.
Goal: proactively scale EKS nodes to avoid latency spikes.

## Decision
Deploy a lightweight FastAPI microservice running a Prophet time-series model.
It consumes CloudWatch metrics, predicts one hour ahead, and publishes desired
replica count to the HPA via a custom metrics API.

## Rationale
- Simple to prototype in Python
- No training pipeline needed; Prophet handles seasonality well
- Works with managed AWS services, minimizing Ops overhead

## Consequences
+ Lower 95th-percentile latency by proactive scaling
+ Demonstrates MLOps integration
– Requires model drift monitoring and key rotation for CloudWatch access
