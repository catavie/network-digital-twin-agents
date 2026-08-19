"""Google ADK Multi-Agent Suite for Autonomous Network Operations & Digital Twin."""

import os
from dotenv import load_dotenv
from google.genai import types
from google.adk.agents import LlmAgent

# Import specialized tools
from tools.spanner_graph_tools import (
    scan_streaming_telemetry,
    run_gnn_anomaly_detection,
    execute_spanner_gql_traversal,
    trace_fault_propagation_path,
)
from tools.knowledge_catalog_tools import (
    query_knowledge_catalog_slices,
    query_enterprise_sla_contracts,
)
from tools.simulation_tools import (
    create_sandboxed_spanner_twin,
    simulate_traffic_reroute,
)
from tools.sdn_execution_tools import (
    generate_intent_validation_scorecard,
    dispatch_netconf_intent,
    verify_live_telemetry_recovery,
    create_servicenow_audit_ticket,
)

load_dotenv()

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT", "default-telecom-project")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "us-central1")
MODEL = "gemini-2.5-flash"

CONFIG = types.GenerateContentConfig(
    temperature=0.1,
    max_output_tokens=2048,
)

def _load_instruction(filename: str) -> str:
    path = os.path.join(os.path.dirname(__file__), "system_instructions", filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

# ---------------------------------------------------------
# Act 1: Predictive Anomaly & Fault Detection Agent
# ---------------------------------------------------------
fault_detection_agent = LlmAgent(
    name="fault_detection_agent",
    model=MODEL,
    generate_content_config=CONFIG,
    description="Analyzes streaming spatial-temporal telemetry using GNNs to predict backhaul SLA breaches before hard alarms trigger.",
    instruction=_load_instruction("01_fault_detection_agent.txt"),
    tools=[scan_streaming_telemetry, run_gnn_anomaly_detection],
)

# ---------------------------------------------------------
# Act 2: Root Cause Analysis (RCA) Agent
# ---------------------------------------------------------
rca_agent = LlmAgent(
    name="root_cause_analysis_agent",
    model=MODEL,
    generate_content_config=CONFIG,
    description="Traverses Spanner Graph topology using in-place GQL and dependency algorithms to isolate the root cause component.",
    instruction=_load_instruction("02_root_cause_analysis_agent.txt"),
    tools=[execute_spanner_gql_traversal, trace_fault_propagation_path],
)

# ---------------------------------------------------------
# Act 3: Service Impact Analysis (SIA) Agent
# ---------------------------------------------------------
sia_agent = LlmAgent(
    name="service_impact_analysis_agent",
    model=MODEL,
    generate_content_config=CONFIG,
    description="Connects Spanner Graph topology with BigQuery Knowledge Catalog to calculate affected URLLC enterprise slices and $1.85M SLA penalties.",
    instruction=_load_instruction("03_service_impact_analysis_agent.txt"),
    tools=[query_knowledge_catalog_slices, query_enterprise_sla_contracts],
)

# ---------------------------------------------------------
# Act 4: Network Simulation & Remediation Agent
# ---------------------------------------------------------
simulation_agent = LlmAgent(
    name="network_simulation_agent",
    model=MODEL,
    generate_content_config=CONFIG,
    description="Performs 'What-If' reroute simulation in a sandboxed Spanner Digital Twin replica, proving 100% SLA recovery and zero packet loss.",
    instruction=_load_instruction("04_network_simulation_agent.txt"),
    tools=[create_sandboxed_spanner_twin, simulate_traffic_reroute],
)

# ---------------------------------------------------------
# Act 5: Governance & Closed-Loop Execution Agent
# ---------------------------------------------------------
governance_execution_agent = LlmAgent(
    name="governance_execution_agent",
    model=MODEL,
    generate_content_config=CONFIG,
    description="Provides human-in-the-loop intent validation, dispatches NETCONF SDN instructions, verifies recovery, and creates ServiceNow audit tickets.",
    instruction=_load_instruction("05_governance_execution_agent.txt"),
    tools=[
        generate_intent_validation_scorecard,
        dispatch_netconf_intent,
        verify_live_telemetry_recovery,
        create_servicenow_audit_ticket,
    ],
)

# ---------------------------------------------------------
# Master Orchestrator Agent (GEAP Cockpit)
# ---------------------------------------------------------
master_orchestrator = LlmAgent(
    name="network_digital_twin_orchestrator",
    model=MODEL,
    generate_content_config=CONFIG,
    description="Master executive orchestrator coordinating end-to-end Level 4 Autonomous Network operations across all 5 operational acts.",
    instruction=_load_instruction("orchestrator_agent.txt"),
    sub_agents=[
        fault_detection_agent,
        rca_agent,
        sia_agent,
        simulation_agent,
        governance_execution_agent,
    ],
)

root_agent = master_orchestrator
