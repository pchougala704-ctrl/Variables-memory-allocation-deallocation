"""NEON QUEST - The Ultimate Treasure Hunt."""

import os
import random
import sys
from dataclasses import dataclass, field
from typing import Set, Tuple


BOARD_SIZE = 5
START: Tuple[int, int] = (2, 2)
MAX_LIVES = 3
MAX_MOVES = 20
COIN_COUNT = 5
TRAP_COUNT = 4
COIN_POINTS = 10
TREASURE_BONUS = 100

Position = Tuple[int, int]


class Colors:
    """ANSI colors, disabled when output is not an interactive terminal."""

    enabled = sys.stdout.isatty() and os.environ.get("TERM") != "dumb" and "NO_COLOR" not in os.environ

    @classmethod
    def paint(cls, text: str, code: str) -> str:
        if not cls.enabled:
            return text
        return f"\033[{code}m{text}\033[0m"


@dataclass
class GameState:
    player: Position = START
    treasure: Position = (0, 0)
    coins: Set[Position] = field(default_factory=set)
    traps: Set[Position] = field(default_factory=set)
    explored: Set[Position] = field(default_factory=lambda: {START})
    score: int = 0
    lives: int = MAX_LIVES
    moves_left: int = MAX_MOVES
    coins_collected: int = 0
    treasure_found: bool = False


def create_game() -> GameState:
    """Create a fresh map with unique, random item locations."""
    available = [
        (row, column)
        for row in range(BOARD_SIZE)
        for column in range(BOARD_SIZE)
        if (row, column) != START
    ]
    placements = random.sample(available, COIN_COUNT + TRAP_COUNT + 1)

    return GameState(
        treasure=placements[0],
        coins=set(placements[1 : 1 + COIN_COUNT]),
        traps=set(placements[1 + COIN_COUNT :]),
    )


def clear_screen() -> None:
    """Clear the screen only when the game is running in a terminal."""
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def show_welcome() -> None:
    title = r"""
 _   _ _____ ___  _   _   ___  _   _ _____ ____ _____
| \ | | ____/ _ \| \ | | / _ \| | | | ____/ ___|_   _|
|  \| |  _|| | | |  \| || | | | | | |  _| \___ \ | |
| |\  | |__| |_| | |\  || |_| | |_| | |___ ___) || |
|_| \_|_____\___/|_| \_| \__\_\\___/|_____|____/ |_|
                 THE ULTIMATE TREASURE HUNT
"""
    print(Colors.paint(title, "96;1"))
    print(Colors.paint("Explore the lost grid. Collect coins. Outsmart the traps.", "95"))
    print("Find the hidden treasure before your lives or moves run out!")
    print()
    print("Controls: W = up   A = left   S = down   D = right")
    print("You have 3 lives and 20 moves. Good luck, explorer!")
    print()


def render_map(state: GameState) -> None:
    """Draw the map, keeping unvisited locations mysterious."""
    print(Colors.paint("       YOUR EXPEDITION MAP", "96;1"))
    print("     " + "   ".join(str(column + 1) for column in range(BOARD_SIZE)))
    print("   +" + "---+" * BOARD_SIZE)

    for row in range(BOARD_SIZE):
        cells = []
        for column in range(BOARD_SIZE):
            position = (row, column)
            if position == state.player:
                symbol = Colors.paint("@", "97;1")
            elif position not in state.explored:
                symbol = Colors.paint("?", "90")
            else:
                symbol = Colors.paint(".", "94")
            cells.append(f" {symbol} ")
        print(f" {row + 1} |" + "|".join(cells) + "|")
        print("   +" + "---+" * BOARD_SIZE)

    print("   @ You   ? Unexplored   . Explored")
    print(
        f"   {Colors.paint('$', '93')} Coins: {state.coins_collected}   "
        f"{Colors.paint('^', '91')} Traps: beware   "
        f"{Colors.paint('*', '95')} Treasure: hidden"
    )
    print()
    print(
        f"   Score: {state.score:>3}   "
        f"Lives: {Colors.paint('♥' * state.lives, '91;1')}"
        f"{Colors.paint('♡' * (MAX_LIVES - state.lives), '90')}   "
        f"Moves left: {state.moves_left}"
    )
    print()


