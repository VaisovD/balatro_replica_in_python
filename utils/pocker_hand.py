from base_classes import Card, Suit, Rank, PokerHand


def get_poker_hand(hand: list[Card]) -> str | None:
    """
    Get the poker hand from a list of cards.

    :param hand: The list of cards.
    :return: The poker hand in string format.
    """
    assert isinstance(hand, list), f"Hand must be a list: {hand}"
    assert len(hand) <= 5, f"Hand must contain at most 5 cards: {hand}"
    assert len(hand) > 0, f"Hand must contain at least 1 card: {hand}"
    assert all(isinstance(card, Card) for card in hand), f"All elements in hand must be Card objects: {hand}"

    stones = [card for card in hand if card.get_suit() is None]
    non_stones = [card for card in hand if card.get_suit() is not None]

    is_flush = False
    is_straight = False
    is_royal = False
    is_five_of_a_kind = False
    is_full_house = False
    if len(hand) == 5 and len(non_stones) == 5:
        is_flush = all(card.compare_suits(hand[0]) for card in hand)

        sorted_cards = list(sorted(hand, key=lambda card: card.get_rank()))
        is_straight = all(
            sorted_cards[i].get_rank() + 1 == sorted_cards[i + 1].get_rank()
            for i in range(len(sorted_cards) - 1)
        )
        if (
            sorted_cards[0].get_rank() == "10" and
            sorted_cards[1].get_rank() == "Jack" and
            sorted_cards[2].get_rank() == "Queen" and
            sorted_cards[3].get_rank() == "King" and
            sorted_cards[4].get_rank() == "Ace"
        ):
            is_royal = True

        is_five_of_a_kind = len(set(card.get_rank() for card in hand)) == 1


    if is_flush and is_straight and is_royal:
        return "Flush Royal"
    if is_flush and is_straight:
        return "Straight Flush"
    if is_flush:
        return "Flush"
    if is_straight:
        return "Straight"

    return "High Card"
