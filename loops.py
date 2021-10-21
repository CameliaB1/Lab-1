states = ["Alabama", "Hawaii", "Massachusetts", "New Mexico", "South Dakota"]

states_lows = [46.5, 67.4, 27.4, 36.1, 19.5]

states_highs = [78.6, 72.2, 68, 71.4, 69.9]

state_temps = zip(states_lows, states_highs, states)
list_states_temps = list(state_temps)

for temp in list_states_temps[1][0]:
    if temp <= 20:
        print("Here is the lowest temp out of the five states")

print(list_states_temps)
