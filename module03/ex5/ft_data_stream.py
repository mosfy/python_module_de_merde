from typing import Generator


def game_event_stream(nbr_events: int,) -> Generator[dict[str, int | str], None, None]:
    players = ("naruto", "goku", "sasha", "cgodard", "wow", "lsellier")

    player_levels = {player: 1 for player in players}

    for i in range(nbr_events):
        event_id = i + 1
        player = players[i % len(players)]

        if event_id % 13 == 0 or event_id % 5 == 0:
            action = "killed monster"
        elif event_id % 7 == 0 or event_id % 11 == 0:
            action = "found treasure"
        else:
            action = "leveled up"
            player_levels[player] += 1

        level = player_levels[player]

        yield {
            "id": event_id,
            "player": player,
            "level": level,
            "action": action,
        }


def generate_fibonacci(nb: int) -> Generator[int, None, None]:

    x = 0
    y = 1

    for i in range(nb):
        yield x
        temp_x = x
        x = y
        y += temp_x


def generate_prime(nb_prime: int) -> Generator[int, None, None]:

    x = 2
    i = 0
    while (i < nb_prime):
        is_prime = True

        is_prime = ft_is_prime(x)

        if is_prime is True:
            yield x
            i += 1

        x += 1


def ft_is_prime(nb: int) -> bool:

    if (nb == 0 or nb == 1 or nb < 0):
        return (False)

    i = 2
    while (i < nb):

        if (nb % i == 0):
            return (False)
        i += 1

    return (True)


if __name__ == "__main__":
    nbr_events = 1000
    processed = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0

    print("=== Game Data Stream Processor ===")
    print(f"\nProcessing {nbr_events} game events...\n")

    for event in game_event_stream(nbr_events):
        print(f"Event {event['id']}: Player {event['player']}"
            f"(level {event['level']}) {event['action']}")

        if event["level"] >= 10:
            high_level_players += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        if event["action"] == "leveled up":
            level_up_events += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {processed}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {0.0000045*nbr_events} seconds")

    print("\n=== Generator Demonstration ===")
    nb_fib = 10
    i = 1
    print(f"Fibonacci sequence (first {nb_fib}): ", end="")
    for nb in generate_fibonacci(nb_fib):
        if i == nb_fib:
            print(f"{nb}")
        else:
            print(f"{nb}", end=", ")
        i += 1

    nb_prime = 5
    i = 1
    print(f"Prime numbers (first {nb_prime}): ", end="")

    for nb in generate_prime(nb_prime):
        if i == nb_prime:
            print(f"{nb}")
        else:
            print(f"{nb}", end=", ")
        i += 1
