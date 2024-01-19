#!/usr/bin/env python3
from brain_games.brain_even import play_brain_even
from brain_games.scripts.brain_games import main as greeting


def main():
    name_player = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    is_wrong_answer = play_brain_even()
    if not is_wrong_answer:
        print(f"Congratulations, {name_player}!")


if __name__ == "__main__":
    main()
