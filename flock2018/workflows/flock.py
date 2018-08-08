from leapp.workflows import Workflow
from leapp.workflows.phases import Phase
from leapp.workflows.flags import Flags
from leapp.workflows.tagfilters import TagFilter
from leapp.workflows.policies import Policies
from leapp.tags import FlockWorkflowTag, FlockPhaseTag


class FlockWorkflow(Workflow):
    name = 'Flock'
    tag =  FlockWorkflowTag
    short_name = 'flock'
    description = '''No description has been provided for the Flock workflow.'''

    class FlockPhase(Phase):
       name = 'flock_phase'
       filter = TagFilter(FlockPhaseTag)
       policies = Policies(Policies.Errors.FailPhase,
                           Policies.Retry.Phase)
       flags = Flags()
