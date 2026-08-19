# Autonomous Network Operations: Network Digital Twin Agentic Suite

## Executive Overview
This repository contains the multi-agent system designed for **Gemini Enterprise Agent Platform (GEAP)** and **Google Agent Development Kit (ADK)**, implementing an **Intent-Driven Closed-Loop Autonomous Network Operations (Level 4 Autonomy)** powered by **Cloud Spanner Graph**, **Vertex AI GNNs (Distributed Graph Flow)**, and **BigQuery / Knowledge Catalog**.

---

## The 5-Act Autonomous Operations Workflow

```mermaid
flowchart TD
    subgraph Act1["Act 1: Autonomous Monitoring & Anomaly Detection"]
        A1[Streaming Telemetry Scan] --> A2[GNN Micro-Degradation Detection]
        A2 --> A3[Predictive SLA Breach Alert: 20m Early Warning]
    end

    subgraph Act2["Act 2: Graph-Driven Root Cause Analysis"]
        A3 --> B1[Spanner Graph GQL Traversal]
        B1 --> B2[Multi-Layer Path Correlation: RAN to Core UPF]
        B2 --> B3[Isolate Optical Transponder Fault 4 Hops Upstream]
    end

    subgraph Act3["Act 3: Business & Service Impact Analysis"]
        B3 --> C1[Knowledge Catalog & BigQuery Lakehouse]
        C1 --> C2[Map Topology to BSS Tenants & URLLC Slices]
        C2 --> C3[Calculate $1.8M Financial SLA Risk]
    end

    subgraph Act4["Act 4: Digital Twin 'What-If' Simulation"]
        C3 --> D1[Clone Live Spanner Topology to Sandbox Twin]
        D1 --> D2[Simulate Traffic Shift & Optical Power Margins]
        D2 --> D3[Verify Zero Packet Loss & 100% SLA Recovery]
    end

    subgraph Act5["Act 5: Closed-Loop Governance & Execution"]
        D3 --> E1[Human-in-the-Loop Intent Validation 98.6% Conf.]
        E1 --> E2[Approve & Apply Intent]
        E2 --> E3[Dispatch NETCONF to SDN Orchestrator]
        E3 --> E4[Verify Spanner Live Recovery & Log ServiceNow Ticket]
    end
```

---

## Agent Architecture Breakdown

| Agent Name | Primary GCP Services / Tools | Core Responsibility | Key Metric / Output |
| :--- | :--- | :--- | :--- |
| **Network Supervisor & Fault Detection Agent** | Vertex AI GNN (DGF), Spanner streaming metrics | Continuous spatial-temporal telemetry scans; micro-degradation prediction | 20-minute proactive SLA breach alert |
| **Root Cause Analysis (RCA) Agent** | Cloud Spanner Graph (GQL), Multi-layer Topology Traversal | Traverses RAN, IP transport, Optical WDM, Core UPF | Isolates faulty transponder 4 hops upstream |
| **Service Impact Analysis (SIA) Agent** | BigQuery Lakehouse, Knowledge Catalog, BSS Billing | Maps physical node to enterprise customer slices (URLLC) | Assesses $1.8M penalty risk across tenants |
| **Network Simulation & Remediation Agent** | Sandboxed Spanner Digital Twin, Traffic Flow Solvers | "What-If" reroute simulation, latency & optical budget verification | 100% SLA recovery with 0% packet loss |
| **Governance & Execution Agent** | SDN Orchestrator (NETCONF), ServiceNow, Cloud Audit Logs | Explainable audit trail, human approval, closed-loop execution | <2s intent execution, MTTR hours to seconds |
| **Network Digital Twin Master Orchestrator** | GEAP Cockpit, Gemini 2.5/3.5 | Coordinates end-to-end multi-agent lifecycle and executive dashboard | Unified CNO/CTO Command Center |
