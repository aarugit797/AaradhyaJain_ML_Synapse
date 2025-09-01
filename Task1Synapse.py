import itertools as it

Pokedex = {
    "Pikachu" : ("Electric",),
    "Charizard": ("Fire", "Flying"),
    "Lapras": ("Water", "Ice"),
    "Machamp": ("Fighting",),
    "Mewtwo": ("Psychic", "Fighting"),
    "Hoopa": ("Psychic", "Ghost", "Dark"),
    "Lugia": ("Psychic", "Flying", "Water"),
    "Squirtle": ("Water",),
    "Gengar": ("Ghost", "Poison"),
    "Onix": ("Rock", "Ground")
}

def check(k):
    if k > 10:
        raise Exception("Invalid team size")   
    else:
        return "Valid team size"               

try:
    k = int(input("Enter the size of the team: "))
    print(check(k))
except Exception as e:
    print("Error:", e)

combi = list(it.combinations(Pokedex, k))

def team_members(team, Pokedex):
    types = set()
    for p in team:
        for t in Pokedex[p]:
            types.add(t)
    return len(types)

best = []
max_types = 0
for team in combi:
    score = team_members(team, Pokedex)
    if score > max_types:
        max_types = score
        best = [team]
    elif score == max_types:
        best.append(team)

print(best)
