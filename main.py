from flight_reservation import *
def dashboard():

    while True:

        print("\n")
        print("=" * 60)
        print("       FLIGHT RESERVATION SYSTEM")
        print("=" * 60)

        print("1. Add Flight")
        print("2. View Flights")
        print("3. Search Flight")
        print("4. Update Flight")
        print("5. Delete Flight")

        print("6. Add Passenger")
        print("7. View Passengers")

        print("8. Reserve Flight")
        print("9. View Reservations")
        print("10. Cancel Reservation")

        print("11. Ask Gemini About Flight")

        print("0. Exit")

        print("=" * 60)

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                add_flight()

            case "2":
                view_flights()

            case "3":
                search_flight()

            case "4":
                update_flight()

            case "5":
                delete_flight()

            case "6":
                add_passenger()

            case "7":
                view_passengers()

            case "8":
                reserve_flight()

            case "9":
                view_reservations()

            case "10":
                cancel_reservation()

            case "11":
                explain_flight_with_gemini()

            case "0":
                print("Thank you for using Flight Reservation System.")
                break

            case _:
                print("Invalid choice. Please try again.")



dashboard()