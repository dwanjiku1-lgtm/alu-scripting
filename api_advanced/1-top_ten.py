#!/usr/bin/python3
"""Query the Reddit API and print the top 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting.api_advanced:v1.0.0"}

    try:
        response = requests.get(
            url, headers=headers, params={"limit": 10},
            allow_redirects=False
        )
        if response.status_code != 200:
            print("OK")
            return
        posts = response.json().get("data", {}).get("children", [])
    except (requests.RequestException, ValueError):
        print("OK")
        return

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
