### From Codecademy

### Main Function
def coffee_bot():
  print("Welcome to the cafe!")

  num_drinks = 0
  drinks = []

  size = get_size()
  drink_type = get_drink_type()
  h_or_c = temp()
  cup_type = cup()

  drinks.append([size, h_or_c, drink_type, cup_type])
  num_drinks += 1

  another()

  for i in range(num_drinks):
    print("A " + str(drinks[i][0]) + " " + str(drinks[i][1]) + " " + str(drinks[i][2]) + " in a " + str(drinks[i][3]))


### Auxiliary Functions
###### Size
def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n ")
  if res == "a":
    return "small"
  elif res == "b":
    return "medium"
  elif res == "c":
    return "large"
  else:
    print_message()
    return get_size()

###### Error Message
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

###### Drink Type
def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte")
  if res == "a":
    return "brewed coffee"
  elif res =="b":
    return "mocha"
  elif res == "c":
    res2 = order_latte()
    return "latte with " + str(res2)
  else:
    print_message()

###### Latte Milk Type
def order_latte():
  res2 = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk")
  if res2 == "a":
    return "2% milk"
  elif res2 == "b":
    return "non-fat milk"
  elif res2 == "c":
    return "soy milk"
  else:
    print_message()

###### Disposable or Plastic Cup
def cup():
    cup = input("Would you like to use your own cup? \n[a] Yes \n[b] No")
    if cup == "a":
        return "reusable cup"
    elif cup == "b":
        return "disposable cup"

###### Hot or Iced
def temp():
    temperature = input("Iced or hot? \n[a] Iced \n[b] Hot")
    if temperature == "a":
        return "iced"
    elif temperature == "b":
        return "hot"

###### Another?
def another():
    another = input("Would you like to order another drink? \n[a] Yes \n[b] No")
    if another == "a":
        coffee_bot()
    if another == "b":
        pass


# Call coffee_bot()!
coffee_bot()

name = input("Can I get your name please?")
print("Thanks " + name + "! Your drink(s) will be ready shortly.")
