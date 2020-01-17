import json
import os

from bitlyshortener import Shortener
from retrying import retry

SHORTENER = Shortener(tokens=[os.getenv("BITLY_GENERIC_ACCESS_TOKEN")], max_cache_size=8192)


@retry(stop_max_attempt_number=5, wait_fixed=30000)
def retryable_shorten(url):
    return dict(id=SHORTENER.shorten_urls([url])[0])


def handler(event, context):
    shortened = retryable_shorten(event['queryStringParameters']['url'])
    result = dict(statusCode=200, body=json.dumps(shortened))
    return result
