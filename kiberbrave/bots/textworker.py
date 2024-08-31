from datetime import datetime

from pydantic_settings import BaseSettings, SettingsConfigDict

from kibernikto.bots import AiSettings
from kibernikto.bots.cybernoone import Kibernikto
from kibernikto.interactors import OpenAIRoles, OpenAiExecutorConfig


class TextWorkerSettings(AiSettings):
    model_config = SettingsConfigDict(env_prefix='TEXT_WORKER_')


TEXT_WORKER_SETTINGS = TextWorkerSettings()


class TextWorker(Kibernikto):
    """
    Works on link/video text and does what is said. To be used by Main Kibernikto
    """

    def __init__(self, master_id: str, username: str, config: OpenAiExecutorConfig, key: object = None):
        fact_checker_config = OpenAiExecutorConfig(model=TEXT_WORKER_SETTINGS.OPENAI_API_MODEL,
                                                   url=TEXT_WORKER_SETTINGS.OPENAI_BASE_URL,
                                                   key=TEXT_WORKER_SETTINGS.OPENAI_API_KEY,
                                                   max_tokens=TEXT_WORKER_SETTINGS.OPENAI_MAX_TOKENS,
                                                   temperature=0.1,
                                                   name=config.name,
                                                   who_am_i="Ты получаешь текст статьи или расшифровку видео и "
                                                            "указания, следуешь указаниям своего старшего брата -- "
                                                            "более умной модели! Веди себя почтительно!")
        super().__init__(config=fact_checker_config, username=username, master_id=master_id, key=key, chat_info=None,
                         add_chat_info=False, hide_errors=False)
