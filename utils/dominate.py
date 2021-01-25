import numpy as np
from dominate.tags import *

from ipywidgets import Image
from PIL import Image

from utils.utils import wordcloud, get_hashtags, remove_hashtags_usernames
'''
    Dominate methods.
    Create the html source.
'''


def set_up_profile_info(doc, infos):
    with doc.head:
        meta(charset="UTF-8")
        link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css')
        link(rel='stylesheet', href='css/style.css')

        script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js")
        script(src="http://www.openlayers.org/api/OpenLayers.js")
        script(src="https://code.jquery.com/jquery-3.5.1.js")
        script(src="https://cdn.datatables.net/1.10.23/js/jquery.dataTables.min.js")
        script(src="https://cdn.datatables.net/1.10.23/js/dataTables.bootstrap5.min.js")
        link(href="https://cdn.datatables.net/1.10.23/css/dataTables.bootstrap5.min.css")

    with doc:

        with div(cls='container'):
            with div(cls='row mt-3'):
                with div(cls='col-md-5'):
                    img(src=infos["user"]["hd_profile_pic_versions"][1]["url"],
                        cls="border border-warning img-responsive")
                with div(cls='col-md-7'):
                    with table():
                        tr(th('Infos', colspan=2))
                        tr(td('Username'), td(infos["user"]["username"]))
                        tr(td('Full Name'), td(infos["user"]["full_name"]))
                        tr(td('IsPrivate'), td(infos["user"]["is_private"]))
                        tr(td('IsVerified'), td(infos["user"]["is_verified"]))
                        tr(td('Follower'), td(infos["user"]["follower_count"]))
                        tr(td('Following'), td(infos["user"]["following_count"]))
                        tr(td('Bio'), td(infos["user"]["biography"]))
                        tr(td('External Url'), td(infos["user"]["external_url"]))

                        try:
                            tr(td('Category'), td(infos["user"]["category"]))
                            tr(td('Phone'), td(infos["user"]["contact_phone_number"]))
                            tr(td('email'), td(infos["user"]["public_email"]))
                            tr(td('Page Linked'), td(infos["user"]["page_name"] + " "))
                        except KeyError:
                            pass


def set_up_locations(doc, locations, geolocations, target):
    # Locations and Map
    locations = sorted(locations.items(), key=lambda t: t[1], reverse=True)
    with doc:
        with div(cls='row mt-3 d-flex justify-content-center pl-2'):
            with div(cls='col-md-5'):
                with table(id='tablepagination', cls='mt-3'):
                    thead(tr(th("Locations"), th("Number Tags")))

                    for location in locations:
                        tr(td(location[0]), td(location[1]))

            with div(id="div_map", cls='col-md-7'):
                div(id="DivMappa", style="width: 100%; height: 100%")
                script(src="js/" + target + "_locations.js")
                script(src="js/" + "map.js")

        locations_output = "var markers=["
        for i in range(len(geolocations)):
            locations_output += geolocations[i].print()
            if i < len(geolocations) - 1:
                locations_output += ','

        locations_output += "];"

        f = open("Output/js/" + target + "_locations.js", "w")
        f.write(locations_output)
        f.close()


def set_up_likes_received(doc, user_likes, n_post):
    with doc:
        with div(cls='row mt-3 d-flex justify-content-center pl-2'):
            with div(cls='col-md-12'):
                with table(id='tablepagination3', cls='mt-3'):
                    thead(tr(th("Username"), th("% Likes Inserted")))

                    for user in user_likes:
                        tr(td(user), td(round(user_likes[user] / n_post, 4)))


def set_up_tags_inserted(doc, tagged_users, n_post, target):
    with doc:
        with div(cls='row mt-3 d-flex justify-content-center pl-2'):
            with div(cls='col-md-12'):
                with table(id='tablepagination2', cls='mt-3'):
                    thead(tr(th("User tagged in a post of "+target), th("Absolute Frequency"), th("Relative Frequency")))

                    for user in tagged_users:
                        tr(td(user), td(tagged_users[user]), td(round(tagged_users[user] / n_post, 4)))


def set_up_word_cloud(doc, text, TARGET, LANGUAGES):
    # Generate HashTag wordcloud
    get_hashtags(text)
    mask = np.array(Image.open('utils/hashtag.jpg'))
    wordcloud(text, "HASH", TARGET, LANGUAGES, mask=mask)

    # Generate wordcloud
    text = remove_hashtags_usernames(text)
    wordcloud(text, "WORDS", TARGET, LANGUAGES)

    with doc:
        with div(cls='row mt-3 d-flex justify-content-center pl-2'):
            with div(cls='col-md-6'):
                with table(id="table_cloud"):
                    with tr():
                        th("Word Cloud")
                img(id="wrdcloud", src=TARGET + "_WORDS.png", cls="")

            with div(cls='col-md-6'):
                with table(id="table_cloud"):
                    with tr():
                        th("Tag Cloud")
                img(id="wrdcloud", src=TARGET + "_HASH.png", cls="")


def set_up_last_scripts(doc):
    with doc:
        script(src="js/pagination.js")
