def get_loc(city):
    loc = [("newyork", (2.5276)), ("paris", (1.235235)), ("LA", (4.2356)), ("Tokyo", (12.23526))]
    for name, coordinates in loc:
        if name.lower() == city.lower():
            return coordinates
    return None

if __name__ == "__main__":
    city = input("name:")
    coordinates = get_loc(city)

    if coordinates:
        print(f"the {city} located in {coordinates}")
    else:
        print(f"the {city} not found")