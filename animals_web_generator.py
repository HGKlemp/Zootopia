import json


def serialize_animal(animal_data):
    output = ""
    output += "<li class=\"cards__item\">\n"
    output += f"  <div class=\"card__title\">{animal_data['name']}</div>\n"
    output += "  <p class=\"card__text\">\n"
    output += f"    <strong>Diet:</strong> {animal_data['characteristics']['diet']}<br/>\n"

    locations = animal_data.get("locations", [])
    location = " and ".join(locations) if locations else "Unknown"
    output += f"    <strong>Location:</strong> {location}<br/>\n"

    animal_type = animal_data.get("characteristics", {}).get("type")
    if animal_type:
        output += f"    <strong>Type:</strong> {animal_type}<br/>\n"

    output += "  </p>\n"
    output += "</li>\n"

    return output


with open("animals_data.json", "r", encoding="utf-8") as handle:
    data = json.load(handle)

with open("animals_template.html", "r", encoding="utf-8") as handle:
    html_template = handle.read()


animals_html = ""

for animal_data in data:
    animals_html += serialize_animal(animal_data)


new_html = html_template.replace(
    "__REPLACE_ANIMALS_INFO__", animals_html)

with open("animals.html", "w", encoding="utf-8") as handle:
    handle.write(new_html)