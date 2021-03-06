'''
def delete_starting_evens(lst):
  while len(lst) > 0 and lst[0] % 2 == 0:
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

lst = [1,2,3]
print(lst)
#print(lst(0))
print(lst.index(1))
sum_lst = sum(lst)
print(f"Sum: {sum_lst}")
def odd_indices(lst):
  odd_lst =[]
  for idx in range(1,len(lst),2):
      odd_lst.append(lst[idx])
  return odd_lst
#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

def larger_sum(lst1, lst2):
  if sum(lst2) > sum(lst1):
    return lst2
  else:
    return lst1
#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

lst1 = [1, 9, 5]
lst2 = [2, 3, 7]

lst3 = [lst1 if sum(lst1) >= sum(lst2) else lst2 for x in range(1)]
print(lst3)

lst = [8000, 900, 120, 5000]
limit = 9000
new_lst = []
i = 0
while sum(new_lst) < limit:
    new_lst.append(lst[i])
    i += 1
    sum(new_lst)

print(sum(new_lst))

def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum
print(over_nine_thousand([8000, 900, 120, 5000]))

def same_values(lst1, lst2):
  new_list = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_list.append(index)
  return new_list

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

lst1 = [1,2,3]
lst2 = [3,2,1]
list.reverse(lst2)
if lst1 == lst2:
  print(True)
else: print(False)

# square_root function
def square_root(num):
  return (num**0.5)
print(square_root(16))
print(square_root(100))

# remainder function
def remainder(num1, num2):
  return (2*num1) % (num2/2)
print(remainder(15, 14))
print(remainder(9, 6))

# int in print string:
def dog_years(name, age):
  dog_age = age * 7
  return (name + ", you are " + str(dog_age) + " years old in dog years")
print(dog_years("Lola", 16))
print(dog_years("Baby", 0))

project: The Boredless Tourist
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "S??o Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

attractions = [[] for lst in destinations]

def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index].append(attraction)

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("S??o Paulo, Brazil", ["S??o Paulo Zoo", ["zoo"]])
add_attraction("S??o Paulo, Brazil", ["P??tio do Col??gio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
  for i in range(len(traveler_attractions)):
    if traveler_attractions[-1] == traveler_attractions[i]:
      interests_string += "the "+ traveler_attractions[i] + "."
    else:
      interests_string += "the "+ traveler_attractions[i] + ","
  return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)

first_name = "Reiko"
last_name = "Matsuki"

#def password_generator(first_name, last_name):

string_one = first_name[len(first_name)-3:]
  

string_two = last_name[len(last_name)-3:]
new_password = string_one + string_two
print(new_password)


Liste1 = ["1:2:3", "4:5:6"]
print(Liste1)
i = 0
Liste2 = []
for i in range(len(Liste1)):
  detail = Liste1[i].split(':')
  Liste2.append(detail)

print(Liste2[0][0])

titles = []
poets = []
dates = []
i = 0

for i in range(len(Liste2)):
  title = Liste2[i][0]
  titles.append(title)
  poet = Liste2[i][1]
  poets.append(poet)
  date = Liste2[i][2]
  dates.append(date)

i = 0
for i in range(len(titles)):
  print("The poem {TITLE} was published by {POET} in {DATE}.".format(TITLE = titles[i], POET = poets[i], DATE = dates[i]))
'''
'''  
daily_sales = \
"""Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
;,;   $5.13   ;,; white   ;,; 09/15/17,
Eduardo George   ;,;$20.39;,; white&yellow 
;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
purple&yellow ;,;09/15/17,   Shaun Brock;,; 
$17.98;,;purple&yellow ;,; 09/15/17 , 
Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
$8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
Israel Cummings;,;   $11.86   ;,;black;,;  
09/15/17,   June Doyle   ;,;   $22.29 ;,;  
black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
$8.35;,;   white&black&yellow   ;,;   09/15/17,   
Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
;,; 09/15/17   ,Hubert Miles;,;   $3.59   
;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
black   ;,;   09/15/17 , Audrey Ferguson ;,; 
$5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
$17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
$14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
$8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
09/15/17 , Melody Moran ;,;   $30.84   
;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
$12.31 ;,; green&yellow&black;,;   09/15/17 ,
Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
white&yellow&black ;,;09/15/17   ,   Dale Brady   
;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
09/15/17, Angelica Garza;,;$11.60;,;white&black   
;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
white&black&red ;,;09/15/17   ,   Rex Hudson   
;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
green&purple&yellow ;,;09/15/17   ,Stanley Holland 
;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
green&red ;,;   09/15/17   ,Irving Patterson 
;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
, Beatrice Newman ;,;$22.45   ;,;white&purple&red 
;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
black&red;,; 09/15/17,   Javier Bailey   ;,;   
$24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
,   Traci Craig ;,;$0.65;,; green&yellow;,; 
09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
Leonard Guerrero ;,;   $1.86   ;,;yellow  
;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
09/15/17   ,Donna Ball ;,; $28.10  ;,; 
yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
$9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
$16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
green&yellow;,;09/15/17,Malcolm Morales ;,;   
$24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
, Leticia Manning;,;$15.70 ;,; green&purple;,; 
09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
09/15/17,Lewis Glover;,;   $13.66   ;,;   
green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

daily_sales_replaced = daily_sales.replace(";,;", "|")

daily_transactions = daily_sales_replaced.split(",")

daily_transactions_split = []
i = 0
for str in daily_transactions:
  str = daily_transactions[i].split("|")
  daily_transactions_split.append(str)
  i += 1

transactions_clean = []
i = 0
for list in range(len(daily_transactions_split)):
  clean = []
  j= 0
  for item in range(len(daily_transactions_split[i])):
    list = daily_transactions_split[i][j].strip()
    j += 1
    clean.append(list)
  i+=1
  transactions_clean.append(clean)  

customers = []
sales = []
thread_sold = []
i = 0
for data in range(len(transactions_clean)):
  customers.append(transactions_clean[i][0])
  sales.append(transactions_clean[i][1])
  thread_sold.append(transactions_clean[i][2])
  i += 1
  
total_sales = 0
i = 0
for i in range(len(sales)):
  value = sales[i].strip("$")
  sales[i] = float(value)
  total_sales += sales[i]
  i += 1

thread_sold_split = []
i = 0
for thread in range(len(thread_sold)):
  if thread_sold[i].find("&") == -1:
    thread_sold_split.append(thread_sold[i])
  else:
    j = 0
    thread_split = thread_sold[i].split("&")
    for split in range(len(thread_split)):
      thread_sold_split.append(thread_split[j])
      j += 1
  i += 1

def color_count(color):
  i = 0
  counter = 0
  for i in range(len(thread_sold_split)):
    if color == thread_sold_split[i]:
      counter += 1
  return counter

colors = ['red','yellow','green','white','black','blue','purple']
quantity = []
for color in colors:
  count = color_count(color)
  threads_sold = "We sold {1} pcs. of {0} thread today."
  print(threads_sold.format(color, count))

total_sales = "{:.2f}".format(total_sales)
print(f"We made a total revenue of: $ {total_sales} today.")


from datetime import datetime

birthday = datetime(1973, 11, 6, 16, 45, 15)
print(birthday)
print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.day) # Weekday ... 1 = Monday to 7 = Sunday

current_time = datetime.now()
print(current_time)

datediff = datetime.now() - datetime(2021, 1, 1)
print(datediff)

#read date from string and parse to date (formatted string values for
# strptime see docs.pyhton.org)
user_input_date = 'Jan 15, 2021'
parsed_date = datetime.strptime(user_input_date, '%b %d, %Y') 
print(parsed_date)
print(parsed_date.day)
print(parsed_date.month)
print(parsed_date.year)

#read date and parse to string
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)

# dictionaries
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}
print(sensors)
sensors["bathroom"] = 26
print(sensors)
sensors.update({"garage" : 16, "basement" : 19})
print(sensors)
sensors["basement"] = 20
print(sensors)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}
print(drinks_to_caffeine)

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key : value for key, value in zip(songs, playcounts)}

print(plays)

plays["Purple Haze"] = 1

plays["Respect"] = 94

library = {"The Best Songs" : plays, "Sunday Feelings" : {}}
print(library)

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
#caffeine_level["matcha"] = 30
try:
  print(caffeine_level["matcha"])
except KeyError:
  print("Unknown Caffeine Level")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for item in num_exercises.values():
  total_exercises += item

print(total_exercises)

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, value in pct_women_in_occupation.items():
  print("Women make up " + str(value) + " percent of " + occupation + "s.")


tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print("Your " + key + " is the " + value + " card.")

oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
for element in oscars.values():
  print(element)

#combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
#print(combo_meals[3])

raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
raffle.pop(561721, "No Value")
print(raffle)

combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
print(combo_meals.get(3, ["hamburger", "fries"]))

oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
for element in oscars:
  print(element)

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
print(12 in inventory)

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
print("the peacemaker" in inventory)

# Scrabble
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

all_letters = []
for letter in letters:
  all_letters.append(letter.lower())
letters += all_letters
points += points

letter_to_points = dict(zip(letters, points))
letter_to_points[" "] = 0

player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "wordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

def play_word(player, word):
  for players, words in player_to_words.items():
      if player == players:
        words.append(word)
  return player_to_words

def score_word(word):
  point_total = 0
  for letter in word:
    if letter in letters:
      point_total += letter_to_points[letter]
    else:
      point_total += 0
  return point_total

def update_point_totals():
  player_to_points = {}
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points

brownie_points = score_word("BROWNIE")
print(brownie_points)
brownie_points = score_word("brownie")
print(brownie_points)

updated_points = update_point_totals()
print(updated_points)
play_word("player1", "pYtHoN")
updated_points = update_point_totals()
print(updated_points)

# Data-Types
my_int = 5
print(type(my_int))

my_dict = {}
print(type(my_dict))

my_list = []
print(type(my_list))

# CLasses
class Facade: #defining a class
  pass # skips all following code in class (eg for developing purposes)
facade_1 = Facade() # Instantiation of "Object"_1 of Class (OOP)
facade_2 = Facade() # Object_2
print(type(facade_1))

class Dog:
  dog_time_dilation = 7
 
  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))
 
pipi_pitbull = Dog()
pipi_pitbull.time_explanation()

class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile
 
converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(f"5 miles equal {kms_in_5_miles} kilometers.")

class Circle:
  pi = 3.14
  def area(self, radius):
    area = self.pi * radius ** 2
    return area

circle = Circle()

pizza_diameter = 12
teaching_table_diameter = 36
round_room_diameter = 11460

pizza_radius = pizza_diameter/ 2
teaching_table_radius = teaching_table_diameter / 2
round_room_radius = round_room_diameter / 2

pizza_area = circle.area(pizza_radius)
teaching_table_area = circle.area(teaching_table_radius)
round_room_area = circle.area(round_room_radius)

print(pizza_area)
print(teaching_table_area)
print(round_room_area)

class Grade:
  minimum_passing = 65

# Class -> Constructor method
class Shouter:
  def __init__(self):
    print("HELLO?!")

shout1 = Shouter()
shout2 = Shouter()

class ShoutLoud:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:
 
      # then shout it out
      print(phrase.upper())
 
shout1 = ShoutLoud("shout")
# prints "SHOUT"
 
shout2 = ShoutLoud("shout")
# prints "SHOUT"
 
shout3 = ShoutLoud("let it all out")
# prints "LET IT ALL OUT"

class Circle:
  pi = 3.14
  
  # constructor:
  def __init__(self, diameter):
    print(f"New circle with diameter: {diameter}")

# call:
teaching_table = Circle(36)


# Instance Variables
class FakeDict:
  pass

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()
 
fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"
 
# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!"


class Store:
  pass
alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"

isabelles_ices.store_name = "Isabelle's Ices"

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for element in can_we_count_it:
  
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
    
  else:
    print(str(type(element)) + " does not have the count attribute :(")

#Constructors
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2

  def circumference(self):
    circumference = 2 * self.pi * self.radius
    return circumference

  def __repr__(self):
    return (f"Circle with radius {self.radius}")

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

print(medium_pizza) #prints out def __repr__
print(teaching_table)
print(round_room)

#dir
print(dir(5))
print("")

def this_function_is_an_object():
  return

print(dir(this_function_is_an_object))
'''
'''
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
 
  def print_grades(self):
    for grade in self.grades:
      print(f"{self.name}'s grade is {grade.score}")
    return 1

class Grade:
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score
    
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

pieter.add_grade(Grade(100))
pieter.add_grade(Grade(80))
pieter.add_grade(Grade(55))
roger.add_grade(Grade(60))
roger.add_grade(Grade(80))
roger.add_grade(Grade(95))

pieter.print_grades()
roger.print_grades()
'''
'''
Great job! You???ve created two classes and defined their interactions. This is object-oriented programming! From here you could:

Write a Grade method .is_passing() that returns whether a Grade 
has a passing .score.
Write a Student method get_average() that returns the student???s 
average score.
Add an instance variable to Student that is a dictionary 
called .attendance, with dates as keys and booleans as values 
that indicate whether the student attended school that day.
Write your own classes to do whatever logic you want!
'''
'''
# Define your exception up here:
class OutOfStock(Exception):
  pass

# Update the class below to raise OutOfStock
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):
    if self.stock[color] < 1:
      raise OutOfStock
      
    self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
try:
  candle_shop.buy('blue')
  candle_shop.buy('green')
except OutOfStock:
  for key, value in candle_shop.stock.items():
    if  value < 1:
      print(f"Color {key} is out of stock!")
      print(CandleShop.name)
'''
'''
#override class method
class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text
      
class Admin(User):
  def edit_message(self, message, new_text):
    message.text = new_text

#adding parameter to inherited constructor via super()
class PotatoSalad:
  print("Potatoe Salad:")
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions 

    print(f"Potatoes: {potatoes}")
    print(f"Celery: {celery}")
    print(f"Onions: {onions}")
    
class RaisinPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions, raisin):
    print("Potatoe Salad with raisins:")
    super().__init__(potatoes, celery, onions)
    self.raisin = raisin
    print(f"Raisins: {raisin}")

class EggPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions, eggs):
    print("Potatoe Salad with eggs:")
    super().__init__(potatoes, celery, onions)
    self.eggs = eggs
    eggs = potatoes * 2
    print(f"Eggs: {eggs}") 
    
PotatoSalad(5,2,3)
print("\n")
RaisinPotatoSalad(4,1,2,45)
print("\n")
EggPotatoSalad(3,1,3,0)

# Own Dunder Methods
class Atom:
  def __init__(self, label):
    self.label = label
    
  def __add__(self, other):
    return Molecule([self, other])
  
  def __repr__(self):
    return self.label
    
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms
  def __repr__(self):
    return (f"{salt.atoms[0].label}{salt.atoms[1].label}")

sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
newsalt = sodium + chlorine

print(salt)
print(newsalt)

class UserGroup:
  def __init__(self, users, permissions):
    self.user_list = users
    self.permissions = permissions
 
  def __iter__(self):
    return iter(self.user_list)
 
  def __len__(self):
    return len(self.user_list)
 
  def __contains__(self, user):
    return user in self.user_list

class User:
  def __init__(self, username):
    self.username = username
 
diana = User('diana')
frank = User('frank')
jenn = User('jenn')
 
can_edit = UserGroup([diana, frank], {'can_edit_page': True})
can_delete = UserGroup([diana, jenn, frank], {'can_delete_posts': True})
 
print(len(can_edit))
# Prints 2
 
for user in can_edit:
  print(user.username)
# Prints "diana" and "frank"
 
if frank in can_delete:
  print("Since when do we allow Frank to delete things? Does no one remember when he accidentally deleted the site?")
 

# working with classes
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

  def __repr__(self):
    return f'{self.name}, {self.franchises}'

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return f'Store: {self.address}'

  def available_menus(self, time):
    available_menu = []
    
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)

    return available_menu

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return f'Our {self.name}-Menu: available from {self.start_time} to {self.end_time}'

  def calculate_bill(self, purchased_items):
    total_price = 0.00
    for item in purchased_items:
      if item in self.items:
        total_price += self.items[item]
    return f'Your total is: {total_price}0 $'

brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu("Brunch", brunch_items, 1100, 1600)

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu("Early bird", early_bird_items,1500, 1800)

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu("Dinner", dinner_items, 1700, 2300)

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu("Kids", kids_items, 1100, 2100)

print(brunch_menu)
bill = brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"])
print(bill)
print(early_bird_menu)
bill = early_bird_menu.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"])
print(bill)
print("\n")

menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
print(flagship_store)
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))
print("\n")

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
print(f"All stores: {basta}")
print(f"No. 1 {basta.franchises[0]}")
print(f"No. 2 {basta.franchises[1]}")
print("\n")

# Creatin a new Business using all of the above classes:
arepa_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Main Menu", arepa_items, 1000, 2000)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)
arepa = Business("Take a' Arepa", arepas_place)
print(arepa)
print(arepa.franchises)
print(arepa.franchises.menus)
print(arepa.franchises.menus.items)
bill = arepas_menu.calculate_bill(["arepa pabellon", "guayanes arepa"])
print(bill)
print("\n")

# strings
import string
def unique_english_letters(word):
  i = 0
  letters = string.ascii_letters
  for letter in letters:
    if letter in word:
      i += 1
  return i

print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))

def count_char_x(word, x):
  i = 0
  for character in word:
    if character == x:
      i += 1
  return i

print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))

def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)
def count_multi_char_x_1(word, x):
  counts = word.count(x)
  return(counts)

print(count_multi_char_x_1("mississippi", "iss"))
print(count_multi_char_x_1("apple", "pp"))


def substring_between_letters(word, start, end):
  start = word.find(start)
  end = word.find(end)
  if start >= 0 and end >= 0:
    return (word[start +1:end])
  return word

print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))

def x_length_words(sentence, x):
  splitted = sentence.split()
  result = True
  i = 0
  for x in range(len(splitted)):
    if len(splitted[i]) < x:
      result = False
      i += 1
  return(result)
print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))

def x_length_words1(sentence, x):
  words = sentence.split(" ")
  for word in words:
    if len(word) < x:
      return False
  return True
print(x_length_words1("i like apples", 2))
print(x_length_words1("he likes apples", 2))

# strings advanced

def check_for_name(sentence, name):
  sentence = sentence.lower()
  name = name.lower()
  if name in sentence:
    return True
  return False

#better:
def check_for_name1(sentence, name):
  return name.lower() in sentence.lower()

print(check_for_name1("My name is Jamie", "Jamie"))
print(check_for_name1("My name is jamie", "Jamie"))
print(check_for_name1("My name is JAMIE", "Jamie"))

def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other
print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))

# or
def every_other_letter(word):
  letter = ""
  for character in word[::2]:
    letter += character
  return letter

print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))

def reverse_string(word):
  reverse_string = ""
  for character in word[::-1]:
    reverse_string += character
  return reverse_string

print(reverse_string("Codecademy"))
print(reverse_string("Hello world!"))

def reverse_string(word):
  reverse_string = ""
  for i in range(len(word) -1, 0 -1, -1):
    reverse_string += word[i]
  return reverse_string

print(reverse_string("Codecademy"))
print(reverse_string("Hello world!"))

# dictionaries
def sum_values(dictionary):
  sum = 0
  for val in dictionary.values():
    sum += val
  return sum
print(sum_values({"milk":5, "eggs":2, "flour": 3}))

def even_keys(dictionary):
  sum = 0
  for key, value in dictionary.items():
    if key % 2 == 0:
      sum += value
  return sum

print(even_keys({1:5, 2:2, 3:3}))
print(even_keys({10:1, 100:2, 1000:3}))

#or:
def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key%2 == 0:
      total += my_dictionary[key]
  return total
print(sum_even_keys({1:5, 2:2, 3:3}))
print(sum_even_keys({10:1, 100:2, 1000:3}))

def add_ten(dictionary):
  for key, value in dictionary.items():
    value += 10
    dictionary[key] = value
  return dictionary
print(add_ten({1:5, 2:2, 3:3}))
print(add_ten({10:1, 100:2, 1000:3}))

def values_that_are_keys(dictionary):
  values_found = []
  for value in dictionary.values():
    if value in dictionary.keys():
      values_found.append(value)
  return values_found
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))

def max_key(dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

print(max_key({1:100, 2:1, 3:4, 4:10}))
print(max_key({"a":100, "b":10, "c":1000}))

# dictionaries advanced
def word_length_dictionary(words):
  new_dictionary = {}
  for string in words:
    new_dictionary[string] = len(string) 
  return new_dictionary

print(word_length_dictionary(["apple", "dog", "cat"]))
print(word_length_dictionary(["a", ""]))

def frequency_dictionary(words):
  new_dictionary = {}
  
  for string in words:
    if string in new_dictionary.keys():
      new_dictionary[string] += 1
    else:
      new_dictionary[string] = 0
      new_dictionary[string] += 1
      
  return new_dictionary
print(frequency_dictionary(["apple", "apple", "cat", 1]))
print(frequency_dictionary([0,0,0,0,0]))

# better:
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
      freqs[word] = 0
    freqs[word] += 1
  return freqs
print(frequency_dictionary(["apple", "apple", "cat", 1]))
print(frequency_dictionary([0,0,0,0,0]))


def unique_values(dictionary):
  uniques = []
  for value in dictionary.values():
    if value not in uniques:
      uniques.append(value) 
  return len(uniques)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
print(unique_values({0:3, 1:3, 4:3, 5:3}))


def count_first_letter(names):
  letters = {}
  i = 0
  for key in names:
    lastname = list(names.keys())[i]
    length = len(list(names.values())[i])
    firstletter = lastname[0]    
    if firstletter not in letters:
      letters[firstletter] = 0
      letters[firstletter] += length
    else:
      letters[firstletter] += length
    i += 1
  return letters
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))

#better:
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))

# classes
class DriveBot:

  all_disabled = False
  latitude = -999999
  longitude = -999999
  robot_count = 0

  def __init__(self, motor_speed=0, direction=0, sensor_range=0, id = 0):
      self.motor_speed = motor_speed
      self.direction = direction
      self.sensor_range = sensor_range
      DriveBot.robot_count += 1
      self.id = DriveBot.robot_count
  
  def control_bot(self, new_speed, new_direction):
    self.motor_speed = new_speed
    self.direction = new_direction
  
  def adjust_sensor(self, new_sensor_range):
    self.sensor_range = new_sensor_range

DriveBot.longitude = 50.0
DriveBot.latitude = - 50.0
DriveBot.all_disabled = True  
  
robot_1 = DriveBot(5 , 90, 10)
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

robot_1.control_bot(10,180)
robot_1.adjust_sensor(20)
print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)

robot_2 = DriveBot(10, 270, 35)
robot_3 = DriveBot(50, 170, 55)
print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)
'''
# classes advanced
class Robot:
  all_disabled = False
  latitude = -999999
  longitude = -999999
  robot_count = 0

  def __init__(self, speed = 0, direction = 180, sensor_range = 10):
      self.speed = speed
      self.direction = direction
      self.sensor_range = sensor_range
      self.obstacle_found = False
      Robot.robot_count += 1
      self.id = Robot.robot_count

  def control_bot(self, new_speed, new_direction):
      self.speed = new_speed
      self.direction = new_direction

  def adjust_sensor(self, new_sensor_range):
      self.sensor_range = new_sensor_range

  def avoid_obstacles(self):
      if self.obstacle_found:
          self.direction = (self.direction + 180) % 360
          self.obstacle_found = False

class DriveBot(Robot):
    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        super().__init__(motor_speed, direction, sensor_range)

class WalkBot(Robot):
    def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length = 5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length

robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = WalkBot(20, 90, 15, 10)

print(robot_2.id)
print(robot_3.step_length)
print(robot_1.speed)


