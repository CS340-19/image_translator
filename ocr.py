import sys
import os
import io
import json
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import translate
from google.cloud import vision
def translation(texts):

    # Instantiates a client
    translate_client = translate.Client()

    # The text to translate
    json_data = json.dumps(texts)
    # The target language
    target = 'zh-CN'

    # Translates some text into Russian
    translation = translate_client.translate(
        json_data,
        target_language=target)

    print(u'Translation: {}'.format(translation['translatedText']))

def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    string = '' 
    for text in texts:
        buf = text.description
        string = string + ' '+buf
    translation(string)

path = os.path.join(os.path.dirname(__file__),sys.argv[1])

detect_text(path)



