import json
def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


animals_data = load_data('animals_data.json')

print(animals_data)

def get_animals(animals_data):
  """ Returns a list of animals """

for animal in animals_data:
    name = animal['name']
    diet = animal['characteristics']['diet']
    location = animal['locations'][0]
    animal_type = animal.get('characteristics', {}).get('type', None)
    print(f"Name: {name}")
    print(f"Diet: {diet}")
    print(f"Location: {location}")
    if  animal_type:
        print(f"Type: {animal_type}")
    print()

    # print(f"Name: {name}")
    # print(f"Diet: {diet}")
    # print(f"Location{location}")
    # print(f"Type: {type}")



animals_data = load_data('animals_data.json')
get_animals(animals_data)