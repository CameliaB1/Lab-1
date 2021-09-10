print("I have information for the following planets:")

print("   1. Mercury   2. Venus    3. Earth    4. Mars")
print("   5. Jupiter   6. Saturn   7. Uranus   8. Neptune")
 
weight = 170
planet = 6

if planet == 1:
 weight = weight * 0.38
elif planet == 2:
  weight = weight * 0.91
elif planet == 3:
 weight = weight
elif planet == 4:
  weight = weight * 0.38
elif planet == 5:
  weight = weight * 2.34
elif planet == 6:
  weight = weight * 1.06
elif planet == 7:
  weight = weight * 0.92
elif planet == 8:
  weight = weight * 1.19

print("your weight:", weight)
