import json
import os
import arabic_reshaper

from wordcloud import WordCloud
from bidi.algorithm import get_display


def parse_events():
    with open('events-1396.json') as data_file:
        data = json.load(data_file)

    for row in data:
        for item in row:
            print(item['title'], file=open('events-title.txt', 'a'))

    result_text = open('events-title.txt').read()
    return result_text


if os.stat('events-title.txt').st_size == 0:
    text = parse_events()
else:
    text = open('events-title.txt').read()
reshaped_text = arabic_reshaper.reshape(text)
bidi_text = get_display(reshaped_text)

stop_list = ['روز']
stop_words = set(
    [
        get_display(arabic_reshaper.reshape(x)) for x in stop_list
    ]
)

wordcloud = WordCloud(
    font_path='Vazir-Light.ttf',
    max_words=5000000,
    stopwords=stop_words,
    margin=0,
    width=800,
    height=800,
    min_font_size=1,
    max_font_size=500,
    background_color="black",
    random_state=0
).generate(bidi_text)

image = wordcloud.to_image()
image.show()
image.save('wordcloud.png')
