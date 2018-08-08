from leapp.models import Model, fields
from leapp.topics import FlockDemoTopic


class FlockMessage(Model):
    topic = FlockDemoTopic
    message = fields.String(required=True)
