from leapp.actors import Actor
from leapp.models import FlockMessage
from leapp.tags import FlockPhaseTag, FlockWorkflowTag


class ProduceFlockMessages(Actor):
    name = 'produce_flock_messages'
    description = 'No description has been provided for the produce_flock_messages actor.'
    consumes = ()
    produces = (FlockMessage,)
    tags = (FlockPhaseTag, FlockWorkflowTag)

    def process(self):
        self.produce(
            FlockMessage(message='Hello Flock 2018!'))
