# Q6. List & Tuple Operations: (4 Marks)
# • Create a list of 8 city names
# • Print first 4 cities
# • Print last 4 cities
# • Add a new city at end
# • Remove the first city
# • Convert list to tuple and print

city=["Bhopal","Indore","Reva","jaipur","Satna","Itarsi","Vidisha","Betul"]

print(city[:5])

print(city[:3:-1])

city.append("Pune")     # Add new city

print(city)

a=city[0]

city.remove(a)  #Remove the first value

print(city)

tup=tuple(city)  #Convert into tuple

print(tup)