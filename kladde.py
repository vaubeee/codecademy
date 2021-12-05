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
'''
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  # call one function in the body of another and save to var
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

print(test_destination_index)