class Seat:

    def __init__(self, seat_number, category, price):
        self.seat_number = seat_number
        self.category = category
        self.price = price
        self.is_booked = False

    def display(self):

        if self.is_booked:
            return "[XX]"

        else:
            return f"[{self.seat_number}]"


class Event:

    def __init__(self, event_name):
        self.event_name = event_name
        self.seats = []

    def add_seat(self, seat):
        self.seats.append(seat)

    def display_seats(self):

        print("\n")
        print("              ┌───────────────┐")
        print("              │     SCREEN    │")
        print("              └───────────────┘")

        print("\nSeat Layout:\n")

        current_row = ""

        for seat in self.seats:

            row = seat.seat_number[0]
            number = int(seat.seat_number[1:])

            # Move to next line when row changes
            if current_row != "" and row != current_row:
                print()

            # Display seat
            print(seat.display(), end=" ")

            # Create aisle after 5th seat
            if number == 5:
                print("    ", end="")

            # Remember current row
            current_row = row

        print("\n")

    def get_available_seat_count(self):

        count = 0

        for seat in self.seats:

            if not seat.is_booked:
                count += 1

        return count

    def find_adjacent_seats(self, number_of_seats):

        rows = {}

        # Group seats according to rows
        for seat in self.seats:

            row = seat.seat_number[0]

            if row not in rows:
                rows[row] = []

            rows[row].append(seat)

        # Check every row
        for row in rows:

            available_group = []

            for seat in rows[row]:

                if not seat.is_booked:

                    available_group.append(seat)

                    # Required number of adjacent seats found
                    if len(available_group) == number_of_seats:

                        return available_group

                else:

                    # Break the current group
                    available_group = []

        # No adjacent group found
        return None

    def book_seats(self, seat_numbers):

        total_price = 0
        selected_seats = []

        for seat_number in seat_numbers:

            # Check duplicate selection
            for selected_seat in selected_seats:

                if selected_seat.seat_number == seat_number:

                    print(f"{seat_number} was selected more than once.")
                    return

            # Find the seat
            seat_found = False

            for seat in self.seats:

                if seat.seat_number == seat_number:

                    seat_found = True

                    # Check if already booked
                    if seat.is_booked:

                        print(f"{seat_number} is already booked.")
                        return

                    selected_seats.append(seat)

                    break

            # Seat does not exist
            if not seat_found:

                print(f"{seat_number} does not exist.")
                return

        # Book seats after all validation
        for seat in selected_seats:

            seat.is_booked = True
            total_price += seat.price

        return total_price


class Booking:

    booking_counter = 1000

    def __init__(self, event, theatre_name, seat_numbers, total_price):

        Booking.booking_counter += 1

        self.booking_id = "ST" + str(Booking.booking_counter)
        self.event = event
        self.theatre_name = theatre_name
        self.seat_numbers = seat_numbers
        self.total_price = total_price
        self.is_cancelled = False

    def display_booking(self):

        print("\n========== BOOKING CONFIRMATION ==========")

        print("\nBooking ID:", self.booking_id)
        print("Theatre:", self.theatre_name)
        print("Movie:", self.event.event_name)

        print("\nBooked Seats:")

        for seat_number in self.seat_numbers:
            print(seat_number)

        print(f"\nTotal Price: ₹{self.total_price}")

        print("\nBooking successful!")

    def display_history(self):

        print("\n========== BOOKING HISTORY ==========")

        print("\nBooking ID:", self.booking_id)
        print("Theatre:", self.theatre_name)
        print("Movie:", self.event.event_name)

        print("Seats:", ", ".join(self.seat_numbers))

        print(f"Total Price: ₹{self.total_price}")


class Theatre:

    def __init__(self, theatre_name):

        self.theatre_name = theatre_name
        self.events = []

    def add_event(self, event):

        self.events.append(event)

    def display_events(self):

        print(f"\nMovies at {self.theatre_name}:")

        for i, event in enumerate(self.events, start=1):

            print(f"{i}.{event.event_name}")

# FUNCTION TO CREATE SEATS

def create_seats(event):

    rows = ["A", "B", "C", "D"]

    for row in rows:

        for number in range(1, 11):

            seat_number = row + str(number)

            # First two rows = Regular
            if row in ["A", "B"]:

                category = "Regular"
                price = 150

            # Last two rows = Premium
            else:

                category = "Premium"
                price = 250

            seat = Seat(seat_number, category, price)

            event.add_seat(seat)

