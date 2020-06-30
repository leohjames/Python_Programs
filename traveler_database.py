import sys
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
attractions= [[], [], [], [], []]

# This function provides the index position of the destination provided the destination in a string
def get_destination_index(destination):
  try:
      destination_index = destinations.index(destination)
      return destination_index
  except ValueError:
      print("Destination is not currently in our system, please choose another location.")
      sys.exit()
  
# This function operates similar to the previous function using the passenger information
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

#This function provides a way to add new attractions to the list of attractions
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination) 
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
  except ValueError:
    print("ValueError recieved!")

#This functions provides a list of attractions provided a destination and a list of interests
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if attraction_tags.count(interest) == 0:
        break
      else:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

#This function creates a string from the information they provided and the information gathered from previous functions
def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": "
  for attraction in traveler_attractions:
    if attraction == traveler_attractions[-1]:
        interests_string = interests_string + attraction + "."
    else: 
        interests_string = interests_string + attraction + ", "

  return interests_string

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
add_attraction("Paris, France", ["The Notre Dame", ["Cathedral", "monument"]])

smills_france = get_attractions_for_traveler(["Dereck Smill", "Paris, France", ["monument"]])
print(smills_france)