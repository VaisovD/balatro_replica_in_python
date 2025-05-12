
class Suit:
    """
    Represents a suit in balatro.
    """

    suits = [
        "Hearts",
        "Diamonds",
        "Clubs",
        "Spades",
    ]
    symbols = [
        "♥",
        "♦",
        "♣",
        "♠",
    ]

    def __init__(self, name: str):
        """
        Initialize the suit with a name and symbol.
        :param name: The name of the suit (e.g., 'Hearts', 'Diamonds').
        """
        assert name in self.suits, f"Invalid suit: {name}. Valid suits are: {self.suits}"
        self.name = name
        self.symbol = self.symbols[self.suits.index(name)] if name in self.suits else None

    def __str__(self):
        return f"{self.symbol}"

    def __repr__(self):
        return f"Suit({self.name})"

    def __eq__(self, other):
        if isinstance(other, Suit):
            return self.name == other.name
        if other is None:
            return False
        raise TypeError(f"Cannot compare Suit with {type(other)}")
