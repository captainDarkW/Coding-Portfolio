import time
import random

class Player:
    def __init__(self, name, health, strength, money):
        self.name = name
        self.health = health
        self.strength = strength
        self.money = money
        self.inventory = []
        self.GAMEOVER = False

    def attack(self, enemy):
        print(f"You attack the {enemy.name} for {self.strength} damage!")
        enemy.health -= self.strength

    def talk(self, enemy):
        print(f"You try to talk to the {enemy.name}...")
        # 10% chance to befriend the dragon and win
        if enemy.name.lower() == "dragon" and random.random() < 0.1:
            print("The dragon looks at you, smiles, and says: 'You are a true friend.'")
            print("You and the dragon become friends and escape the dungeon together!")
            self.GAMEOVER = True
            self.friend_with_dragon = True
            return
        if random.random() > 0.5:
            print(f"The {enemy.name} is moved by your words and leaves you alone!")
            enemy.health = 0
        else:
            print(f"The {enemy.name} ignores you.")

    def pray(self):
        print("You pray for strength...")
        heal = random.randint(5, 15)
        self.health += heal
        print(f"You feel renewed and gain {heal} health!")

class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, player):
        print(f"The {self.name} attacks you for {self.strength} damage!")
        player.health -= self.strength

class Room:
    def __init__(self, description, treasure, pickup, enemy=None):
        self.description = description
        self.treasure = treasure
        self.pickup = pickup
        self.enemy = enemy

def win_screen(player):
    if hasattr(player, 'has_bomb') and player.has_bomb:
        print("\nAs you step out of the dungeon, the suspicious box in your backpack suddenly explodes!")
        print("You have been blown up by a bomb. Game Over!")
        return
    if hasattr(player, 'friend_with_dragon') and player.friend_with_dragon:
        print("\nCongratulations! You and the dragon are now best friends and leave the dungeon together!")
        print(f"Health: {player.health}")
        print(f"Money: {player.money}")
        print(f"Inventory: {player.inventory}")
        print("You win!")
    else:
        print("\nCongratulations! You have escaped the dungeon with:")
        print(f"Health: {player.health}")
        print(f"Money: {player.money}")
        print(f"Inventory: {player.inventory}")
        print("You win!")

def lose_screen():
    print("\nYou have fallen in the dungeon. Game Over.")

# Game setup
player = Player("St. George", 50, 10, 0)
rooms = [
    Room("A golden flask filled with cookies. You are in a medieval room spray-painted pink with windows, desks, chairs, puppies, pigs, and bones on the floor.", "golden flask", "cookies", Enemy("Dragon", 30, 15)),
    Room("A dark hallway with flickering torches. There is a shiny coin on the ground.", "shiny coin", "coin"),
    Room("A suspicious alcove with a strange ticking box on a pedestal.", None, "suspicious box"),  # <-- Add this line
    Room("A chapel with stained glass windows. You feel a peaceful presence.", "holy relic", "relic")
]

current_room = 0

print("You enter a dungeon.")
time.sleep(1)

while not player.GAMEOVER and current_room < len(rooms):
    room = rooms[current_room]
    print(f"\n{room.description}")
    time.sleep(1)

    # Pickup
    choice = input(f"Would you like to pick up the {room.pickup}? (y/n): ").lower()
    if choice == "y":
        player.inventory.append(room.pickup)
        print(f"You picked up the {room.pickup}!")
        if room.pickup == "suspicious box":
            player.has_bomb = True  # <-- Add this line

    # Treasure
    if room.treasure and room.treasure not in player.inventory:
        print(f"You found a {room.treasure}!")
        player.inventory.append(room.treasure)
        if room.treasure == "shiny coin":
            player.money += 10

    # Enemy encounter
    if room.enemy and room.enemy.health > 0:
        print(f"A wild {room.enemy.name} appears!")
        while room.enemy.health > 0 and player.health > 0 and not player.GAMEOVER:
            print(f"\nYour health: {player.health} | {room.enemy.name} health: {room.enemy.health}")
            action = input("Choose an action: [1] Attack [2] Talk [3] Pray: ")
            if action == "1":
                player.attack(room.enemy)
                if room.enemy.health > 0:
                    room.enemy.attack(player)
            elif action == "2":
                player.talk(room.enemy)
                if getattr(player, 'friend_with_dragon', False):
                    win_screen(player)
                    exit()
                if room.enemy.health > 0:
                    room.enemy.attack(player)
            elif action == "3":
                player.pray()
                room.enemy.attack(player)
            else:
                print("Invalid action.")
            time.sleep(1)
            if player.health <= 0:
                player.GAMEOVER = True
                break
            elif not getattr(player, 'friend_with_dragon', False) and room.enemy.health <= 0:
                print(f"You defeated the {room.enemy.name}!")

    current_room += 1

if player.health > 0 and not player.GAMEOVER:
    win_screen(player)
else:
    # Only show lose screen if not friend with dragon
    if not getattr(player, 'friend_with_dragon', False):
        lose_screen()
