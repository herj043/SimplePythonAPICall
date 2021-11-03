
import requests

url_host = "https://dog.ceo"
endpoint = "/api/breeds/list/all"
query = ""

url = url_host + endpoint # + query

response = requests.get(url)
breeds = response.json()["message"]

# get a list of all breeds from the API call
all_breeds = breeds.keys()

# loop and print out each key
for breed in all_breeds:
  print(breed)

# Get a list of all subbreeds of a breed with at least 3 sub-breeds
# but NOT bulldogs
# Examples include: poodles, retrievers, terriers, mastiffs, spaniels, setters, & more

# Display all bulldog subbreeds
print("for examples try bulldog, poodle, retriever, terrier, mastiff, spaniel, and settler, for more try others listed above")
for i in range(1,4,1):
  print(i)
  requested_subbreeds = breeds[input("\nEnter a breed to find a available subreeds(no caps) = ")]


  for sub in requested_subbreeds:
    print(sub)

print("Thank you for testing this program")
