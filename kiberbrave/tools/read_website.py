#
import pprint
import traceback
from typing import Literal
from kiberbrave.brave.kiberbrave import Kiberbrave, BRAVE_SETTINGS
from kibernikto.utils.text import get_website_as_text


async def read_website(site_url: str, key: str = "unknown"):
    print(f"\nrunning read_website for '{site_url}' with key={key}\n")

    try:
        transcript = await get_website_as_text(site_url)
        return transcript
    except Exception as e:
        print(traceback.format_exc())
        return f"ERROR: {e}"


def read_website_tool():
    return {
        "type": "function",
        "function": {
            "name": "read_website",
            "description": "You can read the websites provided by search_the_web function to obtain the answers to "
                           "user questions",
            "parameters": {
                "type": "object",
                "properties": {
                    "site_url": {
                        "type": "string",
                        "description": "website url to read",
                    }
                },
                "required": ["site_url"]
            }
        }
    }
