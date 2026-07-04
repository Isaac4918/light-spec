from .models import Agent, IntegrationTarget

INTEGRATION_TARGETS: dict[Agent, IntegrationTarget] = {
    Agent.COPILOT: IntegrationTarget(root_dir=".github"),
    Agent.CLAUDE: IntegrationTarget(root_dir=".claude"),
    Agent.OPENCODE: IntegrationTarget(root_dir=".opencode"),
}
