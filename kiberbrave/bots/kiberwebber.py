import logging
import pprint
import re
import json
from datetime import datetime
from typing import Literal

from openai._types import NOT_GIVEN
from openai.types import CompletionUsage
from pydantic_settings import BaseSettings, SettingsConfigDict

from avatar.db.chroma.knowledge_api import find_in_rag
from avatar.utils.text import stem_text, clear_text_format
from kibernikto.bots.cybernoone import Kibernikto
from kibernikto.interactors import OpenAiExecutorConfig, OpenAIRoles

from avatar.db.sqlite.logs import save_message_log
from kibernikto.telegram.telegram_bot import KiberniktoChatInfo


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
        stem_text(wai)
        print(f"{self.__class__.__name__}: [{wai}]")
        self.about_me = dict(role=OpenAIRoles.system.value, content=f"{wai}")
