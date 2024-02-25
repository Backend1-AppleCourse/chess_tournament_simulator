import random

class Player:
    def __init__(self, ranking, name, points):
        self.ranking = ranking
        self.name = name
        self.points = points

    def play(self, opponent):
        draw = 0.2
        player_win_chances = 0.4
        opponent_win_chances = 0.4

        diff = 1 - opponent.ranking/self.ranking 
        player_win_chances += diff
        opponent_win_chances -= diff

        result = random.choices([self, opponent, None], [player_win_chances, opponent_win_chances, draw])[0]
        if result == self:
            self.points += 1
        elif result == opponent:
            opponent.points += 1
        else:
            self.points += 0.5
            opponent.points += 0.5
        return result

    def __str__(self):
        return f'{self.ranking} {self.name} ({self.points} points)'

def _get_schedule(players):
        if len(players) % 2:
            players.append('Bye')
        
        schedule = []
        for i in range(len(players) - 1):
            round_matches = []
            for j in range(len(players) // 2):
                round_matches.append((players[j], players[len(players) - j - 1]))
            players.insert(1, players.pop()) 
            schedule.append(round_matches)
        
        return schedule

# round robin chess tournament
class Tournament:
    

    def __init__(self, players):
        self.players = players
        self.schedule = _get_schedule(players)

    def play_tournament(self):
        for round_matches in self.schedule:
            for mch in round_matches:
                mch[0].play(mch[1])
        return self.get_ranking()

    def get_winner(self):
        return max(self.players, key=lambda player: player.points)

    def get_loser(self):
        return min(self.players, key=lambda player: player.points)

    def get_ranking(self):
        return sorted(self.players, key=lambda player: player.points, reverse=True)
    
    def __str__(self):
        return '\n'.join([str(player) for player in self.get_ranking()])


tournamnet = Tournament([
        Player(random.randint(1500,2000), 'Alice', 0), 
        Player(random.randint(1500,2000), 'Bob', 0), 
        Player(random.randint(1500,2000), 'Charlie', 0), 
        Player(random.randint(1500,2000), 'David', 0)
    ])


tournamnet.play_tournament()
print(tournamnet.get_winner())
