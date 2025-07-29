heroes = ['Ironman', 'Thor', 'Hulk', 'Spidermain']
def print_heroes(heroes_list):
    for hero in heroes_list:
        print(hero)
print()

def add_hero(heroes_list, AntMan):
    heroes_list.append(AntMan)
    print(f'Added hero: {AntMan}')
    return heroes_list

def insert_hero(heroes_list, CaptainAmerica, index):
    heroes_list.insert(index, CaptainAmerica)
    print(f'Inserted hero: {CaptainAmerica} at index {index}')
    return heroes_list

def remove_hero(heroes_list, Thor):
    if Thor in heroes_list:
        heroes_list.remove(Thor)
        print(f'Removed hero: {Thor}')
    else:
        print(f'Hero {Thor} not found in the list.')