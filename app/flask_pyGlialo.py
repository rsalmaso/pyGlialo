from flask import Flask, render_template, redirect, url_for

from app.pyGlialo import *

app = Flask(__name__)


@app.route('/')
def spread_the_goodies():
    winner_json = extract_safe_winner(MEETUP_JSON)
    winner = {
        'name': winner_json['member']['name'],
        'member_id': winner_json['member']['member_id'],
        'photo_url': safe_photo_url(winner_json)
    }
    lead_text = 'Rolling for goodies Number %s' % str(len(LIST_OF_WINNERS) + 1)
    return render_template('index.html', winner=winner, winners=LIST_OF_WINNERS, lead_text=lead_text)


@app.route('/save/<name>/')
def save_winner(name):
    if name not in LIST_OF_WINNERS:
        LIST_OF_WINNERS.append(name)
    return redirect(url_for('spread_the_goodies'))


@app.route('/pass')
def pass_extraction():
    LIST_OF_WINNERS.append('empty_slot')
    return redirect(url_for('spread_the_goodies'))


@app.route('/finalize')
def finalize_the_goodies():
    save_winners_list(LIST_OF_WINNERS)
    return render_template('finalize.html', winners=LIST_OF_WINNERS)


@app.route('/reset')
def reset_app():
    meetup_json = get_meetup_json()  # reset_meetup_json()
    LIST_OF_WINNERS.clear()
    winner = {
        'name': 'PyGlialo is Reset',
        'member_id': '000000',
        'photo_url': 'img/reset.jpg'
    }
    reset_text = 'Reset Successful'
    return render_template('index.html', winner=winner, winners=LIST_OF_WINNERS, lead_text=reset_text)


if __name__ == '__main__':
    app.run(debug=True)
