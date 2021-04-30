import random
import player

class Game:
    def __init__(self, letters=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "],
                 points=[1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0],
                 num_tiles=[9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1, 2]):
        self.letter_to_points = {letters[i]: points[i] for i in range(len(letters))}
        self.tiles = []
        for letter, number in zip(letters, num_tiles):
            self.tiles += [letter for _ in range(number)]
        random.shuffle(self.tiles)
        self.players = []
        for num in range(1, 5):
            name = input(f"Please enter a name for player #{num} or press enter to start: ")
            if not name:
                break
            self.add_player(name)
        self.play()
    
    def play(self):
        '''Continue until there are no more free tiles left.'''
        while self.tiles:
            for player in self.players:
                self.ask_for_word(player)
        
    def add_player(self, name):
        new_player = player.Player(name)
        self.assign_tiles(new_player)
        self.players.append(new_player)


    def assign_tiles(self, player, num_tiles=7):
        """Assign num_tiles tiles to player."""
        if len(self.tiles) <= num_tiles:
            player.add_tiles(self.tiles)
            self.tiles = []
        else:
            random.shuffle(self.tiles)
            tiles = []
            for _ in range(num_tiles):
                tiles.append(self.tiles.pop())
            player.add_tiles(tiles)

    def score_word(self, word):
        return sum(self.letter_to_points[letter] for letter in word)
    
    def ask_for_word(self, player):
        print(f"{player.name}'s tiles: {player.show_tiles()}")
        word = input(f"{player.name}, please enter a word: ")
        result = player.play_word(word)
        if result:
            score = self.score_word(result)
            print(f"{result} is worth {score} points.")
            player.update_score(score)
            self.assign_tiles(player, len(result))
        else:
            print(f"{word} is not valid.")
        print(f"{player.name}'s current score is: {player.score} points.")
            
if __name__ == "__main__":
      game = Game()



      
