def blackjack_3cards(deck, card_max):
    max_sum = 0

    for card_1 in range(len(deck)):
        for card_2 in range(card_1 + 1, len(deck)):
            for card_3 in range(card_2 + 1, len(deck)):
                card_sum = deck[card_1] + deck[card_2] + deck[card_3]

                if card_max >= card_sum > max_sum:
                    max_sum = card_sum

    return max_sum

N, M = map(int, input().split())
cards = list(map(int, input().split()))

print(blackjack_3cards(cards, M))

