import re

# Input flag
flag = "Qf1x3DIOW{7s3_k4i7b_m3e3i_3mw$}"

# Extract content inside the braces
pattern = r"\{(.+)\}"
match = re.search(pattern, flag)
if not match:
    print("No valid flag pattern found.")
    exit()

leet_text = match.group(1)

# Leetspeak conversion table
leet_dict = {
    '4': ['A'],
    '3': ['E'],
    '1': ['I', 'L'],
    '7': ['T', 'L'],
    '0': ['O'],
    '$': ['S'],
    '5': ['S'],
    '@': ['A'],
    '!': ['I'],
}

def leet_translate(text):
    """Generate all possible translations of leetspeak words."""
    from itertools import product

    chars = []
    for char in text:
        if char in leet_dict:
            chars.append(leet_dict[char])
        else:
            chars.append([char])

    # Cartesian product of all substitutions
    possibilities = [''.join(candidate) for candidate in product(*chars)]
    return possibilities

# Process each word separately
words = leet_text.split("_")
translated_candidates = [leet_translate(word) for word in words]

# Combine word permutations into possible full sentences
from itertools import product
combinations = list(product(*translated_candidates))

print(f"\n[*] Possible decoded outputs ({len(combinations)} candidates):\n")
for combo in combinations:
    print(" ".join(combo))
