from leapp.actors import Actor
from leapp.models import FlockMessage
from leapp.tags import FlockPhaseTag, FlockWorkflowTag


class FlockMessagePrinter(Actor):
    name = 'flock_message_printer'
    description = 'No description has been provided for the flock_message_printer actor.'
    consumes = (FlockMessage,)
    produces = ()
    tags = (FlockPhaseTag, FlockWorkflowTag)

    def process(self):
        for message in self.consume(FlockMessage):
            print('FlockMessage: ' + message.message)
