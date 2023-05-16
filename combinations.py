import itertools

def generate_possible_combinations(characters, length):
    combinations = []
    for r in range(1, length + 1):
        combinations.extend(itertools.product(characters, repeat=r))
    return combinations

# Example usage
characters = input("Enter the characters: ")
length = int(input("Enter the length of the password: "))
All_Possible_combinations = generate_possible_combinations(characters, length)
print("All possible combinations:")
for combination in All_Possible_combinations:
    print("".join(combination))
