import pyodbc
from math import radians, sin, cos, sqrt, atan2


def get_connection():
    #connection to database pyodbs
    conn = pyodbc.connect(
        'DRIVER={SQLite3 ODBC Driver};'
        'Direct=True;'
        'Database=city_coordinates.db;'
        'String Types=Unicode'
    )
    return conn


def create_table_if_not_exists():
    #Create table Coordinates
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Coordinates (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        city_name TEXT NOT NULL,
                        latitude REAL NOT NULL,
                        longitude REAL NOT NULL)''')
    conn.commit()
    conn.close()


def get_coordinates_from_db(city_name: str):
    #Get coordinates from database if city exists
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT latitude, longitude FROM Coordinates WHERE city_name = ?", (city_name,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0], result[1]
    else:
        return None


def store_coordinates_in_db(city_name: str, latitude: float, longitude: float):
    # Write coordinates to database if city isn`t exists
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Coordinates (city_name, latitude, longitude) VALUES (?, ?, ?)",
                   (city_name, latitude, longitude))
    conn.commit()
    conn.close()


def get_coordinates(city_name: str):
    coordinates = get_coordinates_from_db(city_name)

    if coordinates:
        return coordinates
    else:
        print(f"Coordinates for '{city_name}' not found.")
        #If no coordinates in database ask the user
        latitude = float(input(f"Enter latitude for {city_name}: "))
        longitude = float(input(f"Enter longitude for {city_name}: "))
        store_coordinates_in_db(city_name, latitude, longitude)
        print()
        return latitude, longitude


def calculate_distance(lat1, lon1, lat2, lon2):
    #Haversine formula
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Earth radius in km
    radius = 6371.0
    return radius * c


def main():
    #Create table if not exists
    create_table_if_not_exists()

    city1 = input("Enter the first city: ")
    lat1, lon1 = get_coordinates(city1)

    city2 = input("Enter the second city: ")
    lat2, lon2 = get_coordinates(city2)

    distance = calculate_distance(lat1, lon1, lat2, lon2)
    print(f"Distance between {city1} and {city2}: {distance:.2f} km")


if __name__ == "__main__":
    main()
