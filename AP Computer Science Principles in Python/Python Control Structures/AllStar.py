# Enter your code here
points = int(input("Points per game? "))
print(points)
rebounds = int(input("Rebounds per game? "))
print(rebounds)
assists = int(input("Assists per game? "))
print(assists)

rolled_doubles = bool((points >= 25) or ((points >= 10) and (rebounds >= 10) and (assists >= 10)))

print("Is all star? " + str(rolled_doubles))