friends = ["xyz", "abc", "234", "123", "Sam", "Har"]
print(friends)
for y in friends:
    print("Hello ", y)
for i in range(len(friends)):
    print("Hello ", friends[i])

z = "Hello ".join(friends)
print(z)
