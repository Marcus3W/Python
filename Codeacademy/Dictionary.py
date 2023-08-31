

translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}


# Below will result in Type error as its got a list for the key (["Sonny", "Fredo", "Michael"]: "Corleone")
# children = {["Johannes", "Rosmarie", "Eleonore"]: "von Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"}

# Fixed
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone" :["Sonny", "Fredo", "Michael"]}


# Empty Dictionary
# animals_in_zoo = {}

animals_in_zoo = {"zebras": 8, "monkeys": 12, "dinosaurs": 0}
#print(animals_in_zoo)


# Add Multiple Keys - using .update() method
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper": 138475, "stringQueen": 85739})
#print(user_ids)


# Overwrite Values
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

# Dict Comprehensions
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}


# Review

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key:value for key, value in zip(songs, playcounts)}
#print(plays)
plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
#print(plays)

library = {"The Best Songs": plays, "Sunday Feelings": {}}
#print(library)


#  Creating a dictionary using a list comprehension
conference_rooms = ["executive", "hopper", "lovelace", "pod", "snooze booth"]
capacity = [7, 20, 6, 2, 1]
room_dict = {key:value for key, value in zip(conference_rooms, capacity)}

#print(room_dict)



# POP
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

check = "stamina grains"

if check in available_items:
  health_points += available_items["stamina grains"]
  available_items.pop("stamina grains")


# Get All Items
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

#for occupation, percentage in pct_women_in_occupation.items():
  #print("Women make up " + str(percentage) + " percent of " + occupation + "s.")

# Review

#tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

#spread = {}
#spread["past"] = tarot.pop(13)
#spread["present"] = tarot.pop(22)
#spread["future"] = tarot.pop(10)

#for key, value in spread.items():
  #print("Your " + key + " is the " + value + " card.")


# PROJECT

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_word("BROWNIE")

print(letter_to_points)
print(brownie_points)

player_to_words = {
    'player1': ['BLUE', 'TENNIS', 'EXIT'],
    'wordNerd': ['EARTH', 'EYES', 'MACHINE'],
    'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],
    'Prof Reader': ['ZAP', 'COMA','PERIOD']
}
player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)
