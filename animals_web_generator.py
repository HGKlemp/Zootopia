import json


with open("animals_data.json", "r") as handle:
    animals_data = json.load(handle)


with open("animals_template.html", "r") as handle:
    html_template = handle.read()


animals_html = ""


for animal in animals_data:

    name = animal.get("name", "Unknown")
    diet = animal.get("characteristics", {}).get("diet", "Unknown")

    locations = animal.get("locations", [])
    location = locations[0] if locations else "Unknown"

    animal_type = animal.get("characteristics", {}).get("type")

    animals_html += "<li class='cards__item'>\n"

    animals_html += f"  <h2 class='card__title'>{name}</h2>\n"
    animals_html += "  <div class='card__text'>\n"

    animals_html += f"    <p><strong>Diet:</strong> {diet}</p>\n"
    animals_html += f"    <p><strong>Location:</strong> {location}</p>\n"

    if animal_type:
        animals_html += f"    <p><strong>Type:</strong> {animal_type}</p>\n"

    animals_html += "  </div>\n"
    animals_html += "</li>\n"


new_html = html_template.replace(
    "__REPLACE_ANIMALS_INFO__",
    animals_html
)


with open("animals.html", "w") as handle:
    handle.write(new_html)