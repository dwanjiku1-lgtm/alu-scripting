#!/usr/bin/python3
"""Recursively query the Reddit API and return all hot post titles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot posts of a subreddit.

    Returns None if the subreddit is invalid or has no posts.
    """
    if after is None:
        hot_list = []  # fresh list on each top-level call

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(
            url, headers=headers, params=params,
            allow_redirects=False, timeout=10
        )
        if response.status_code != 200:
            return hot_list or None
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return hot_list or None

    for child in data.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))

    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list or None
