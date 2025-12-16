---
title: "Data Governance Notifier"
type: "nodes"
id: "governance-notifier"
shape: "diamond"
parent: "prototypes"
subtitle: "2024 | application"
connectionType: "solid"
weight: 20
draft: false
connections:
  - target: "veltys"
    label: "BUILT_FOR"
  - target: "tech-neo4j"
    label: "BUILT_WITH"
  - target: "tech-python"
    label: "BUILT_WITH"
  - target: "skill-knowledge-graphs"
    label: "REQUIRES"
  - target: "it-and-ai-senior-consultant"
    label: "BUILT_DURING"
---

# Automated Data Lineage Governance System

When upstream data changes, engineers working on dependent datasets are automatically notified via Google Chat within 2 minutes.

[GitHub](https://github.com/ArthurSrz/governance_notifier)

## Knowledge Graph Schema

The system persists all changes and notifications in a Neo4j knowledge graph:

| Node | Description |
|------|-------------|
| `Table` | Dataset in the lineage graph (BigQuery table or Google Sheet) |
| `Change` | Recorded modification event on a Table |
| `Engineer` | User who produces or consumes datasets |
| `Notification` | Message sent to an engineer about a data change |

| Relationship | Description |
|--------------|-------------|
| `FLOW_FROM_TO` | Data dependency between Tables (upstream → downstream) |
| `AFFECTS` | Links Change to the Table it modified |
| `TRIGGERED_NOTIFICATION` | Links Change to Notifications it generated |
| `SENT_TO` | Links Notification to recipient Engineer |

## Architecture

Multi-project architecture monitoring 4 GCP projects from a central hub:

- **Pub/Sub**: Change event ingestion from BigQuery and Google Sheets
- **Cloud Run**: Impact analyzer services (one per monitored project)
- **Neo4j Aura**: Graph database for lineage and notification persistence
- **Google Chat**: Team notification delivery

## Features

- **Impact Preview**: Preview downstream impact before committing changes
- **Operational Intelligence**: Analytics on most changed datasets, notification volume
- **Multi-project Monitoring**: Central hub coordinating 4 GCP projects

**Stack**: Python 3.11, Cloud Run, Neo4j Aura, Pub/Sub, Google Chat, BigQuery
