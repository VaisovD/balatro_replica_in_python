class PokerHand:
    """
    A class representing a poker hand with leveling system
    """

    hands = [
        "High Card",
        "Pair",
        "Two Pair",
        "Three of a Kind",
        "Straight",
        "Flush",
        "Full House",
        "Four of a Kind",
        "Straight Flush",
        "Royal Flush",
        "Five of a Kind",
        "Flush House",
        "Flush Five",
    ]
    base_chips = {
        "High Card": 5,
        "Pair": 10,
        "Two Pair": 20,
        "Three of a Kind": 30,
        "Straight": 30,
        "Flush": 35,
        "Full House": 40,
        "Four of a Kind": 60,
        "Straight Flush": 100,
        "Royal Flush": 100,
        "Five of a Kind": 120,
        "Flush House": 140,
        "Flush Five": 160,
    }
    upgrade_chips = {
        "High Card": 10,
        "Pair": 15,
        "Two Pair": 20,
        "Three of a Kind": 20,
        "Straight": 30,
        "Flush": 15,
        "Full House": 25,
        "Four of a Kind": 30,
        "Straight Flush": 40,
        "Royal Flush": 40,
        "Five of a Kind": 35,
        "Flush House": 40,
        "Flush Five": 50,
    }
    base_mult = {
        "High Card": 1,
        "One Pair": 2,
        "Two Pair": 2,
        "Three of a Kind": 3,
        "Straight": 4,
        "Flush": 4,
        "Full House": 4,
        "Four of a Kind": 7,
        "Straight Flush": 8,
        "Royal Flush": 8,
        "Five of a Kind": 12,
        "Flush House": 14,
        "Flush Five": 16,
    }
    upgrade_mult = {
        "High Card": 1,
        "One Pair": 1,
        "Two Pair": 1,
        "Three of a Kind": 2,
        "Straight": 3,
        "Flush": 2,
        "Full House": 2,
        "Four of a Kind": 3,
        "Straight Flush": 4,
        "Royal Flush": 4,
        "Five of a Kind": 3,
        "Flush House": 4,
        "Flush Five": 3,
    }

    def __init__(self, hand: str, level: int = 1):
        """
        Initialize the PokerHand with a hand of cards.

        :param hand: The type of poker hand (e.g., 'High Card', 'One Pair').
        """
        assert hand in self.hands, f"Invalid hand: {hand}. Valid hands are: {self.hands}"
        assert isinstance(level, int), f"Level must be an integer: {level}"
        assert level >= 1, f"Level must be at least 1: {level}"
        self.hand = hand
        self.level = level

    def get_base_chips(self) -> float:
        """
        Get the base chips of the poker hand.

        :return: The base chips of the poker hand.
        """
        chips = self.base_chips[self.hand]
        if self.level > 1:
            chips += self.upgrade_chips[self.hand] * (self.level - 1)
        return chips

    def get_base_mult(self) -> float:
        """
        Get the base multiplier of the poker hand.

        :return: The base multiplier of the poker hand.
        """
        mult = self.base_mult[self.hand]
        if self.level > 1:
            mult += self.upgrade_mult[self.hand] * (self.level - 1)
        return mult

    def __eq__(self, other):
        if isinstance(other, PokerHand):
            return self.hand == other.hand
        if isinstance(other, str):
            return self.hand == other
        if other is None:
            return False
        raise TypeError(f"Cannot compare PokerHand with {type(other)}")
