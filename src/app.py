from flask import request
import json
from . import create_app
from .models import Words, db


app = create_app()


@app.route('/', methods=['GET'])
def fetch():
    words = Words.query.filter_by(learned=False).limit(5).all()
    all_words = {}
    for word in words:
        if word.origin_language not in all_words:
            all_words[word.origin_language] = []
        word_dict = {
            'id': word.id,
            'word': word.word,
            'english_meaning': word.english_meaning
        }

        all_words[word.origin_language].append(word_dict)

    return json.dumps(all_words), 200


@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    word = data['word']
    origin_language = data['origin_language']
    english_meaning = data['english_meaning']
    learned = data['learned']

    word = Words(word=word, origin_language=origin_language, english_meaning=english_meaning, learned=learned)
    db.session.add(word)
    db.session.commit()
    x = Words.query.all()
    print('>>>>',x)
    return json.dumps("Added"), 200


@app.route('/remove/<word_id>', methods=['DELETE'])
def remove(word_id):
    Words.query.filter_by(id=word_id).delete()
    db.session.commit()
    return json.dumps("Deleted"), 200


@app.route('/edit/<word_id>', methods=['PATCH'])
def edit(word_id):
    data = request.get_json()
    learned = data['learned']
    word_to_update = Words.query.filter_by(id=word_id).all()[0]
    word_to_update.learned = learned
    db.session.commit()
    return json.dumps('Edited'), 200

