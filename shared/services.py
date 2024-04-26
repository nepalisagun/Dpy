from shared.models import Message

from shared.repositories import IMessageRepository

class MessageService:
    def __init__(self, repository: IMessageRepository):
        self.repository = repository

    def create_message(self, content, user_id, channel_id):
        # Assuming Message is a dataclass with id auto-generated (e.g., UUID)
        from uuid import uuid4
        from datetime import datetime
        message = Message(id=uuid4(), user_id=user_id, channel_id=channel_id, content=content, timestamp=datetime.utcnow())
        self.repository.save_message(message)
        return message

    def fetch_message(self, message_id):
        return self.repository.get_message(message_id)
