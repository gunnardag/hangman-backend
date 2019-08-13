# hangman-backend
flask server that saves and distributes random or saved words for hangman

to run in dev mode:

### to install
```
virtualenv -p python3.6 .env
source .env/bin/activate
pip install -r requirements.txt
```

### to run
run python models.py to generate the database
```
python models.py
export FLASK_APP=app.py
flask run
```

### endpoints

You can get images from this url
```
/image/[id]
```

You can create your own game from this url which will return an id for others to play the game
```
/creategame?word=[word]
```

You can create a game, with or without an id, if no id is provided you will get a random Icelandic word
```
/newgame?game_id=[game_id]
```
