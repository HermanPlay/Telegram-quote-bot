import asyncio
from TikTokApi import TikTokApi
import asyncio


def download():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        with TikTokApi() as api:
            video_bytes = api.video(id='7117580418974567685').bytes()
            return video_bytes
    except RuntimeError as ex:
        if "There is no current event loop in thread" in str(ex):
            return ex
    finally:
        with TikTokApi() as api:
            video_bytes = api.video(id='7117580418974567685').bytes()
            return video_bytes
    