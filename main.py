
from random import randrange

global score, play_count

score = 0
play_count = 0
ENGLISH_INDEX = 0
ORIGINAL_INDEX = 1

hiragana = [
    [["a", "あ"],  ["i", "い"],  ["u", "う"],  ["e", "え"],  ["o", "お"]],
    [["ka", "か"], ["ki", "き"], ["ku", "く"], ["ke", "け"], ["ko", "こ"]],
    [["sa", "さ"], ["shi", "し"], ["su", "す"], ["se", "せ"], ["so", "そ"]],
    [["ta", "た"], ["chi", "ち"], ["tsu", "つ"], ["te", "て"], ["to", "と"]],
    [["na", "な"], ["ni", "に"], ["nu", "ぬ"], ["ne", "ね"], ["no", "の"]],
    [["ha", "は"], ["hi", "ひ"], ["fu", "ふ"], ["he", "へ"], ["ho", "ほ"]],
    [["ma", "ま"], ["mi", "み"], ["mu", "む"], ["me", "め"], ["mo", "も"]],
    [["ya", "や"], ["yu", "ゆ"], ["yo", "よ"]],
    [["ra", "ら"], ["ri", "り"], ["ru", "る"], ["re", "れ"], ["ro", "ろ"]],
    [["wa", "わ"], ["wo", "を"]],
    [["n", "ん"]],
]

def random_question():
    global score, play_count
    picked_hiranalist = hiragana[randrange(len(hiragana))]
    picked_hirana = picked_hiranalist[randrange(len(picked_hiranalist))]

    try:
        percentage = score / float(play_count) * 100.0
    except ZeroDivisionError:
        percentage = 100.0

    print("current percentage : {:3.2f} ({}/{})".format(percentage, score, play_count))
    print("What is this? : {0}".format(picked_hirana[ORIGINAL_INDEX]))
    player_answer = input()
    if check_answer(player_answer, picked_hirana[ENGLISH_INDEX]):
        print("correct!")
        score += 1
    else:
        print("incorrect! answer is {0}".format(picked_hirana[ENGLISH_INDEX]))
    play_count += 1

def check_answer(player_answer, answer):
    if player_answer == "si" and answer == "shi":
        return True
    if player_answer == "hu" and answer == "fu":
        return True
    if player_answer == "tu" and answer == "tsu":
        return True
    if player_answer == "ti" and answer == "chi":
        return True
    return player_answer == answer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        random_question()
