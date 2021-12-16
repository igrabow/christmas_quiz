from flask import render_template, flash, redirect, url_for
from app.main import bp
from app.main.forms import QuestionForm, StartForm, StartGameForm
from app.main.quiz import Quiz


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = StartForm()
    if form.validate_on_submit():
        return redirect(url_for('main.start_game'))
    return render_template('index.html', title='Weihnachtsquiz', form=form)


@bp.route('/start_game', methods=['GET', 'POST'])
def start_game():
    form = StartGameForm()
    if form.validate_on_submit():
        if form.players.data:
            q = Quiz()
            q.save_players(form.players.data)
        return redirect(url_for('main.question'))
    return render_template('start_game.html',
                           title='Weihnachtsquiz', form=form)


@bp.route('/question', methods=['GET', 'POST'])
def question():
    form = QuestionForm()
    if form.validate_on_submit():
        if form.player_choices.data:
            q = Quiz()
            q.add_point(form.player_choices.data)
        return redirect(url_for('main.question'))
    q = Quiz()
    question, answer, audio_file = q.get_next_question()

    choices = []
    players = q.get_players()
    for player, score in players.items():
        choices.append((player, player))
    form.player_choices.choices = choices
    if not question:
        return render_template(
            'game_over.html',
            title='Weihnachtsquiz',
            players=players)
    return render_template(
        'question.html',
        title='Weihnachtsquiz',
        form=form,
        question=question,
        answer=answer,
        audio_file=audio_file,
        players=players)
