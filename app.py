from flask import Flask
from flask import request
from grade2Translator.updatedBrailleTranslator import translate_word as tr


app = Flask(__name__)


@app.route('/translate', methods=['POST'])
def translate():
    d = request.get_json(force=True)
    return {
        "response": tr(d['translate'])
    }


if __name__ == '__main__':
    app.run()
