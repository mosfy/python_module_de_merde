import sys

scores = []

print("=== Player Score Analytics ===")
if len(sys.argv) == 1:
    print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    sys.exit(0)

for arg in sys.argv[1:]:
    try:
        scores.append(int(arg))
    except ValueError:
        print("Invalid score:", arg)
        sys.exit(0)
        
if len(scores) == 0:
    print("No valid scores to analyze.")
    sys.exit(0)
 
total = sum(scores)
maximum = max(scores)
minimum = min(scores)
average = total / len(scores)

print(f"Scores processed: {scores}")
print(f"Total players: {len(scores)}")
print(f"Total score: {total}")
print(f"Average score: {average:.2f}")
print(f"High score: {maximum}")
print(f"Low score: {minimum}")
print(f"Score range: {maximum - minimum}")
