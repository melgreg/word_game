class Player:

    def __init__(self, name):
        self.name = name
        self.tiles = []
        self.words_played = []
        self.score = 0


    def add_tiles(self, new_tiles):
        """Add new tiles to tiles in hand."""
        self.tiles += new_tiles


    def show_tiles(self):
        return ",".join(self.tiles)
