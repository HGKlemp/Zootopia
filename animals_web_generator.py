import data_fetcher

def serialize_animal(animal_data):
    """Create HTML for one animal."""

    output = ""
    output += "<li class=\"cards__item\">\n"
    output += f"  <div class=\"card__title\">{animal_data.get('name', 'Unknown')}</div>\n"
    output += "  <p class=\"card__text\">\n"

    diet = animal_data.get("characteristics", {}).get("diet", "Unknown")
    output += f"    <strong>Diet:</strong> {diet}<br/>\n"

    locations = animal_data.get("locations", [])
    location = " and ".join(locations) if locations else "Unknown"
    output += f"    <strong>Location:</strong> {location}<br/>\n"

    animal_type = animal_data.get("characteristics", {}).get("type")
    if animal_type:
        output += f"    <strong>Type:</strong> {animal_type}<br/>\n"

    output += "  </p>\n"
    output += "</li>\n"

    return output


def load_template():
    """Load HTML template."""

    try:
        with open("animals_template.html", "r", encoding="utf-8") as handle:
            return handle.read()

    except FileNotFoundError:
        print("Error: The file 'animals_template.html' was not found.")
        return None

    except OSError as e:
        print(f"Error reading the template file: {e}")
        return None


def write_html(html):
    """Write HTML file."""

    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(html)


def get_user_input():
    """Get animal name from user."""
    return input("Enter a name of an animal: ")


def main():
    """Run program."""

    load_animal = get_user_input()

    data = data_fetcher.fetch_data(load_animal)
    html_template = load_template()

    if not data:
        animals_html = f"<h2>No data found for '{load_animal}'.</h2>"
    else:
        animals_html = ""

        for animal_data in data:
            animals_html += serialize_animal(animal_data)

    new_html = html_template.replace(
        "__REPLACE_ANIMALS_INFO__", animals_html
    )

    write_html(new_html)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
    