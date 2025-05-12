from base_classes import Card, Suit, Rank
from utils.pocker_hand import get_poker_hand


# Test cases for the Poker Hand Recognition
diamond_suit = Suit("Diamonds")
heart_suit = Suit("Hearts")
club_suit = Suit("Clubs")
spade_suit = Suit("Spades")

nine_of_diamonds = Card(diamond_suit, Rank("9"))
nine_of_spades = Card(spade_suit, Rank("9"))
ten_of_diamonds = Card(diamond_suit, Rank("10"))
jack_of_diamonds = Card(diamond_suit, Rank("Jack"))
queen_of_diamonds = Card(diamond_suit, Rank("Queen"))
king_of_diamonds = Card(diamond_suit, Rank("King"))
ace_of_diamonds = Card(diamond_suit, Rank("Ace"))
stone_card = Card(diamond_suit, Rank("Ace"), enhancement="Stone")

royal_flush_hand = [
    ten_of_diamonds,
    jack_of_diamonds,
    queen_of_diamonds,
    king_of_diamonds,
    ace_of_diamonds,
]
print([str(i) for i in royal_flush_hand], " =>  ", get_poker_hand(royal_flush_hand))
straight_flush_hand = [
    nine_of_diamonds,
    ten_of_diamonds,
    jack_of_diamonds,
    queen_of_diamonds,
    king_of_diamonds,
]
print([str(i) for i in straight_flush_hand], " =>  ", get_poker_hand(straight_flush_hand))
four_of_a_kind_hand = [
    nine_of_diamonds,
    nine_of_spades,
    nine_of_diamonds,
    nine_of_diamonds,
    nine_of_diamonds,
]
print([str(i) for i in four_of_a_kind_hand], " =>  ", get_poker_hand(four_of_a_kind_hand))
three_of_a_kind_hand = [
    nine_of_diamonds,
    nine_of_spades,
    nine_of_diamonds,
    ten_of_diamonds,
    ten_of_diamonds,
]
print([str(i) for i in three_of_a_kind_hand], " =>  ", get_poker_hand(three_of_a_kind_hand))
two_pair_hand = [
    nine_of_diamonds,
    nine_of_spades,
    ten_of_diamonds,
    ten_of_diamonds,
    jack_of_diamonds,
]
print([str(i) for i in two_pair_hand], " =>  ", get_poker_hand(two_pair_hand))
one_pair_hand = [
    nine_of_diamonds,
    nine_of_spades,
    ten_of_diamonds,
    jack_of_diamonds,
    queen_of_diamonds,
]
print([str(i) for i in one_pair_hand], " =>  ", get_poker_hand(one_pair_hand))
high_card_hand = [
    nine_of_diamonds,
    jack_of_diamonds,
    queen_of_diamonds,
    king_of_diamonds,
    stone_card,
]
print([str(i) for i in high_card_hand], " =>  ", get_poker_hand(high_card_hand))
flush_hand = [
    nine_of_diamonds,
    ten_of_diamonds,
    jack_of_diamonds,
    queen_of_diamonds,
    ace_of_diamonds,
]
print([str(i) for i in flush_hand], " =>  ", get_poker_hand(flush_hand))
full_house_hand = [
    nine_of_diamonds,
    nine_of_spades,
    ten_of_diamonds,
    ten_of_diamonds,
    ten_of_diamonds,
]
print([str(i) for i in full_house_hand], " =>  ", get_poker_hand(full_house_hand))
flush_house_hand = [
    nine_of_diamonds,
    nine_of_diamonds,
    ten_of_diamonds,
    ten_of_diamonds,
    ten_of_diamonds,
]
print([str(i) for i in flush_house_hand], " =>  ", get_poker_hand(flush_house_hand))
