from base_classes.rank import Rank
from base_classes.suit import Suit


class Card:
    """
    Base class for a card in balatro
    """

    enhancements = [
        "Bonus",
        "Mult",
        "Steel",
        "Gold",
        "Stone",
        "Glass",
        "Wildcard",
    ]

    editions = [
        "Base",
        "Foil",
        "Holographic",
        "Polychrome",
    ]

    def __init__(
        self,
        suit: Suit | None,
        rank: Rank | None,
        base_chips: float = 0,
        base_mult: float = 0,
        times_mult: float = 1,
        enhancement: str | None = None,
        edition: str | None = "Base",
    ):
        """
        Initialize the card with a suit and rank.

        :param suit: The suit of the card (e.g., 'Hearts', 'Diamonds'). base_classes.suit.Suit
        :param rank: The rank of the card (e.g., 'Ace', '2', '3'). base_classes.rank.Rank
        :param base_chips: The base chips of the card.
        :param base_mult: The base multiplier of the card.
        :param times_mult: The times multiplier of the card.
        """
        assert isinstance(suit, Suit), f"Invalid suit: {suit}. Must be an instance of base_classes.suit.Suit"
        assert isinstance(rank, Rank), f"Invalid rank: {rank}. Must be an instance of base_classes.rank.Rank"
        assert base_chips >= 0, f"Base chips cannot be negative: {base_chips}"
        assert base_mult >= 0, f"Base multiplier cannot be negative: {base_mult}"
        assert times_mult > 0, f"Times multiplier must be greater than 0: {times_mult}"

        self.suit = suit
        self.rank = rank
        self.base_chips = float(base_chips)
        self.base_mult = float(base_mult)
        self.times_mult = float(times_mult)
        self.enhancement = enhancement if enhancement in self.enhancements else None
        self.edition = edition if edition in self.editions else None

    def get_suit(self) -> Suit | None:
        """
        Get the suit of the card.

        :return: The suit of the card.
        """
        if self.enhancement == "Stone":
            return None
        return self.suit

    def get_rank(self) -> Rank | None:
        """
        Get the rank of the card.

        :return: The rank of the card.
        """
        if self.enhancement == "Stone":
            return None
        return self.rank

    def get_base_chips(self) -> float:
        """
        Get the base chips of the card.

        :return: The base chips of the card.
        """
        total_chips = self.base_chips
        if self.enhancement == "Stone":
            return 50
        if self.edition == "Foil":
            total_chips += 50
        return total_chips

    def get_base_mult(self) -> float:
        """
        Get the base multiplier of the card.

        :return: The base multiplier of the card.
        """
        mult = self.base_mult
        if self.enhancement == "Mult":
            mult += 4
        return mult

    def get_times_mult(self) -> float:
        """
        Get the times multiplier of the card.

        :return: The times multiplier of the card.
        """
        times_mult = self.times_mult
        if self.edition == "Polychrome":
            times_mult += 1.5
        return times_mult

    def compare_suits(self, other) -> bool:
        """
        Compare the suits of two cards.

        :param other: The other card to compare with.
        :return: True if the suits are equal, False otherwise.
        """
        if not isinstance(other, Card):
            raise TypeError(f"Cannot compare Card with {type(other)}")
        if self.enhancement == "Stone" or other.enhancement == "Stone":
            return False
        if self.enhancement == "Wildcard" or other.enhancement == "Wildcard":
            return True
        return self.suit == other.suit

    def compare_ranks(self, other) -> bool:
        """
        Compare the ranks of two cards.

        :param other: The other card to compare with.
        :return: True if the ranks are equal, False otherwise.
        """
        if not isinstance(other, Card):
            raise TypeError(f"Cannot compare Card with {type(other)}")
        if self.enhancement == "Stone" or other.enhancement == "Stone":
            return False
        return self.rank == other.rank
