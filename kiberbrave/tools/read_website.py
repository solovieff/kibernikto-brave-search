#
import traceback

from kibernikto.plugins._youtube_summarizator import _is_youtube_url, _get_video_details, _get_video_transcript
from kibernikto.utils.text import get_website_as_text


async def read_website(url: str, key: str = "unknown"):
    print(f"\nrunning read_website for '{url}' with key={key}\n")

    try:
        if _is_youtube_url(url):
            info, video, text = _get_video_details(url)

            if video is None:
                return None

            transcript = _get_video_transcript(video.video_id)
        else:
            transcript = await get_website_as_text(url)
        return transcript
    except Exception as e:
        print(traceback.format_exc())
        return f"ERROR: {e}"


def read_website_tool():
    return {
        "type": "function",
        "function": {
            "name": "read_website",
            "description": "Use to read the websites and videos provided to obtain the answers to "
                           "user questions",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "website url to read",
                    }
                },
                "required": ["url"]
            }
        }
    }
