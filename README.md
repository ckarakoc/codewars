# Celal Karakoç - Codewars 

## Prerequisites
python libraries:

    beautifulsoup4
    selenium
    Jinja2

Download [geckodriver](https://github.com/mozilla/geckodriver/releases) or [chromedriver](https://chromedriver.chromium.org/downloads) and put it into the `./drivers` folder.

Add your [codewars](https://www.codewars.com) username and password in the `config.py` file (copy-paste `config.py.example` > `config.py`).

## Run
The `extensions.json` file in `assets\json\ ` does not support all programming languages. Add the programming languages you want it to support based on the json-object structure. You can search through [this gist](https://gist.github.com/ppisarczyk/43962d06686722d26d176fad46879d41) for examples.

run `python main.py --url <url> --driver <'geckodriver' or 'chromedriver'> --headless`

## TODO
- Implement logging properly
- Add 404 page iwth 404favicon.ico