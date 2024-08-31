import pprint
import traceback
from typing import Literal
from kiberbrave.brave.kiberbrave import Kiberbrave, BRAVE_SETTINGS
from kiberbrave.brave.types import ImageSearchApiResponse
from kiberbrave.brave.types.web.web_search_response import WebSearchApiResponse


async def search_the_web(user_request: str, search_type: Literal['images', 'web', 'news'] = 'web',
                         key: str = "unknown"):
    print(f"\nrunning search_the_web for '{user_request}' and 'search_type' set to '{search_type}' with key={key}\n")

    async_brave_search = Kiberbrave()

    query = f"{user_request}"
    num_results = 3
    try:
        if search_type == 'images':
            search_result: ImageSearchApiResponse = await async_brave_search.image(q=query, count=num_results,
                                                                                   country=BRAVE_SETTINGS.COUNTRY,
                                                                                   search_lang=BRAVE_SETTINGS.LANGUAGE)
            if search_result.results:
                img_urls = []
                for image_result in search_result.results:
                    img_urls.append(image_result.properties.url)
                return img_urls
        elif search_type == 'web' or search_type == 'news' or search_type == 'videos':
            num_results = 13
            search_results: WebSearchApiResponse = await async_brave_search.search(
                freshness=None,
                q=query,
                count=num_results)
            cut_results = []

            for search_res in search_results.web_results:
                cut_object = {'title': search_res.get('title'),
                              'url': str(search_res.get('url')),
                              'description': search_res.get('description'),
                              'page_age': search_res.get('page_age')}
                cut_results.append(cut_object)

            for search_res in search_results.news_results:
                print("news_results\n\n")
                print(search_res)
                # cut_object = {'title': search_res.get('title'), 'url': str(search_res.get('url')),
                #              'description': search_res.get('description'),
                #              'page_age': search_res.get('page_age'), }
                # cut_results.append(cut_object)

            if search_results.discussions:
                for search_res in search_results.discussions:
                    print("discussions\n\n")
                    print(search_res)
                # cut_object = {'title': search_res.get('title'), 'url': str(search_res.get('url')),
                #              'description': search_res.get('description'),
                #              'page_age': search_res.get('page_age'), }
                # cut_results.append(cut_object)
            for search_res in search_results.video_results:
                cut_object = {'title': search_res.get('title'),
                              'url': str(search_res.get('url')),
                              # 'description': search_res.get('description'),
                              'page_age': search_res.get('page_age')}
                cut_results.append(cut_object)

            return cut_results
        elif search_type == 'videos':
            raise NotImplementedError("videos search not implemented yet")

    except Exception as e:
        print(traceback.format_exc())
        return f"ERROR: {e}"


def search_the_web_tool():
    return {
        "type": "function",
        "function": {
            "name": "search_the_web",
            "description": "Use to search the web when asked. If not asked, do not return the found links! give the "
                           "answer on user question using your younger brother if needed!",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_request": {
                        "type": "string",
                        "description": "what to search for",
                    },
                    "search_type": {
                        "type": "string",
                        "description": "can be one of ['images', 'web', 'news', 'videos']",
                    }
                },
                "required": ["user_request", "search_type"]
            }
        }
    }
