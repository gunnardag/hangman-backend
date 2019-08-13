import random
from flask import Flask, request, make_response, render_template
from models import Game, PrivateWord, init_app

app = Flask(__name__)
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/gunnar/Backend/hangman/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/gunnar/botti/test.db'

init_app(app)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/image/<image_id>")
def get_image(image_id):
    return app.send_static_file("Hangman-{}.png".format(image_id))


@app.route("/newgame")
def new_game():

    game_id = request.args.get('game_id')
    word = None
    try:
        word = PrivateWord.query.filter_by(id=game_id).first().word if game_id else get_random_word()
    except AttributeError:
        pass
    if not word:
        return make_response("Wrong game id given", 400)

    game = Game(word=word, user_id="anonymous")
    game.create()

    return make_response(word, 200)




@app.route("/creategame")
def create_game():

    game_id = create_id()
    word = request.args.get('word')

    if word:
        private_word = PrivateWord(id=game_id, word=word)
        private_word.create()
        return make_response(game_id, 200)
    else:
        return make_response("no word given", 400)


def create_id():
    file = open('wordlist.txt')
    lines = file.read().splitlines()
    random_id = "{}{}".format(lines[random.randint(0, 7775)], lines[random.randint(0, 7775)])
    return random_id


def get_random_word():
    file = open('icelandicwords.txt')
    lines = file.read().splitlines()
    return lines[random.randint(0, 4997)]