# CREATE MOVIES FOR PVR

pvr_avengers = Event("Avengers")
pvr_interstellar = Event("Interstellar")
pvr_jurassic = Event("Jurassic World")

create_seats(pvr_avengers)
create_seats(pvr_interstellar)
create_seats(pvr_jurassic)


# CREATE MOVIES FOR INOX

inox_avengers = Event("Avengers")
inox_avatar = Event("Avatar")
inox_batman = Event("Batman")

create_seats(inox_avengers)
create_seats(inox_avatar)
create_seats(inox_batman)


# CREATE MOVIES FOR CINEPOLIS

cinepolis_avatar = Event("Avatar")
cinepolis_interstellar = Event("Interstellar")
cinepolis_spiderman = Event("Spider-Man")

create_seats(cinepolis_avatar)
create_seats(cinepolis_interstellar)
create_seats(cinepolis_spiderman)


# CREATE THEATRES

theatre1 = Theatre("PVR Cinemas")
theatre2 = Theatre("INOX")
theatre3 = Theatre("Cinepolis")


# ADD MOVIES TO PVR

theatre1.add_event(pvr_avengers)
theatre1.add_event(pvr_interstellar)
theatre1.add_event(pvr_jurassic)

# ADD MOVIES TO INOX

theatre2.add_event(inox_avengers)
theatre2.add_event(inox_avatar)
theatre2.add_event(inox_batman)


# ADD MOVIES TO CINEPOLIS

theatre3.add_event(cinepolis_avatar)
theatre3.add_event(cinepolis_interstellar)
theatre3.add_event(cinepolis_spiderman)


# STORE ALL THEATRES

theatres = [theatre1, theatre2, theatre3]

booking_history = []


# MAIN PROGRAM

