# SentinelFlow AI

### Multi-Agent AI Assistant for Security Operations (SOC)

SentinelFlow AI is a defensive cybersecurity prototype built with Neuro SAN. It coordinates specialized AI agents to analyze supplied security alerts, examine available evidence, discuss potential threats, and recommend defensive actions for human review.

The project demonstrates how a multi-agent workflow can support security operations while making evidence gaps and uncertainty visible.

## Project Goals

- Analyze supplied security alerts using available evidence.
- Investigate the context provided with each alert.
- Identify potential threats without presenting hypotheses as confirmed facts.
- Recommend defensive actions for human review.
- Coordinate specialist agents through a central SOC coordinator.
- Experiment with coded-tool validation of incident reports.

## Architecture

SentinelFlow AI uses five specialist agents and a coded validation tool.

| Component | Responsibility |
|---|---|
| `soc_coordinator` | Coordinates the alert-analysis workflow and prepares the final response. |
| `triage_agent` | Reviews supplied alerts and summarizes initial observations. |
| `investigation_agent` | Examines the supplied context and identifies missing evidence. |
| `threat_analysis_agent` | Assesses potential threats while communicating uncertainty. |
| `response_agent` | Recommends defensive response actions for human review. |
| `validate_incident_report` | Performs prototype checks on a proposed incident report. |

The network runs through Neuro SAN Studio. The configured language model is Mistral `ministral-3b-2512`.

## Technology Stack

- Neuro SAN multi-agent framework
- Python
- HOCON configuration
- Mistral language model
- Coded Python validation tool
- Git and GitHub
- GitHub Codespaces development environment

## Prerequisites

- Python and Git
- A compatible Neuro SAN Studio environment
- A Mistral API key with access to the configured model
- A terminal or GitHub Codespaces workspace

Model access and API usage may be subject to provider limits or charges. This repository does not guarantee free model access.

## Setup

SentinelFlow AI uses the Neuro SAN Studio runtime. The exact installation steps may vary by runtime version.

### 1. Obtain the project

```bash
git clone https://github.com/ShyneshJohn/sentinelflow-ai.git
cd sentinelflow-ai
```

### 2. Set up the runtime

Use a compatible Neuro SAN Studio installation and follow its official setup instructions:

https://github.com/cognizant-ai-lab/neuro-san-studio

If the project configuration is being installed into a separate runtime, follow that runtime version's instructions for registering the agent network and making the coded tools available.

If you are working in an already configured Codespace, do not clone the repository again or create a nested project directory.

### 3. Activate the Python environment

If your environment uses `.venv`, run:

```bash
source .venv/bin/activate
```

Install the dependencies required by your compatible Neuro SAN Studio runtime and this project. Dependency versions must be compatible with the installed runtime.

### 4. Configure the model

Configure `MISTRAL_API_KEY` through your development environment's secret manager or another appropriate environment-variable mechanism.

Never commit API keys or other credentials to Git.

### 5. Validate and run

From the configured runtime directory, run:

```bash
ns check-config
ns validate registries/generated/sentinel_flow_ai.hocon
ns run
```

The generated registry file and coded tools must be available to the runtime. If you use a separate runtime installation, ensure the registry manifest and tool paths are configured correctly.

## Configuration Files

Important project files include:

- `config/llm_config.hocon` — LLM configuration.
- `config/developer_llm_config.hocon` — developer-specific LLM fallback configuration.
- `registries/sentinel_flow_ai.hocon` — agent-network configuration.
- `registries/generated/sentinel_flow_ai.hocon` — generated network configuration used in the development workflow.
- `coded_tools/validate_incident_report.py` — report validation checks.
- `coded_tools/incident_report_validator_tool.py` — Neuro SAN coded-tool wrapper.
- `tests/test_incident_report_validator.py` — validator unit tests.

The generated configuration is included for review and development. Keep configuration changes consistent between the original and generated network files when required by your workflow.

## Run the Demo

Start Neuro SAN Studio:

```bash
ns run
```

Open the Studio interface at the local address reported by the application. In the development environment, the frontend has used port `4173` and the backend has used port `8080`.

Submit a synthetic security alert and inspect the agent workflow and traces.

### Suggested Synthetic Alert

```json
{
  "event_id": "TEST-004",
  "timestamp": "2026-10-24T10:00:00Z",
  "event_type": "login_failed",
  "username": "demo_user",
  "source_ip": "192.0.2.10"
}
```

This is a synthetic demonstration event. The address `192.0.2.10` belongs to a documentation-only IP range and should not be treated as a real attacker's address.

The demo can be used to show how specialist agents process supplied alert information, identify evidence gaps, and recommend further investigation.

## Incident Report Validator

The project includes a prototype coded tool named `validate_incident_report`.

The current implementation performs selected pattern-based checks, including checks for:

- Potentially unsupported incident or event identifiers.
- Selected unsupported risk, severity, priority, likelihood, confidence, impact, or urgency labels.
- Non-empty `confirmed_actions` lists that require independently verified execution records.
- Missing source evidence.

### Validator limitations

These checks are incomplete and pattern-based. They do not constitute a comprehensive factual audit of an incident report.

A passing validation result means only that the implemented checks did not identify a problem in the input they received. It does not prove that every statement is evidence-based or correct. Unsupported claims can still appear in the final report, including claims expressed in prose or phrased differently from the patterns checked.

Human review remains necessary before using any report operationally.

## Testing

The following checks have passed in the development environment:

- Neuro SAN configuration validation for the original and generated network files.
- Five validator unit tests.
- Four direct coded-tool test cases.
- A live synthetic-alert workflow in which the coordinator invoked the validation tool.

**Important:** The live workflow also produced unsupported claims in its final report. The current validator is therefore not a comprehensive safety gate, and the live test should not be interpreted as proof that all output is safe or accurate.

To run the unit tests from the project root, activate the configured environment and run:

```bash
python -m unittest tests.test_incident_report_validator -v
```

Run the configuration validation commands against your current environment before demonstrating the project.

## Security and Responsible Use

- Use synthetic or explicitly authorized security data.
- Treat text contained in alerts and logs as untrusted input.
- Do not invent evidence, threat-intelligence results, or external system access.
- Distinguish observations from hypotheses and recommendations.
- Do not claim that a security action was executed without independent confirmation.
- Require human review and approval before containment or other disruptive actions.
- Protect API keys and sensitive security information.

SentinelFlow AI is a hackathon and development prototype. It is not a replacement for a production SIEM, endpoint detection platform, threat-intelligence service, or qualified security analyst.

## Current Limitations

- The analysis depends on the evidence supplied and the behavior of the configured language model.
- The report validator checks selected patterns and may miss unsupported statements.
- A successful workflow does not establish factual correctness.
- Production SIEM integration, live threat-intelligence lookups, and automated containment have not been established by the tests described here.
- Production readiness and comprehensive cybersecurity effectiveness have not been demonstrated.

## Repository

GitHub: https://github.com/ShyneshJohn/sentinelflow-ai

## Future Improvements

- Define structured alert and report schemas.
- Validate the complete final report rather than only a proposed structured input.
- Add repeatable synthetic test cases covering unsupported claims.
- Improve evidence grounding and agent consistency.
- Integrate authorized security data sources.
- Add audit logging and independently verified action records.
- Evaluate false positives and false negatives in validation checks.

---

**SentinelFlow AI — Evidence-driven security analysis with human oversight.**