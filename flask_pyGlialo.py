from flask import Flask, render_template, redirect, url_for
import pyGlialo as py
from pyGlialo import MEETUP_JSON, LIST_OF_WINNERS


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',event = py.get_event())


@app.route('/random')
def spread_the_goodies():
    winner_json = py.extract_safe_winner(MEETUP_JSON)
    winner = {
        'name': winner_json['member']['name'],
        'member_id': winner_json['member']['member_id'],
        'photo_url': py.safe_photo_url(winner_json)
    }
    lead_text = 'Rolling for goodies Number %s' % str(len(LIST_OF_WINNERS) + 1)
    # print(len(MEETUP_JSON['results']))
    return render_template('random.html', winner=winner, winners=LIST_OF_WINNERS, lead_text=lead_text)


@app.route('/save/<name>/')
def save_winner(name):
    if name not in LIST_OF_WINNERS:
        LIST_OF_WINNERS.append(name)
        py.remove_member_from_pool(name)
    return redirect(url_for('saved'))


@app.route('/saved')
def saved():
    name = LIST_OF_WINNERS[-1]
    winner = {
        'name': name
    }
    lead_text = 'Winner for slot %s' % str(len(LIST_OF_WINNERS))
    return render_template('saved.html', winner=winner, winners=LIST_OF_WINNERS, lead_text=lead_text)


@app.route('/pass')
def pass_extraction():
    LIST_OF_WINNERS.append('empty_slot')
    lead_text = 'Slot %s is empty :(' % str(len(LIST_OF_WINNERS))
    return render_template('pass.html', winners=LIST_OF_WINNERS, lead_text=lead_text)


@app.route('/finalize')
def finalize_the_goodies():
    py.save_winners_list(LIST_OF_WINNERS)
    return render_template('finalize.html', winners=LIST_OF_WINNERS)


@app.route('/reset')
def reset_app():
    MEETUP_JSON = py.get_meetup_json()  # reset_meetup_json()
    LIST_OF_WINNERS.clear()
    winner = {
        'name': 'PyGlialo is Reset',
        'member_id': '000000',
        'photo_url': '/static/img/Reset_Icon.png'
    }
    reset_text = 'Reset Successful'
    return render_template('random.html', winner=winner, winners=LIST_OF_WINNERS, lead_text=reset_text)


if __name__ == '__main__':
    app.run(debug=True)
