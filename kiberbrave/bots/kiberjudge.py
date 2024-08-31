from typing import Literal

from openai import NOT_GIVEN

from kibernikto.bots.cybernoone import Kibernikto


class KiberJudge(Kibernikto):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Here you can add additional initialization code if needed
        self.init_routes()

    def init_routes(self):
        pass