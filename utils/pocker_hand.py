from base_classes import Card, Suit, Rank, PokerHand


def get_poker_hand(hand: list[Card]) -> tuple[str, list[str]]:
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
    scoring = [card.uid for card in stones]
    non_stones = [card for card in hand if card.get_suit() is not None]
    sorted_cards = list(sorted(non_stones, key=lambda card: card.get_rank()))
    if len(non_stones) == 0:
        return "High Card", scoring

    is_flush = False
    is_straight = False
    is_royal = False
    is_five_of_a_kind = False
    is_full_house = False
    if len(hand) == 5 and len(non_stones) == 5:
        is_flush = all(card.compare_suits(non_stones[0]) for card in non_stones)

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
        house_check: dict = {}
        for card in hand:
            rank = card.get_rank()
            if rank in house_check:
                house_check[rank] += 1
            else:
                house_check[rank] = 1
        if len(house_check) == 2 and any(v == 3 for v in house_check.values()):
            is_full_house = True
    # check for four of a kind
    is_four_of_a_kind = False
    my_dict: dict = {}
    for card in hand:
        rank = card.get_rank()
        if rank in my_dict:
            my_dict[rank] += 1
        else:
            my_dict[rank] = 1
    for i, v in my_dict.items():
        if v == 4:
            is_four_of_a_kind = True
            scoring.extend([card.uid for card in hand if card.get_rank() == i])
            break

    if is_flush and is_straight and is_royal:
        scoring = [c.uid for c in hand]
        return "Flush Royal", scoring
    if is_flush and is_straight:
        scoring = [c.uid for c in hand]
        return "Straight Flush", scoring
    if is_five_of_a_kind and is_flush:
        scoring = [c.uid for c in hand]
        return "Flush Five", scoring
    if is_five_of_a_kind:
        scoring = [c.uid for c in hand]
        return "Five of a Kind", scoring
    if is_four_of_a_kind:
        return "Four of a Kind", scoring
    if is_full_house and is_flush:
        scoring = [c.uid for c in hand]
        return "Flush House", scoring
    if is_full_house:
        scoring = [c.uid for c in hand]
        return "Full House", scoring
    if is_flush:
        scoring = [c.uid for c in hand]
        return "Flush", scoring
    if is_straight:
        scoring = [c.uid for c in hand]
        return "Straight", scoring
    counts = {}
    for key, value in my_dict.items():
        if value in counts:
            if key in counts[value]:
                counts[value][key] += 1
            else:
                counts[value][key] = 1
        else:
            counts[value] = {key: 1}

    for i, v in counts.items():
        if i == 3:
            scoring.extend([card.uid for card in hand if card.get_rank() == v])
            return "Three of a Kind", scoring
        if i == 2 and len(v) == 2:
            for key in v:
                scoring.extend([card.uid for card in hand if card.get_rank() == key])
            return "Two Pair", scoring
        if i == 2 and len(v) == 1:
            scoring.extend([card.uid for card in hand if card.get_rank() == v])
            return "Pair", scoring
    # append the card with the highest rank to the scoring list
    scoring.append(sorted_cards[-1].uid)
    return "High Card", scoring
