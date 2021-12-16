from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import ValidationError, DataRequired, Length
from app.main.quiz import Quiz


class StartForm(FlaskForm):
    submit = SubmitField('Starten')


class StartGameForm(FlaskForm):
    players = TextAreaField('Players')
    submit = SubmitField('Starten')


class QuestionForm(FlaskForm):
    q = Quiz()
    players = q.get_players()
    choices = []
    for player, score in players.items():
        choices.append((player, player))
    player_choices = RadioField(
        'Wer hat geantwortet?',
        choices=choices)
    submit = SubmitField('Nächste Frage')
