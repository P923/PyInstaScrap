import codecs
import re

from wordcloud import WordCloud
from stop_words import get_stop_words


def wordcloud(text, output_file, TARGET, LANGUAGES, mask=None):
    stopwords = []
    for language in LANGUAGES:
        stopwords.extend(get_stop_words(language))

    wordcloud = WordCloud(width=3000, height=2000, random_state=1, mask=mask, background_color=None, mode="RGBA",
                          colormap='Pastel1',
                          collocations=False, stopwords=stopwords).generate(text)

    wordcloud.to_file('Output/' + TARGET + "_" + output_file + ".png")


def to_json(python_object):
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                '__value__': codecs.encode(python_object, 'base64').decode()}
    raise TypeError(repr(python_object) + ' is not JSON serializable')


def from_json(json_object):
    if '__class__' in json_object and json_object['__class__'] == 'bytes':
        return codecs.decode(json_object['__value__'].encode(), 'base64')
    return json_object


def get_all_elements(target, funct):
    feed = []
    results = funct(target)
    feed.extend(results.get('items', []))

    next_max_id = results.get('next_max_id')
    while next_max_id:
        results = funct(target, max_id=next_max_id)
        feed.extend(results.get('items', []))
        next_max_id = results.get('next_max_id')
    return feed


def remove_hashtags_usernames(text):
    regex = r"(?:(?<=\s)|^)#(\w*[A-Za-z_]+\w*)"
    text = re.sub(regex, '', text)
    regex = r"(?:(?<=\s)|^)@(\w*[A-Za-z_]+\w*)"
    text = re.sub(regex, '', text)
    return text


def get_hashtags(text):
    text_output = " "
    regex = r"(?:(?<=\s)|^)#(\w*[A-Za-z_]+\w*)"
    for match in re.finditer(regex, text):
        text_output += match.group(0) + " "
    return text_output


class GeoLocation:
    def __init__(self, name, lat, lng):
        self.name = name.replace("'", " ")
        self.lng = lng
        self.lat = lat

    def print(self):
        return "[" + str(self.lng) + "," + str(self.lat) + ",'" + self.name + "'" + "]"
