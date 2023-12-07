
from functools import cmp_to_key
from collections import Counter
from enum import Enum

class HandType(Enum):
  FIVE_OF_A_KIND = 6
  FOUR_OF_A_KIND = 5
  FULL_HOUSE = 4
  THREE_OF_A_KIND = 3
  TWO_PAIR = 2
  ONE_PAIR = 1
  HIGH_CARD = 0

def part1(input):
  sum = 0

  def get_hand_type(hand):
    top_two = Counter(hand).most_common(2)

    if (top_two[0][1] == 5):
      return HandType.FIVE_OF_A_KIND
    elif (top_two[0][1] == 4):
      return HandType.FOUR_OF_A_KIND
    elif (top_two[0][1] == 3 and top_two[1][1] == 2):
      return HandType.FULL_HOUSE
    elif (top_two[0][1] == 3):
      return HandType.THREE_OF_A_KIND
    elif (top_two[0][1] == 2 and top_two[1][1] == 2):
      return HandType.TWO_PAIR
    elif (top_two[0][1] == 2):
      return HandType.ONE_PAIR
    
    return HandType.HIGH_CARD

  face_card_values = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
  }

  def card_to_val(card):
    if (card.isnumeric()):
      return int(card)
    else:
      return face_card_values[card]

  def compare_hands(a, b):
    a_hand = a[0]
    b_hand = b[0]
    a_hand_type = get_hand_type(a_hand)
    b_hand_type = get_hand_type(b_hand)
    if (a_hand_type == b_hand_type):
      for i in range(0, len(a_hand)):
        a_card = card_to_val(a_hand[i])
        b_card = card_to_val(b_hand[i])

        if (a_card != b_card):
          return a_card - b_card

    return a_hand_type.value - b_hand_type.value

  parsed_input = [l.split() for l in input]
  si = sorted(parsed_input, key=cmp_to_key(compare_hands))

  for i, hand_data in enumerate(si):
    sum += (i + 1) * int(hand_data[1])

  return sum

def part2(input):
  sum = 0

  def get_hand_type(hand):
    top_two = list(filter(lambda x: x[0] != "J", Counter(hand).most_common(3)))
    if (len(top_two) == 3):
      del top_two[-1]

    joker_count = hand.count("J")
    if (joker_count == 5):
      return HandType.FIVE_OF_A_KIND

    if (top_two[0][1] >= (5 - joker_count)):
      return HandType.FIVE_OF_A_KIND
    elif (top_two[0][1] >= (4 - joker_count)):
      return HandType.FOUR_OF_A_KIND
    elif (top_two[0][1] >= (3 - joker_count) and top_two[1][1] == 2):
      return HandType.FULL_HOUSE
    elif (top_two[0][1] >= (3 - joker_count)):
      return HandType.THREE_OF_A_KIND
    elif (top_two[0][1] == 2 and top_two[1][1] == 2):
      return HandType.TWO_PAIR
    elif (top_two[0][1] >= (2 - joker_count)):
      return HandType.ONE_PAIR
    
    return HandType.HIGH_CARD

  face_card_values = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "J": 1,
  }

  def card_to_val(card):
    if (card.isnumeric()):
      return int(card)
    else:
      return face_card_values[card]

  def compare_hands(a, b):
    a_hand = a[0]
    b_hand = b[0]
    a_hand_type = get_hand_type(a_hand)
    b_hand_type = get_hand_type(b_hand)
    if (a_hand_type == b_hand_type):
      for i in range(0, len(a_hand)):
        a_card = card_to_val(a_hand[i])
        b_card = card_to_val(b_hand[i])

        if (a_card != b_card):
          return a_card - b_card

    return a_hand_type.value - b_hand_type.value

  parsed_input = [l.split() for l in input]
  si = sorted(parsed_input, key=cmp_to_key(compare_hands))

  for i, hand_data in enumerate(si):
    sum += (i + 1) * int(hand_data[1])

  return sum