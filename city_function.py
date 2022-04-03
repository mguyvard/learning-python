def get_city_name(city_name, city_country, population = ""):
    """Returns the name of the city followed by the name of the country"""
    if population:
        full_name = f"{city_name}, {city_country} - population {population}"
    else:
        full_name = f"{city_name}, {city_country}"
    return full_name.title()
