import pickle

import memcache

from models.DotsGame import create_new_game

_mc = memcache.Client(['127.0.0.1:11211'])

def new_session(token):
    game_session = create_new_game()
    dump = pickle.dumps(game_session)
    _mc.set(token, dump, time=60*60)

def save_session(token, session):
    dump = pickle.dumps(session)
    _mc.set(token, dump, time=60*60)

def load_session(token):
    dump = _mc.get(token)
    game_session = pickle.loads(dump)
    return game_session
