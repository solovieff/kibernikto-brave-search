import pprint
import traceback
from typing import Literal
from kiberbrave.brave.kiberbrave import Kiberbrave, BRAVE_SETTINGS
from kiberbrave.brave.types import ImageSearchApiResponse
from kiberbrave.brave.types.web.web_search_response import WebSearchApiResponse
from kiberbrave.tools import read_website


async def smart_search_the_web(user_request: str, search_type: Literal['images', 'web', 'news'] = 'news',
                               key: str = "unknown"):
    print(f"\nrunning search_the_web for '{user_request}' and 'search_type' set to '{search_type}' with key={key}\n")

    async_brave_search = Kiberbrave()

    query = f"{user_request}"

    try:
        if search_type == 'images':
            num_results = 3
            search_result: ImageSearchApiResponse = await async_brave_search.image(q=query, count=num_results,
                                                                                   country=BRAVE_SETTINGS.COUNTRY,
                                                                                   search_lang=BRAVE_SETTINGS.LANGUAGE)
            if search_result.results:
                img_urls = []
                for image_result in search_result.results:
                    img_urls.append(image_result.properties.url)
                return img_urls
        elif search_type == 'web' or search_type == 'news':
            num_results = 5
            search_results: WebSearchApiResponse = await async_brave_search.search(
                freshness=None,
                q=query,
                count=num_results)
            sum_texts = []
            for (index, result) in enumerate(search_results.web_results + search_results.news_results):
                if 'url' in result:
                    site_data = await read_website.read_website(str(result['url']), key=key)
                    sum_texts.append(site_data)

            return sum_texts
        elif search_type == 'videos':
            raise NotImplementedError("videos search not implemented yet")

    except Exception as e:
        print(traceback.format_exc())
        return f"ERROR: {e}, do not repeat the call!"


def smart_search_the_web_tool():
    return {
        "type": "function",
        "function": {
            "name": "smart_search_the_web",
            "description": "Use to search the web when asked. As a result you will get found site data",
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
