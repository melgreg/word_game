class Player:

    def __init__(self, name):
        self.name = name
        self.tiles = []
        self.words_played = []
        self.score = 0


    def __gt__(self, other):
        return self.score > other.score

    def __str__(self):
        return f"{self.name}: {self.score} points. Words played:\n{self.words_played}"
    
    def add_tiles(self, new_tiles):
        """Add new tiles to tiles in hand."""
        self.tiles += new_tiles


    def show_tiles(self):
        return ",".join(self.tiles)


    def update_score(self, points):
        self.score += points

        
    def play_word(self, word):
        old_tiles = list(self.tiles)
        word = word.upper()
        for i in range(len(word)):
            letter = word[i]
            if letter in self.tiles:
                self.tiles.remove(letter)
            elif " " in self.tiles:
                self.tiles.remove(" ")
                word = word[:i] + " " + word[i+1:]
            else:
                self.tiles = old_tiles
                return
        self.words_played.append(word)
        return word


    def exchange_tiles(self, tiles):
        old_tiles = list(self.tiles)
        tiles = tiles.split(",")
        for tile in tiles:
            try:
                self.tiles.remove(tile)
            except ValueError:
                self.tiles = old_tiles
                return
        return tiles
                
        

