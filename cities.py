from city_function import get_city_name

print("Enter 'q' to quit anytime")
while True:
    city_name = input("Enter the name of the city: ")
    if city_name == 'q':
        break
    city_country = input("Enter the name of the country: ")
    if city_country == 'q':
        break
    formatted_city = get_city_name(city_name, city_country)
    print(f"\tFormatted city name and country {formatted_city}")
    
    
    
