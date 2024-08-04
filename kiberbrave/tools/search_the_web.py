import pprint
import traceback
from typing import Literal
from kiberbrave.brave.kiberbrave import Kiberbrave


async def search_the_web(user_request: str, search_type: Literal['images', 'web', 'news'] = 'news',
                         key: str = "unknown"):
    print(f"\nrunning search_the_web for '{user_request}' and 'search_type' set to '{search_type}' with key={key}\n")

    async_brave_search = Kiberbrave(endpoint=search_type)

    query = f"{user_request}"
    num_results = 3
    try:
        if search_type == 'images':
            search_results = await async_brave_search.image(q=query, count=num_results)
        else:
            search_results = await async_brave_search.search(q=query, count=num_results)
        pprint.pprint(search_results)
        return search_results

    except Exception as e:
        print(traceback.format_exc())
        return f"ERROR: {e}"


def search_the_web_tool():
    return {
        "type": "function",
        "function": {
            "name": "search_the_web",
            "description": "Use to search the web when asked. ",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_request": {
                        "type": "string",
                        "description": "what to search for",
                    },
                    "search_type": {
                        "type": "string",
                        "description": "can be one of ['images', 'web', 'news']",
                    }
                },
                "required": ["user_request", "search_type"]
            }
        }
    }
