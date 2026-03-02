import sys

print("=== Command Quest ===")

args = sys.argv
total_args = len(args)

if total_args == 1:
    print("No arguments provided!")
    print(f"Program name: {args[0]}")
else:
    print(f"Program name: {args[0]}")
    print(f"Arguments received: {total_args - 1}")

    index = 1
    while index < total_args:
        print(f"Argument {index}: {args[index]}")
        index += 1

print(f"Total arguments: {total_args}")
