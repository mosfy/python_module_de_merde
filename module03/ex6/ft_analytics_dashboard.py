
def listComprension() -> None:
    print("=== List Comprehension Examples ===")
    players = ["alice", "bob", "charlie", "diana"]
    scores = [2300, 1800, 2150, 2050]
    recentPlays = [2, 5, 4, 67]

    high_scorers = []
    i = 0
    for player in players:
        if scores[i] > 2000:
            high_scorers.append(player)
        i += 1

    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [score * 2 for score in scores]
    print(f"Scores doubled: {scores_doubled}")

    active_players = []
    i = 0
    for player in players:
        if recentPlays[i] < 30:
            active_players.append(player)
        i += 1
    print(f"Active players: {active_players}")


def dictComprehension():
    print("=== Dict Comprehension Examples ===")
    players = [{"name": "alice", "score": 2300, "achivement": 5},
               {"name": "bob", "score": 1800, "achivement": 3},
               {"name": "charlie", "score": 2150, "achivement": 7}]
    player_scores = {player['name']: player['score'] for player in players}
    print("Player scores: ", player_scores)
    score_categorie = {
        "high": sum(1 for player in players if player['score'] >= 2200),
        "medium": sum(
            1 for player in players if 1900 <= player['score'] < 2200
        ),
        "low": sum(1 for player in players if player['score'] < 1900)
    }
    print("Score categories: ", score_categorie)
    achievement_counts = {
        player['name']: player['achivement'] for player in players
    }
    print("Achievement counts: ", achievement_counts)


def setComprehension():
    print("=== Set Comprehension Examples ===")
    players = [{"name": "alice(goat)", "region": "north",
                "achivement": ["god_slayer"]},
               {"name": "bob", "region": "central",
                "achivement": ["first_kill"]},
               {"name": "charlie", "region": "east",
                "achivement": ["first_kill", "level_10", "boss_slayer"]},
               {"name": "diana", "region": "east", "achivement": []}]

    unique_players = {player['name'] for player in players}
    print(f"Unique players :{unique_players}")
    unique_achievements = {achievement for player in players for achievement in
                           player['achivement']}
    print(f"Unique achievements :{unique_achievements}")
    active_region = {player['region'] for player in players}
    print(f"Active region :{active_region}")


def combined_analysis():
    players = [{"name": "alice", "region": "north", "score": 2300,
                "achivement": ["god_slayer", "a", "b", "c", "d"]},
               {"name": "bob", "region": "central", "score": 1800,
                "achivement": ["first_kill"]},
               {"name": "charlie", "region": "east", "score": 2150,
                "achivement": ["first_kill", "level_10", "boss_slayer"]},
               {"name": "diana", "region": "east", "score": 2050,
                "achivement": ["e", "f", "g", "h",]}]
    nbr_players = len({player['name'] for player in players})
    print(f"Total players :{nbr_players}")
    nbr_achievements = len({achievement for player in players for achievement
                           in player['achivement']})
    print(f"Total unique achievements:{nbr_achievements}")
    avr_score = sum(player['score'] for player in players) / nbr_players
    print(f"Average score: {avr_score}")
    top_player = max(players, key=lambda player: player["score"])
    print(
        f"Top performer: {top_player['name']} "
        f"({top_player['score']} points, "
        f"{len(top_player['achievement'])} achievements)"
    )

if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    listComprension()
    print()
    dictComprehension()
    print()
    setComprehension()
    print()
    combined_analysis()

