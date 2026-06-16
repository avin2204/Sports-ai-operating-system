from langfuse import Langfuse


class LangfuseTracker:

    def __init__(self):

        self.client = Langfuse()

    def track(

        self,

        name,

        input_text

    ):

        self.client.trace(

            name=name,

            input=input_text
        )