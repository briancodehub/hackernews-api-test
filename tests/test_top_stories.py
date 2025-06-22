import requests
import pytest


# 1 Retrieving top stories with the top stories API
def test_top_stories_returns_ids():
    """Retrieving top stories with the top stories API"""
    response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    # print("Response status:", response.status_code) # for debugging.
    assert response.status_code == 200  # check if response is success

    data = response.json()          # convert response to json
    # print("Top 5 story IDs:", data[:5])  # Show first 5 IDs for debugging
    assert isinstance(data, list)  # check the data if it is a list 
    assert len(data) > 0     # check to see list of data is empty
    assert isinstance(data[0], int)   # check to see if the first element is int. 


# 2 using the top stories API to retrieve the current top story from the items api
def test_top_story_has_title_and_url_or_text():
    """using the top stories API to retrieve the current top story from the items api"""
    response_1 = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    assert response_1.status_code == 200  # check if response is success
    top_ids = response_1.json() # convert response to json

    response_2 = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{top_ids[0]}.json")
    assert response_2.status_code == 200  # check if response is success
    story = response_2.json() 
    # print("Story:", story) # for debugging.

    assert story["type"] == "story" # check if the top item is a story.
    assert "title" in story   # check if title present
    assert "url" in story or "text" in story # story type can a url (story) or text (ask)  


# 3 using the top stories api to retrieve a top story, retrieve its first comment using the item api.
def test_top_story_first_comment():
    """using the top stories api to retrieve a top story, retrieve its first comment using the item api."""
    response_1 = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    assert response_1.status_code == 200  # check if response is success
    top_ids = response_1.json() # convert response to json

    response_2 = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{top_ids[0]}.json")
    assert response_2.status_code == 200  # check if response is success
    story = response_2.json() # convert response to json

    # print("Story:", story) # for debugging.

    if "kids" in story and story["kids"]: # check if story as comments. 
        comment_id = story["kids"][0]  # first comment id
        response_3 = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{comment_id}.json")
        assert response_3.status_code == 200  # check if response is success
        comment = response_3.json() # convert response to json

        # print("top comment:", comment) # for debugging.
        assert "text" in comment  # check if text is present.
        assert comment["type"] == "comment" # #check if type is comment

#4 edge case: check json with id = 0. 
def test_lowest_id_item():
    """edge case: check json with id = 0."""
    response = requests.get("https://hacker-news.firebaseio.com/v0/item/0.json")
    assert response.status_code == 200 # check if response is success potential bug? should this be 404 instead? 
    assert response.json() is None  # check if the data is NIL

#5 edge case: check json with max id number. 
def test_max_id_item():
    """edge case: check json with max id number."""
    response = requests.get("https://hacker-news.firebaseio.com/v0/maxitem.json")
    assert response.status_code == 200 # check if response is success  
    max_id = response.json() # convert to json
    assert isinstance(max_id, int), "maxitem is not an integer" # check to see if return int

    response_2 = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{max_id}.json")
    assert response_2.status_code == 200 # check if response is success 
    item = response_2.json()          # convert response to json
    assert "id" in item     #check if the max item has an id


#6 edge case: check for all the top stories if they have title:
def test_every_top_story_is_type_story():
    """edge case: check for all the top stories if they have title:"""
    response_1 = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    assert response_1.status_code == 200  # check if response is success
    top_ids = response_1.json() # convert response to json
    assert isinstance(top_ids, list)  # check the data if it is a list

    for id in top_ids[:10]: # Only test top 10 stories

        response_2 = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json")
        assert response_2.status_code == 200  # check if response is success
        story = response_2.json() 
        # print("Story:", story) # for debugging.

        story_type = story.get("type") # get the type 
        if story_type != "story":
            print(f"Skipping item ID {id}: type is '{story_type}'")
            continue  # Don't assert on non-story types

        assert "title" in story   # check if title present
        assert "url" in story or "text" in story # story type can have an url (story) or text (ask)  


#6.1 edge case: check for all the top stories if they have title:


# @pytest.fixture(scope="module")
# def top_story_ids():
#     response = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", timeout=5)
#     assert response.status_code == 200
#     return response.json()[:10]  # Limit to top 10 stories


# @pytest.mark.parametrize("story_id", top_story_ids)
# def test_story_details(story_id):
#     response = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json")
#     assert response.status_code == 200
#     story = response.json()
#     assert story.get("type") == "story"
#     assert "title" in story
#     assert "url" in story or "text" in story



#7 edge case check for all the top stories first comment have text. 
# Found deleted comment, but it is expected. 
def test_every_comment_top_story_has_a_comment():
    """edge case check for all the top stories first comment have text."""
    response_1 = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json")
    assert response_1.status_code == 200  # check if response is success
    top_ids = response_1.json() # convert response to json

    for id in top_ids[:10]: # Only test top 10 stories

        response_2 = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{id}.json")
        assert response_2.status_code == 200  # check if response is success
        story = response_2.json() 
        # print("Story:", story) # for debugging.

        if "kids" in story and story["kids"]: # check if story as comments. 
            comment_id = story["kids"][0]  # first comment id
            response_3 = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{comment_id}.json")
            assert response_3.status_code == 200  # check if response is success
            comment = response_3.json() # convert response to json

            # print("top comment:", comment) # for debugging.

            # Skip deleted or dead comments
            if comment.get("deleted") or comment.get("dead"):
                print(f"Skipping deleted/dead comment ID {comment_id}")
                continue

            assert "text" in comment, f"Comment ID {comment_id} missing 'text'" # check missing text
            assert comment["type"] == "comment", f"Item ID {comment_id} is not a comment" # check non-comment type 




