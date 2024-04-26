from abc import ABC, abstractmethod

class IMessageRepository(ABC):
    @abstractmethod
    def save_message(self, message):
        pass

    @abstractmethod
    def get_message(self, message_id):
       pass

# Removed Cassandra imports and usage due to connection issues
# TODO: Replace with an alternative storage solution or mock

class ScyllaMessageRepository(IMessageRepository):
    def __init__(self, cluster_ips):
        # Mock implementation for demonstration
        self.messages = {}

    def save_message(self, message):
        self.messages[message.id] = message

    def get_message(self, message_id):
        return self.messages.get(message_id, None)