import re
def domain_name(url):
    return re.sub('https?://|www\.', '', url).split('.', 1)[0]