import uuid


class SessionManager:

    @staticmethod
    def create_session():

        return str(
            uuid.uuid4()
        )