import mysql.connector
import os

from dotenv import load_dotenv
from google import genai
load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key is None:
    print("Gemini API key not found.")
else:
    print("Gemini API key is found.")
        
def get_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="flightdb"
    )

    return connection


def test_connection():

    connection = get_connection()

    if connection.is_connected():
        print("MySQL connection successful.")

    connection.close()

def add_flight():

    flight_no = input("Enter flight number: ")
    source = input("Enter source: ")
    destination = input("Enter destination: ")
    travel_date = input("Enter travel date (YYYY-MM-DD): ")
    departure_time = input("Enter departure time: ")
    arrival_time = input("Enter arrival time: ")
    price = input("Enter ticket price: ")
    seats = input("Enter number of seats: ")

    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        INSERT INTO flights
        (
            flight_no,
            source,
            destination,
            travel_date,
            departure_time,
            arrival_time,
            price,
            seats
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        flight_no,
        source,
        destination,
        travel_date,
        departure_time,
        arrival_time,
        price,
        seats
    )

    cursor.execute(sql, values)

    connection.commit()

    print("Flight added successfully.")

    cursor.close()
    connection.close()


# test_connection()

def view_flights():

    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        SELECT
            flight_id,
            flight_no,
            source,
            destination,
            travel_date,
            departure_time,
            arrival_time,
            price,
            seats
        FROM flights
    """

    cursor.execute(sql)

    rows = cursor.fetchall()

    print("\nAVAILABLE FLIGHTS")
    print("-" * 100)

    for row in rows:

        print(
            row[0],
            row[1],
            row[2],
            "->",
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
            row[8]
        )

    cursor.close()
    connection.close()

def search_flight():

    source = input("Enter source: ")
    destination = input("Enter destination: ")

    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        SELECT
            flight_id,
            flight_no,
            source,
            destination,
            travel_date,
            departure_time,
            arrival_time,
            price,
            seats
        FROM flights
        WHERE source = %s
        AND destination = %s
    """

    values = (source, destination)

    cursor.execute(sql, values)

    rows = cursor.fetchall()

    if len(rows) == 0:

        print("No flights found.")

    else:

        print("\nFlights Found")
        print("-" * 80)

        for row in rows:

            print(
                "ID:", row[0],
                "| Flight:", row[1],
                "|", row[2],
                "->",
                row[3],
                "| Date:", row[4],
                "| Price:", row[7],
                "| Seats:", row[8]
            )

    cursor.close()
    connection.close()

def update_flight():

    flight_id = input("Enter flight ID: ")

    new_price = input("Enter new price: ")
    new_seats = input("Enter new seat count: ")

    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        UPDATE flights
        SET price = %s,
            seats = %s
        WHERE flight_id = %s
    """

    values = (
        new_price,
        new_seats,
        flight_id
    )

    cursor.execute(sql, values)

    connection.commit()

    if cursor.rowcount > 0:
        print("Flight updated successfully.")
    else:
        print("Flight not found.")

    cursor.close()
    connection.close()



def delete_flight():

    flight_id = input("Enter flight ID: ")

    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        DELETE FROM flights
        WHERE flight_id = %s
    """

    cursor.execute(sql, (flight_id,))

    connection.commit()

    if cursor.rowcount > 0:
        print("Flight deleted successfully.")
    else:
        print("Flight not found.")

    cursor.close()
    connection.close()



def add_passenger():

    name = input("Enter passenger name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")

    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        INSERT INTO passengers
        (
            passenger_name,
            email,
            phone
        )
        VALUES (%s,%s,%s)
    """

    values = (
        name,
        email,
        phone
    )

    cursor.execute(sql, values)

    connection.commit()

    print("Passenger added successfully.")

    cursor.close()
    connection.close()


def view_passengers():

    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        SELECT
            passenger_id,
            passenger_name,
            email,
            phone
        FROM passengers
    """

    cursor.execute(sql)

    rows = cursor.fetchall()

    print("\nPASSENGERS")
    print("-" * 70)

    for row in rows:

        print(
            "ID:", row[0],
            "| Name:", row[1],
            "| Email:", row[2],
            "| Phone:", row[3]
        )

    cursor.close()
    connection.close()