while True:

    print("\n========== SMART TICKET ==========")

    print("\n1. Book Tickets")
    print("2. View Booking History")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = input("\nEnter your choice: ")


    # BOOK TICKETS

    if choice == "1":

        print("\nAvailable Theatres:")

        for i, theatre in enumerate(theatres, start=1):

            print(f"{i}. {theatre.theatre_name}")

        # Select theatre

        while True:

            try:

                theatre_choice = int(
                    input("\nChoose a theatre: ")
                )

                if theatre_choice < 1 or theatre_choice > len(theatres):

                    print(
                        "Invalid choice. Please choose a valid theatre."
                    )

                else:

                    break

            except ValueError:

                print("Please enter a number.")


        selected_theatre = theatres[theatre_choice - 1]

        print(f"\nYou selected: {selected_theatre.theatre_name}")


        # Select movie

        selected_theatre.display_events()

        while True:

            try:

                movie_choice = int(
                    input("\nChoose a movie: ")
                )

                if movie_choice < 1 or movie_choice > len(
                    selected_theatre.events
                ):

                    print(
                        "Invalid choice. Please choose a valid movie."
                    )

                else:

                    break

            except ValueError:

                print("Please enter a number.")


        selected_event = selected_theatre.events[movie_choice - 1]

        print(f"\nYou selected: {selected_event.event_name}")


        # Display seats

        selected_event.display_seats()

        print(
            f"\nTotal seats: {len(selected_event.seats)}"
        )

        available_seats = (
            selected_event.get_available_seat_count()
        )

        print(
            f"Available seats: {available_seats}"
        )

        # Ask number of seats

        while True:

            try:

                number_of_seats = int(
                    input(
                        "\nHow many seats do you want to book? "
                    )
                )

                if number_of_seats <= 0:

                    print(
                        "Please enter at least 1 seat."
                    )

                elif number_of_seats > available_seats:

                    print(
                        f"Only {available_seats} seats are available."
                    )

                else:

                    break

            except ValueError:

                print(
                    "Please enter a number, like 1, 2, or 3."
                )

        # SMART SEAT SUGGESTION
        
        suggested_seats = (
            selected_event.find_adjacent_seats(
                number_of_seats
            )
        )

        # If adjacent seats are available

        if suggested_seats:

            print("\nSmart Seat Suggestion:")

            for seat in suggested_seats:

                print(
                    seat.seat_number,
                    end=" "
                )

            print()

            print("\n1. Accept suggested seats")
            print("2. Choose seats manually")


            # Choose suggestion or manual selection

            while True:

                suggestion_choice = input(
                    "\nEnter your choice: "
                )


                # Accept suggested seats
                if suggestion_choice == "1":

                    seat_numbers = []

                    for seat in suggested_seats:

                        seat_numbers.append(
                            seat.seat_number
                        )

                    manual_selection = False

                    break


                # Choose seats manually
                elif suggestion_choice == "2":

                    seat_numbers = []

                    manual_selection = True

                    break


                else:

                    print(
                        "Invalid choice. Please enter 1 or 2."
                    )

        # No adjacent seats available

        else:

            print(
                "\nSorry, no adjacent seats are available."
            )

            seat_numbers = []

            manual_selection = True


        # MANUAL SEAT SELECTION

        if manual_selection:

            for i in range(number_of_seats):

                while True:

                    seat_number = input(
                        f"Enter seat number {i + 1}: "
                    ).upper()


                    # Check duplicate selection

                    if seat_number in seat_numbers:

                        print(
                            f"{seat_number} is already selected. "
                            "Please choose another seat."
                        )

                        continue

                    # Assume seat is not found

                    seat_found = False

                    # Check all seats

                    for seat in selected_event.seats:

                        if seat.seat_number == seat_number:

                            seat_found = True


                            # Check if already booked
                            if seat.is_booked:

                                print(
                                    f"{seat_number} is already booked. "
                                    "Please choose another seat."
                                )

                                break


                            # Seat is valid and available
                            seat_numbers.append(
                                seat_number
                            )

                            break

                    # Seat does not exist
    
                    if not seat_found:

                        print(
                            f"{seat_number} does not exist. "
                            "Please enter a valid seat."
                        )

                        continue

                    # Check whether the seat was booked
                    
                    booked = False

                    for seat in selected_event.seats:

                        if seat.seat_number == seat_number:

                            if seat.is_booked:

                                booked = True

                            break


                    if booked:

                        continue


                    # Valid seat
                    break


        # BOOK SEATS
        
        total_price = selected_event.book_seats(
            seat_numbers
        )

        # CREATE BOOKING

        booking = Booking(
            selected_event,
            selected_theatre.theatre_name,
            seat_numbers,
            total_price
        )


        # Save booking
        booking_history.append(booking)


        # Display ticket
        booking.display_booking()

    # BOOKING HISTORY

    elif choice == "2":

        print("\n========== BOOKING HISTORY ==========")

        if len(booking_history) == 0:

            print("\nNo bookings found.")

        else:

            for booking in booking_history:

                booking.display_history()

    # CANCEL BOOKING

    elif choice == "3":

        print("\n========== CANCEL BOOKING ==========")

        if len(booking_history) == 0:

            print("\nNo bookings found.")

        else:

            booking_id = input("\nEnter Booking ID: ").upper()

            booking_found = False

            for booking in booking_history:

                if booking.booking_id == booking_id:

                    if booking.is_cancelled:
                        print("\nThis booking is already cancelled.")
                        break

                    booking_found = True

                    print("\nBooking found!")

                    print("\nBooking ID:", booking.booking_id)
                    print("Theatre:", booking.theatre_name)
                    print("Movie:", booking.event.event_name)
                    print("Seats:", ", ".join(booking.seat_numbers))
                    print(f"Total Price: ₹{booking.total_price}")

                    print("\nDo you want to cancel this booking?")
                    print("1. Yes")
                    print("2. No")

                    cancel_choice = input("\nEnter your choice: ")

                    if cancel_choice == "1":

                        # Release the booked seats

                        for seat_number in booking.seat_numbers:

                            for seat in booking.event.seats:

                                if seat.seat_number == seat_number:

                                    seat.is_booked = False

                                    break

                        booking.is_cancelled = True

                        refund = booking.total_price
                        print(f"\nRefund Amount: ₹{refund}")

                        print("\nBooking cancelled successfully.")

                    elif cancel_choice == "2":

                        print("\nCancellation cancelled.")

                    else:

                        print("\nInvalid choice.")

                    break
            if not booking_found:

                print("\nBooking ID not found.")

    # EXIT

    elif choice == "4":

        print(
            "\nThank you for using SmartTicket!"
        )

        break

    # INVALID CHOICE
    
    else:

        print(
            "\nInvalid choice. Please select 1, 2, or 3."
        )








