###From Codecademy
def trip_planner_welcome(name):
  greeting = 'Welcome to tripplanner v1.0 '
  print(greeting + name)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

name = input("What is your name?")
trip_planner_welcome(name)

origin = input("Where are you traveling from?")
destination = input("Where do you want to go?")
estimated_time = input("How long do you think it will take?")
mode_of_transport = input("How will you get there? (i.e. car)")
destination_setup(origin, destination, estimated_time, mode_of_transport)
