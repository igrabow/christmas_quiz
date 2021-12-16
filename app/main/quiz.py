import json
import random


class Quiz:
    def __init__(self):
        with open('done.json', 'r') as f:
            try:
                done_file = json.load(f)
                self.done = done_file['data']
            except:
                self.done = []
            f.close()

        with open('questions.json', 'r') as f:
            try:
                self.questions = json.load(f)
            except:
                self.questions = []
            f.close()

        with open('players.json', 'r') as f:
            try:
                self.players = json.load(f)
            except:
                self.players = dict()
            f.close()

    def save_file(self, filename, data):
        with open(filename, 'w') as f:
            json.dump(data, f)
            f.close()

    def save_players(self, players):
        self.save_file('done.json', dict())
        players_dict = dict()
        players = players.split(',')
        for player in players:
            players_dict[player] = 0
        self.save_file('players.json', players_dict)

    def get_next_question(self):
        pick = True
        questions = self.questions['data']
        random.shuffle(questions)
        while pick is True:
            for question in questions:
                if question['question'] not in self.done:
                    # Save done to done questions
                    self.done.append(question['question'])
                    self.save_file('done.json', dict(data=self.done))

                    return (question.get('question'),
                            question.get('answer'),
                            question.get('audio_file')
                            )
            self.save_file('done.json', dict())
            pick = False
        return '', '', ''

    def get_players(self):
        return self.players

    def add_point(self, player):
        players = self.players
        players[player] += 1
        self.save_file('players.json', players)
