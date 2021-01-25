from utils.dominate import *
from utils.login import *
import dominate
from tqdm import tqdm
import time

USERNAME = ''
PASSWORD = ''
DEFAULT_COOKIE_PATH = 'insta_cookie'    # Set the name of the cookie.
TARGET = ''                             # Target of the scan.
LANGUAGES = ['it', 'en']                # Set the languages used in the posts of TARGET.

CHECK_LIKERS = False                    # Check who is the most liker of TARGET's posts.
SLEEP_BEETWEEN_POSTS = 3                # seconds.


if __name__ == '__main__':
    api = login(USERNAME, PASSWORD, DEFAULT_COOKIE_PATH)
    doc = dominate.document(title='InstaScrap_' + TARGET)
    # - - - - - - -  TARGET FEED - - - - - - -

    # Get Bio information
    bio_information = api.username_info(TARGET)
    set_up_profile_info(doc, bio_information)
    user_id = bio_information["user"]["pk"]

    # Get likers, locations, words, from posts of TARGET
    print("Get all posts of " + TARGET + "...")

    target_feed = get_all_elements(TARGET, api.username_feed)

    user_likes = dict()
    tagged_user = dict()

    locations = dict()
    geolocations = list()

    text = ""

    feed_size = len(target_feed)
    print("Starting to analyze posts...")
    for post_nr in tqdm(range(feed_size)):
        post = target_feed[post_nr]
        post_id = post["id"]

        if post["caption"] is not None:
            text += post["caption"]["text"] + " "

        # Get all the locations
        if 'location' in post:
            location = post["location"]["name"]
            if location in locations:
                locations[location] += 1
            else:
                locations[location] = 1

            if 'lat' in post['location']:
                geolocations.append(GeoLocation(post["location"]["name"],
                                                post["location"]["lat"],
                                                post["location"]["lng"]))

        if 'usertags' in post:
            users = post['usertags']['in']
            for user in users:
                username = user["user"]["username"]
                if username in tagged_user:
                    tagged_user[username] += 1
                else:
                    tagged_user[username] = 1

        if CHECK_LIKERS:
            # Get all likers of the post
            likers = api.media_likers(post_id)
            likers = likers["users"]
            for liker in likers:
                    if liker["username"] in user_likes:
                        user_likes[liker["username"]] += 1
                    else:
                        user_likes[liker["username"]] = 1

            time.sleep(SLEEP_BEETWEEN_POSTS)

    # - - - - - -  OUTPUT - - - - - - - - -
    print("\n")
    print("Generating Locations...")
    set_up_locations(doc, locations, geolocations, TARGET)

    print("Generating wordcloud...")
    set_up_word_cloud(doc, text, TARGET, LANGUAGES)

    print("Checking tags...")
    set_up_tags_inserted(doc, tagged_user, feed_size, TARGET)

    if CHECK_LIKERS:
        print("Checking Likers...")
        set_up_likes_received(doc, user_likes, feed_size)

    set_up_last_scripts(doc)
    f = open("Output/" + TARGET + ".html", "w")
    f.write(doc.render())
    f.close()
    print("Done.")
