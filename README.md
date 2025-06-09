

## Overview

Write API Tests for the following cases:
1. Retrieving top stories with the Top Stories API
2. Using the Top Stories API to retrieve the current top story from the Items API
3. Using the Top Stories API to retrieve a top story, retrieve its first comment using
the Items API
4. Consider any edge cases for the above to test out

---

##  Test Coverage (Testcases)

1. test_top_stories_returns_ids 
  -Retrieving top stories with the top stories API
2. test_top_story_has_title_and_url_or_text
  -using the top stories API to retrieve the current top story from the items api
3. test_top_story_first_comment
  -using the top stories api to retrieve a top story, retrieve its first comment using the item api.
4. test_lowest_id_item
  -edge case: check json with id = 0.
5. test_max_id_item
  -edge case: check json with max id number. 
6. test_every_top_story_is_type_story
  -edge case: check for all the top stories if they have title
7. test_every_comment_top_story_has_a_comment
  -edge case check for all the top stories first comment have text. 

---

##  How to Run

###  Setup

#### Clone the repo:
   ```bash
   git clone https://github.com/briancodehub/hackernews-api-test.git
   cd hackernews-api-test

   ```
#### Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

#### Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Run Tests all tests
   ```bash
   pytest
   ```

### Run Test verbose and debugging with print statements:
   ```bash
   pytest -s -v
   ```
