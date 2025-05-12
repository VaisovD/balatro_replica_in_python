import orjson as json
import random
import string
import uuid

from base_classes import Card, PokerHand, Suit, Rank


class Loadout:
    """
    Represents a player's loadout in a game. It includes deck, pocker_hand and their levels, consumables.
    """

    def __init__(
        self,
        uid: str = None,
        seed: str = None,
        deck: list[Card] = None,
        pocker_hands: list[PokerHand] = None,
        consumables: list = None,
    ):
        self.uid = str(uuid.uuid4()) if uid is None else uid
        self.seed = seed if seed is not None else self._generate_seed()
        self.deck = deck if deck is not None else self._load_default_deck()
        self.pocker_hands = pocker_hands if pocker_hands is not None else self._load_default_pocker_hands()
        self.consumables = consumables if consumables is not None else self._load_default_consumables()

    @staticmethod
    def _load_default_deck() -> list[Card]:
        """
        Load the default deck of cards.
        :return: The default deck of cards.
        """
        deck = []
        suits = [Suit("Hearts"), Suit("Diamonds"), Suit("Clubs"), Suit("Spades")]
        ranks = [
            Rank("2"), Rank("3"), Rank("4"), Rank("5"), Rank("6"),
            Rank("7"), Rank("8"), Rank("9"), Rank("10"),
            Rank("Jack"), Rank("Queen"), Rank("King"), Rank("Ace")
        ]
        for suit in suits:
            for rank in ranks:
                deck.append(Card(suit, rank))
        return []

    @staticmethod
    def _load_default_pocker_hands() -> list[PokerHand]:
        """
        Load the default poker hands.
        :return: The default poker hands.
        """
        with open("configurations/poker_hands.json", "r") as file:
            data = json.loads(file.read())
            poker_hands = []
            for i in data:
                poker_hand = PokerHand(**i)
                poker_hands.append(poker_hand)
            return poker_hands

    @staticmethod
    def _load_default_consumables() -> list:
        """
        Load the default consumables.
        :return: The default consumables.
        """
        # Placeholder for loading the default consumables
        return []

    @staticmethod
    def _generate_seed() -> str:
        """
        Generate a random seed in the format of ABCD-EFGH.
        :return: The generated seed.
        """
        seed = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) + '-' + \
               ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        return seed
