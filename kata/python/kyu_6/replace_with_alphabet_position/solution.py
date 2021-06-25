import re
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in re.sub('[^a-zA-Z]', '', text.lower()))