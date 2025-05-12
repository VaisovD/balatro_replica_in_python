
class Rank:
    """
    Base class for a rank in balatro
    """

    ranks = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    def __init__(
        self,
        rank: str | None,
    ):
        """
        Initialize the rank with a rank.

        :param rank: The rank of the card (e.g., 'Ace', '2', '3').
        """
        assert rank in self.ranks, f"Invalid rank: {rank}. Valid ranks are: {self.ranks}"
        self.rank = rank
        self.index = self.ranks.index(rank)

    def increase_rank(self, n: int = 1):
        """
        Increase the rank by n.

        :param n: The number to increase the rank by.
        """
        assert n > 0, f"Cannot increase rank by a negative number or 0: {n}"
        self.index = (self.index + n) % len(self.ranks)
        self.rank = self.ranks[self.index]

    def __add__(self, other):
        if isinstance(other, int):
            return Rank(self.ranks[(self.index + other) % len(self.ranks)])
        raise TypeError(f"Cannot add {type(other)} to Rank")

    def decrease_rank(self, n: int = 1):
        """
        Decrease the rank by n.

        :param n: The number to decrease the rank by.
        """
        assert n > 0, f"Cannot decrease rank by a negative number or 0: {n}"
        self.index = (self.index - n) % len(self.ranks)
        self.rank = self.ranks[self.index]

    def __sub__(self, other):
        if isinstance(other, int):
            return Rank(self.ranks[(self.index - other) % len(self.ranks)])
        raise TypeError(f"Cannot subtract {type(other)} from Rank")

    def __eq__(self, other):
        if isinstance(other, Rank):
            return self.rank == other.rank
        if isinstance(other, str):
            return self.rank == other
        raise TypeError(f"Cannot compare Rank with {type(other)}")

    def __lt__(self, other):
        if isinstance(other, Rank):
            return self.index < other.index
        raise TypeError(f"Cannot compare Rank with {type(other)}")

    def __le__(self, other):
        if isinstance(other, Rank):
            return self.index <= other.index
        raise TypeError(f"Cannot compare Rank with {type(other)}")

    def __gt__(self, other):
        if isinstance(other, Rank):
            return self.index > other.index
        raise TypeError(f"Cannot compare Rank with {type(other)}")

    def __ge__(self, other):
        if isinstance(other, Rank):
            return self.index >= other.index
        raise TypeError(f"Cannot compare Rank with {type(other)}")

    def __str__(self):
        return self.rank

    def __repr__(self):
        return f"Rank({self.rank})"

    def __hash__(self):
        return hash(self.rank)
