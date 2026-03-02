alice_achievements = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
bob_achievements = {"first_kill", "level_10", "boss_slayer", "collector"}
charlie_achievements = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}

print("=== Achievement Tracker System ===")
print(f"Player alice achievements: {alice_achievements}")
print(f"Player bob achievements: {bob_achievements}")
print(f"Player charlie achievements: {charlie_achievements}")

all_achievements = alice_achievements.union(bob_achievements).union(charlie_achievements)
print("=== Achievement Analytics ===")
print(f"All unique achievements: {all_achievements}")
print(f"Total unique achievements: {len(all_achievements)}")

common_to_all = alice_achievements.intersection(bob_achievements).intersection(charlie_achievements)
print(f"Common to all players: {common_to_all}")

rare_achievements = set()
for achievement in all_achievements:
    count = sum([
        achievement in alice_achievements,
        achievement in bob_achievements,
        achievement in charlie_achievements
    ])
    if count == 1:
        rare_achievements.add(achievement)
print(f"Rare achievements (1 player): {rare_achievements}")

alice_vs_bob_common = alice_achievements.intersection(bob_achievements)
alice_unique = alice_achievements.difference(bob_achievements)
bob_unique = bob_achievements.difference(alice_achievements)

print(f"Alice vs Bob common: {alice_vs_bob_common}")
print(f"Alice unique: {alice_unique}")
print(f"Bob unique: {bob_unique}")
