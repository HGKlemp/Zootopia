import json


with open("animals_data.json", "r") as handle:
    animals_data = json.load(handle)


with open("animals_template.html", "r") as handle:
    html_template = handle.read()

animals_text = ""

for animal in animals_data:

    name = animal.get("name", "Unknown")
    diet = animal.get("characteristics", {}).get("diet", "Unknown")

    locations = animal.get("locations", [])
    location = locations[0] if locations else "Unknown"

    animal_type = animal.get("characteristics", {}).get("type", "")


    animals_text += f"Name: {name} "
    animals_text += f"Diet: {diet} "
    animals_text += f"Location: {location}"

    if animal_type:
        animals_text += f" Type: {animal_type}"

    animals_text += "\n"


new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_text)


with open("animals.html", "w") as handle:
    handle.write(new_html)
