import random

class Game:
    def __init__(self, letters=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "],
                 points=[1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0],
                 num_tiles=[9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1, 2]):
        self.letter_to_points = {letters[i]: points[i] for i in range(len(letters))}
        self.tiles = []
        for letter, number in zip(letters, num_tiles):
            self.tiles += [letter for _ in range(number)]
        random.shuffle(self.tiles)
    
    


##def score_word(word):
##    '''Calculate the score for word.'''
##    return sum(letter_to_points.get(letter, 0) for letter in word.upper())


##player_to_words = {
##  "player1" : ["BLUE", "TENNIS", "EXIT"],
##  "wordNerd" : ["EARTH", "EYES", "MACHINE"],
##  "Lexi Con" : ["ERASER", "BELLY", "HUSKY"],
##  "Prof Reader" : ["ZAP", "COMA", "PERIOD"],
##}
##
##player_to_points = {}
##for player, words in player_to_words.items():
##  player_points = sum(score_word(word) for word in words)
##  player_to_points[player] = player_points
##
##def play_word(player, word):
##  player_to_words[player].append(word.upper())
##  score = score_word(word)
##  player_to_points[player] += score

if __name__ == "__main__":
      game = Game()
      print(game.tiles)
