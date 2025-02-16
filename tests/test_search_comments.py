from pmaw import PushshiftAPI
from .config import tape, reddit
from .__mocks__.comment import ids as comment_ids


@tape.use_cassette()
def test_comment_search_limit():
    api = PushshiftAPI(file_checkpoint=1)
    comments = api.search_comments(subreddit="science", limit=100, until=1629990795)
    assert len(comments) == 100


@tape.use_cassette()
def test_comment_search_query():
    api = PushshiftAPI(file_checkpoint=1)
    comments = api.search_comments(
        q="quantum", subreddit="science", limit=100, until=1629990795
    )
    assert len(comments) == 100


@tape.use_cassette()
def test_comment_search_ids():
    api = PushshiftAPI(file_checkpoint=1)
    comments = api.search_comments(ids=comment_ids)
    assert len(comments) == len(comment_ids)


@tape.use_cassette()
def test_comment_search_mem_safe():
    api = PushshiftAPI(file_checkpoint=1)
    comments = api.search_comments(
        subreddit="science", limit=1000, mem_safe=True, until=1629990795
    )
    assert len(comments) == 1000


@tape.use_cassette()
def test_comment_praw_ids():
    api_praw = PushshiftAPI(file_checkpoint=1, praw=reddit)
    comments = api_praw.search_comments(ids=comment_ids)
    assert len(comments) == len(comment_ids)


# TODO: update cassettes to fix JSON issues
# @tape.use_cassette()
# def test_comment_praw_query():
#     api_praw = PushshiftAPI(file_checkpoint=1, praw=reddit)
#     comments = api_praw.search_comments(
#         q="quantum", subreddit="science", limit=100, until=1629990795
#     )
#     assert len(comments) == 100


# @tape.use_cassette()
# def test_comment_praw_limit():
#     api_praw = PushshiftAPI(file_checkpoint=1, praw=reddit)
#     comments = api_praw.search_comments(
#         subreddit="science", limit=100, until=1629990795
#     )
#     assert len(comments) == 100


# @tape.use_cassette()
# def test_comment_praw_mem_safe():
#     api_praw = PushshiftAPI(file_checkpoint=1, praw=reddit)
#     comments = api_praw.search_comments(
#         subreddit="science", limit=1000, mem_safe=True, until=1629990795
#     )
#     # TODO: investigate why this isnt 1000
#     assert len(comments) == 999
