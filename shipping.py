### From Codecademy
weight = float(input("How heavy is your item in pounds?"))

### Ground shipping
if weight <= 2:
  cost_ground = 20 + weight*1.5
elif weight <= 6:
  cost_ground = 20 + weight*3
elif weight <= 10:
  cost_ground = 20 + weight*4
elif weight > 10:
  cost_ground = 20 + weight*4.75
print("Ground cost: $" + str(round(cost_ground, 2)))

### Ground Shipping Premium
cost_ground_premium = 125
print("Ground Premium cost: $" + str(round(cost_ground_premium, 2)))

### Drone Shipping
if weight <= 2:
  cost_drone = weight*4.5
elif weight <= 6:
  cost_drone = weight*9
elif weight <= 10:
  cost_drone = weight*12
elif weight > 10:
  cost_drone = weight*14.25
print("Drone cost: $" + str(round(cost_drone, 2)))

costs = [cost_ground, cost_ground_premium, cost_drone]
mode = ["Ground", "Ground Premium", "Drone"]

cheapest_option = mode[costs.index(min(costs))]
print("The cheapest option is " + cheapest_option + " at $" + str(min(costs)))
