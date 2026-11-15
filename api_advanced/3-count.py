#!/usr/bin/python3
"""Recursively count keywords in the hot post titles of a subreddit."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keywords found in hot post titles.

    Prints nothing if the subreddit is invalid or nothing matches.
    """
    if counts is None:
        counts = {}

    # Duplicate keywords (case-insensitive) add up, so count each one's multiplicity
    multiplicity = {}
    for word in word_list:
        key = word.lower()
        multiplicity[key] = multiplicity.get(key, 0) + 1

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
            return _print_counts(counts)
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return _print_counts(counts)

    for child in data.get("children", []):
        title = child.get("data", {}).get("title") or ""
        for token in title.lower().split():
            if token in multiplicity:
                counts[token] = counts.get(token, 0) + multiplicity[token]

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, after, counts)

    return _print_counts(counts)


def _print_counts(counts):
    """Print counts by descending count, then alphabetically."""
    for word, number in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, number))
