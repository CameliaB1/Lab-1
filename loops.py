states = ["Alabama", "Hawaii", "Massachusetts", "New Mexico", "South Dakota"]
 
states_lows = [46.5, 67.4, 27.4, 36.1, 19.5]
 
states_highs = [78.6, 72.2, 68, 71.4, 69.9]
 
states_low = [temp for temp in states_lows if temp < 20]
states_high = [temp1 for temp1 in states_highs if temp1 > 75]
 
print("Out of the five states, ",  states,  ", the lowest temperature see was ", states_low, " F, while the highest the five states normally sees is ", states_high, "F.")
