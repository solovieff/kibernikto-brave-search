from datetime import datetime

from kibernikto.bots.cybernoone import Kibernikto
from kibernikto.interactors import OpenAIRoles


class Kiberwebber(Kibernikto):
    """
    Internet connected Kibernikto
    """

    def _reset(self):
        # load messages on first call
        # some reset code here: mb clear the db or history
        super()._reset()
        wai = self.full_config.who_am_i.format(self.full_config.name)
        today = datetime.now().strftime("%Y-%m-%d")
        today = f"\n[Сегодня {today}]"
        wai += today

        if self.chat_info:
            conversation_information = self._generate_chat_info()
            wai += f"\n{conversation_information}"
        # lol
        print(f"{self.__class__.__name__}: [{wai}]")
        self.about_me = dict(role=OpenAIRoles.system.value, content=f"{wai}")