def reserve_flight():

    passenger_id = input("Enter passenger ID: ")
    flight_id = input("Enter flight ID: ")
    seat_no = input("Enter seat number: ")

    connection = get_connection()
    cursor = connection.cursor()

    # Check available seats

    sql = """
        SELECT seats
        FROM flights
        WHERE flight_id = %s
    """

    cursor.execute(sql, (flight_id,))

    row = cursor.fetchone()

    if row is None:

        print("Flight not found.")

        cursor.close()
        connection.close()

        return

    seats = row[0]

    if seats <= 0:

        print("No seats available.")

        cursor.close()
        connection.close()

        return

    # Create reservation

    sql = """
        INSERT INTO reservations
        (
            passenger_id,
            flight_id,
            seat_no,
            booking_date
        )
        VALUES
        (
            %s,
            %s,
            %s,
            CURDATE()
        )
    """

    values = (
        passenger_id,
        flight_id,
        seat_no
    )

    cursor.execute(sql, values)

    # Reduce available seats

    sql = """
        UPDATE flights
        SET seats = seats - 1
        WHERE flight_id = %s
    """

    cursor.execute(sql, (flight_id,))

    connection.commit()

    print("Flight reservation successful.")

    cursor.close()
    connection.close()



def view_reservations():

    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        SELECT
            r.reservation_id,
            p.passenger_name,
            f.flight_no,
            f.source,
            f.destination,
            f.travel_date,
            r.seat_no,
            r.booking_date
        FROM reservations r
        INNER JOIN passengers p
            ON r.passenger_id = p.passenger_id
        INNER JOIN flights f
            ON r.flight_id = f.flight_id
    """

    cursor.execute(sql)

    rows = cursor.fetchall()

    print("\nRESERVATIONS")
    print("-" * 100)

    for row in rows:

        print(
            "Reservation:", row[0],
            "| Passenger:", row[1],
            "| Flight:", row[2],
            "|", row[3],
            "->",
            row[4],
            "| Date:", row[5],
            "| Seat:", row[6],
            "| Booking:", row[7]
        )

    cursor.close()
    connection.close()


def cancel_reservation():

    reservation_id = input("Enter reservation ID: ")

    connection = get_connection()
    cursor = connection.cursor()

    # Find flight

    sql = """
        SELECT flight_id
        FROM reservations
        WHERE reservation_id = %s
    """

    cursor.execute(sql, (reservation_id,))

    row = cursor.fetchone()

    if row is None:

        print("Reservation not found.")

        cursor.close()
        connection.close()

        return

    flight_id = row[0]

    # Delete reservation

    sql = """
        DELETE FROM reservations
        WHERE reservation_id = %s
    """

    cursor.execute(sql, (reservation_id,))

    # Increase available seats

    sql = """
        UPDATE flights
        SET seats = seats + 1
        WHERE flight_id = %s
    """

    cursor.execute(sql, (flight_id,))

    connection.commit()

    print("Reservation cancelled.")

    cursor.close()
    connection.close()



def explain_flight_with_gemini():

    flight_no = input("Enter flight number: ")

    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        SELECT
            flight_no,
            source,
            destination,
            travel_date,
            departure_time,
            arrival_time,
            price,
            seats
        FROM flights
        WHERE flight_no = %s
    """

    cursor.execute(sql, (flight_no,))

    row = cursor.fetchone()

    cursor.close()
    connection.close()

    if row is None:

        print("Flight not found.")
        return

    flight_details = (
        "Flight Number: " + str(row[0]) + "\n"
        "Source: " + str(row[1]) + "\n"
        "Destination: " + str(row[2]) + "\n"
        "Travel Date: " + str(row[3]) + "\n"
        "Departure: " + str(row[4]) + "\n"
        "Arrival: " + str(row[5]) + "\n"
        "Price: " + str(row[6]) + "\n"
        "Available Seats: " + str(row[7])
    )

    prompt = """
You are a helpful flight reservation assistant.

Explain the following flight details to a customer
in simple language.

Do not invent any information.

Flight information:

""" + flight_details

    try:

        client = genai.Client(api_key=google_api_key)

        response = client.models.generate_content(
            model="gemini-3.7-flash",
            contents=prompt
        )

        print("\nGEMINI FLIGHT ASSISTANT")
        print("-" * 60)
        print(response.text)

    except Exception as e:

        print("Gemini error:", e)