def get_move() -> str:
    """Read and validate a movement key without consuming a move."""
    valid_moves = {"w", "a", "s", "d"}
    while True:
        choice = input(Colors.paint("Your move [W/A/S/D]: ", "96;1")).strip().lower()
        if choice in valid_moves:
            return choice
        print(Colors.paint("Please enter W, A, S, or D.", "93"))


def move_player(state: GameState, direction: str) -> str:
    """Move one tile, applying any item effect and returning a message."""
    row, column = state.player
    offsets = {"w": (-1, 0), "a": (0, -1), "s": (1, 0), "d": (0, 1)}
    row_offset, column_offset = offsets[direction]
    destination = (row + row_offset, column + column_offset)

    if not (0 <= destination[0] < BOARD_SIZE and 0 <= destination[1] < BOARD_SIZE):
        return Colors.paint("The edge of the map blocks your way. Try another direction!", "93")

    state.player = destination
    state.explored.add(destination)
    state.moves_left -= 1

    if destination in state.coins:
        state.coins.remove(destination)
        state.coins_collected += 1
        state.score += COIN_POINTS
        return Colors.paint(f"Coin collected! +{COIN_POINTS} points.", "93;1")

    if destination in state.traps:
        state.traps.remove(destination)
        state.lives -= 1
        return Colors.paint("Trap! You lose a life, but the path is now clear.", "91;1")

    if destination == state.treasure:
        state.treasure_found = True
        state.score += TREASURE_BONUS
        return Colors.paint(f"Treasure found! +{TREASURE_BONUS} bonus points!", "95;1")

    return Colors.paint("The path is quiet. Keep exploring!", "94")


def get_rank(score: int) -> str:
    """Return the explorer's rank for their final score."""
    if score >= 150:
        return "NEON LEGEND"
    if score >= 100:
        return "TREASURE MASTER"
    if score >= 50:
        return "GOLDEN EXPLORER"
    return "BRAVE ROOKIE"


def show_result(state: GameState) -> None:
    clear_screen()
    if state.treasure_found:
        print(Colors.paint(r"""
 __   __ _____ _____ ___  ____  ___  ____
 \ \ / /| ____/ ____/ _ \|  _ \|_ _|/ ___|
  \ V / |  _|| |   | | | | |_) || | \___ \
   | |  | |__| |___| |_| |  _ < | |  ___) |
   |_|  |_____\_____\___/|_| \_\___||____/
""", "92;1"))
        print(Colors.paint("THE TREASURE IS YOURS!", "93;1"))
    else:
        print(Colors.paint(r"""
   ____ _____ _____   ___  _____ _____
  / ___| ____/ _ \ \ / / | ____|  _ \
 | |  _|  _|| | | \ V /| |  _| | |_) |
 | |_| | |__| |_| || | | | |___|  _ <
  \____|_____\___/ |_| |_|_____|_| \_\
""", "91;1"))
        if state.lives == 0:
            print("Your expedition ran out of lives.")
        else:
            print("Your 20 moves are up. The treasure remains hidden...")

    print()
    print(f"Final score: {state.score}")
    print(f"Coins collected: {state.coins_collected}/{COIN_COUNT}")
    print(f"Explorer rank: {Colors.paint(get_rank(state.score), '96;1')}")
    print()


def play_round() -> None:
    state = create_game()
    message = "A new expedition begins. Choose your first move!"

    while state.lives > 0 and state.moves_left > 0 and not state.treasure_found:
        clear_screen()
        render_map(state)
        print(message)
        direction = get_move()
        message = move_player(state, direction)

    show_result(state)


def ask_to_play_again() -> bool:
    """Ask for a valid yes/no response."""
    while True:
        answer = input("Play again? [Y/N]: ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter Y or N.")


def main() -> None:
    show_welcome()
    while True:
        play_round()
        if not ask_to_play_again():
            print(Colors.paint("Thanks for playing NEON QUEST. See you next time!", "96"))
            break


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nExpedition ended. Thanks for playing NEON QUEST!")
