# Define regions
regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']

# Define neighbouring regions
neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

# Available colours
colors = ['Red', 'Green', 'Blue']

# Dictionary to store assigned colours
solution = {}

# CHECK IF COLOUR IS SAFE

def is_safe(region, color):
    for neighbor in neighbors[region]:
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True

# BACKTRACKING ALGORITHM

def solve(index=0):

    # If all regions assigned
    if index == len(regions):
        return True

    region = regions[index]

    for color in colors:

        if is_safe(region, color):
            solution[region] = color

            if solve(index + 1):
                return True

            # Backtrack
            del solution[region]

    return False

# RUN PROGRAM

if solve():
    print("Australia Map Colouring Solution:\n")

    for region in solution:
        print(region, "->", solution[region])
else:
    print("No solution found")



#Colouring Nairobi subcounties


sub_counties = [
    'Westlands',
    'Dagoretti North',
    'Dagoretti South',
    'Langata',
    'Kibra',
    'Roysambu',
    'Kasarani',
    'Ruaraka',
    'Embakasi South',
    'Embakasi North',
    'Embakasi Central',
    'Embakasi East',
    'Embakasi West',
    'Makadara',
    'Kamukunji',
    'Starehe',
    'Mathare'
]

# Adjacency relationships
neighbors = {
    'Westlands': ['Dagoretti North', 'Starehe', 'Roysambu'],
    'Dagoretti North': ['Westlands', 'Dagoretti South', 'Kibra'],
    'Dagoretti South': ['Dagoretti North', 'Langata'],
    'Langata': ['Dagoretti South', 'Kibra', 'Embakasi South'],
    'Kibra': ['Langata', 'Dagoretti North', 'Starehe'],
    'Roysambu': ['Westlands', 'Kasarani', 'Ruaraka'],
    'Kasarani': ['Roysambu', 'Ruaraka', 'Embakasi North', 'Mathare'],
    'Ruaraka': ['Roysambu', 'Kasarani', 'Mathare', 'Starehe'],
    'Embakasi South': ['Langata', 'Embakasi West'],
    'Embakasi North': ['Kasarani', 'Embakasi Central'],
    'Embakasi Central': ['Embakasi North', 'Embakasi East', 'Embakasi West'],
    'Embakasi East': ['Embakasi Central', 'Makadara'],
    'Embakasi West': ['Embakasi South', 'Embakasi Central', 'Makadara'],
    'Makadara': ['Embakasi East', 'Embakasi West', 'Kamukunji'],
    'Kamukunji': ['Makadara', 'Starehe'],
    'Starehe': ['Westlands', 'Kibra', 'Kamukunji', 'Mathare'],
    'Mathare': ['Kasarani', 'Ruaraka', 'Starehe']
}

# Least possible colours
colors = ['Red', 'Green', 'Blue']

solution = {}

# CHECK VALIDITY

def is_safe(area, color):
    for neighbor in neighbors[area]:
        if neighbor in solution and solution[neighbor] == color:
            return False
    return True

# BACKTRACKING SEARCH
def solve(index=0):

    if index == len(sub_counties):
        return True

    area = sub_counties[index]

    for color in colors:

        if is_safe(area, color):
            solution[area] = color

            if solve(index + 1):
                return True

            del solution[area]

    return False

# EXECUTE PROGRAM

if solve():
    print("\nNairobi Sub-County Colouring Solution:\n")

    for area in solution:
        print(area, "->", solution[area])
else:
    print("No solution found")
