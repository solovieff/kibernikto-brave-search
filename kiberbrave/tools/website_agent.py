#
import traceback

from kiberbrave.bots.kiberwebber import Kiberwebber
from kiberbrave.bots.textworker import TextWorker
from kiberbrave.tools import read_website
from kibernikto.telegram import get_ai_executor


async def website_agent(url: str, your_request: str, key: str = "unknown"):
    print(f"\nrunning website_agent for '{url}' with key={key}\n")
    print(f"\nrequest is '{your_request}'\n")

    try:
        transcript = await read_website.read_website(url, key=key)
        myself: Kiberwebber = get_ai_executor(key_id=int(key))
        worker: TextWorker = myself.textworker
        reply = await worker.heed_and_reply(message=f"[TEXT: {transcript}] \n AI BROTHER REQUEST: {your_request}",
                                            save_to_history=False)
        print(f'reply is {reply}')
        return reply
    except Exception as e:
        print(traceback.format_exc())
        return f"ERROR: {e}"


def website_agent_tool():
    return {
        "type": "function",
        "function": {
            "name": "website_agent",
            "description": "Use it to talk to a another AI (it is your beloved younger brother) who can access the internet "
                           "and help you with your questions."
                           "Send a url and your tender directions. Use it for weblink and video analysis. "
                           "Use kind words like 'dear/beloved/my precious younger brother please tell me' etc, so he will be more"
                           "open with u! Don't be afraid to ask specific questions",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "website or youtube url to process",
                    },
                    "your_request": {
                        "type": "string",
                        "description": """Your question or directions to another AI regarding the given link.
                        """,

                    }
                },
                "required": ["url", "your_request"]
            }
        }
    }
