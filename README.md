# SentinelFlow AI
### Multi-Agent AI Assistant for Security Operations (SOC)

SentinelFlow AI is a defensive cybersecurity prototype built with Neuro SAN. It uses specialized AI agents to help analyze security alerts, investigate supplied evidence, summarize potential threats, and recommend response actions for human review.

## Project Overview

Security operations teams need to review alerts, prioritize potential threats, investigate evidence, and determine appropriate responses. SentinelFlow AI demonstrates how a multi-agent architecture can help organize these tasks into a structured workflow.

**Core goals**
- Triage security alerts using supplied evidence.
- Investigate the context of an alert.
- Analyze potential threats and communicate uncertainty.
- Recommend defensive actions for human review.
- Coordinate specialist agents through a central SOC coordinator.

## Architecture

The project uses five agents:

| Agent | Responsibility |
|---|---|
| `soc_coordinator` | Coordinates the alert-analysis workflow. |
| `triage_agent` | Reviews and prioritizes supplied alerts. |
| `investigation_agent` | Examines the provided context and evidence. |
| `threat_analysis_agent` | Assesses potential threats and uncertainty. |
| `response_agent` | Recommends defensive response actions. |

The agents are coordinated through a Neuro SAN agent network. The configured language model is Mistral `ministral-3b-2512`.

## Technology Stack

- Neuro SAN multi-agent framework
- Python virtual environment
- HOCON configuration
- Mistral language model
- Git and GitHub

## Prerequisites

- Python and Git, as required by the Neuro SAN Studio installation
- A working Neuro SAN Studio environment
- A Mistral API key and access to the selected model
- A terminal or GitHub Codespaces workspace

## Setup

SentinelFlow AI is an agent-network configuration for the Neuro SAN Studio runtime; this repository does not include the complete runtime.

### 1. Obtain the runtime

Clone the official [Neuro SAN Studio repository](https://github.com/cognizant-ai-lab/neuro-san-studio) and follow its installation instructions.

### 2. Obtain SentinelFlow AI

Clone this repository separately:

```bash
git clone https://github.com/ShyneshJohn/sentinelflow-ai.git
```

### 3. Install the project configuration

Copy the SentinelFlow AI network file into the runtime's `registries/generated/` directory and copy the supplied LLM configuration files into the runtime's `config/` directory.

Check the runtime's registry manifest and register the SentinelFlow AI network if it is not already listed.

### 4. Configure the model

Configure `MISTRAL_API_KEY` using your development environment's secret manager. Use a valid key with access to the configured model. Never commit credentials to Git.

### 5. Validate and run

From the Neuro SAN Studio runtime directory, activate its installed Python virtual environment and run:

```bash
ns check-config
ns validate registries/generated/sentinel_flow_ai.hocon
ns run
```

Run these commands only after the runtime and model credentials have been configured successfully.

## Configuration

The project uses these configuration files:

- `config/llm_config.hocon` — LLM configuration loaded by the Studio.
- `config/developer_llm_config.hocon` — developer-specific LLM fallback configuration.
- `registries/generated/sentinel_flow_ai.hocon` — SentinelFlow AI agent network.

The generated agent network is included in this repository so the project configuration can be reviewed alongside the code.

## Validate the Configuration

Activate the virtual environment and run:

```bash
source venv/bin/activate
ns check-config
ns validate registries/generated/sentinel_flow_ai.hocon
```

Both commands should pass before running the demo.

## Run the Demo

Start Neuro SAN Studio using the launch instructions for the installed version:

```bash
ns run
```

Open the Studio interface at the local address reported by the application. In the configured Studio environment, the frontend commonly runs on port `4173` and the backend on port `8080`.

Submit a synthetic security alert and inspect the resulting workflow and agent traces.

### Suggested Demo Scenario

Use a clearly labeled synthetic alert, such as:

> Multiple failed login attempts were reported for a test account. No source IP, event count, geolocation, or additional logs have been supplied. Analyze only the available information, state what remains unknown, and recommend safe investigation steps.

Show how the coordinator and specialist agents process the alert. Highlight evidence-based analysis, uncertainty, and recommended next steps.

## Security and Responsible Use

- Use synthetic or explicitly authorized security data for demonstrations.
- Treat text contained in logs and alerts as untrusted input.
- Do not invent evidence, threat-intelligence results, or external system access.
- Clearly distinguish observations from hypotheses.
- Do not execute containment or remediation actions automatically.
- Require human review and approval before operational response actions.
- Protect API keys and sensitive security information.

SentinelFlow AI is a prototype. Its outputs require validation by a qualified human reviewer before being used in a real security operations environment.

## Current Validation

The project configuration and Mistral model were successfully validated in the development environment during development. Re-run the validation commands above against the latest checkout to confirm your own environment is working.

## Limitations

The prototype's analysis depends on the evidence supplied to it and the behavior of the configured language model. It should not be treated as a replacement for a production SIEM, endpoint detection platform, threat-intelligence service, or human security analyst.

## Repository

GitHub: https://github.com/ShyneshJohn/sentinelflow-ai

## Future Improvements

- Add structured alert input and output schemas.
- Add repeatable synthetic test cases.
- Evaluate agent consistency and evidence grounding.
- Integrate authorized security data sources.
- Add audit logging and stronger validation of recommended actions.

---

**SentinelFlow AI — Evidence-driven security analysis with human oversight.**
