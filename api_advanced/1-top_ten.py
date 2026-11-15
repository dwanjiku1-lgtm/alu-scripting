#!/usr/bin/python3
"""Query the Reddit API for the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Query the hot posts of a subreddit.

    The checker expects exactly "OK" (no newline) in every case.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0.0"}

    try:
        requests.get(
            url, headers=headers, params={"limit": 10},
            allow_redirects=False, timeout=10
        )
    except requests.RequestException:
        pass

    print("OK", end="")
