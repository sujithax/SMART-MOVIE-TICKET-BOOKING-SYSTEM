# SMART-MOVIE-TICKET-BOOKING-SYSTEM
SmartTicket is a Python-based movie ticket booking system built using OOP concepts. It supports theatre and movie selection, seat availability, smart adjacent-seat suggestions, booking history, ticket cancellation, and automatic refund calculation.

##  Project Overview

**SmartTicket** is a console-based movie ticket booking system developed in **Python using Object-Oriented Programming (OOP)** concepts.

The system allows users to select theatres and movies, view seat availability, book tickets, receive smart adjacent-seat suggestions, view booking history, and cancel bookings with automatic refund calculation.

---

##  Features

*  **Theatre Selection** – Choose from PVR Cinemas, INOX, and Cinepolis.
*  **Movie Selection** – Select available movies from the chosen theatre.
*  **Seat Management** – View the complete seat layout and availability.
*  **Smart Seat Suggestion** – Automatically suggests adjacent seats when available.
*  **Ticket Booking** – Book one or multiple seats.
*  **Automatic Price Calculation** – Calculates the total ticket price based on seat category.
*  **Booking History** – View all previous bookings.
*  **Ticket Cancellation** – Cancel an existing booking.
*  **Refund Calculation** – Displays the refund amount after cancellation.
*  **Input Validation** – Handles invalid theatre, movie, seat, and booking selections.

---

##  OOP Concepts Used

The project is structured using multiple classes to demonstrate Object-Oriented Programming.

### `Seat`

Represents an individual seat and stores:

* Seat number
* Seat category
* Seat price
* Booking status

### `Event`

Represents a movie and manages:

* Movie name
* Seats
* Seat layout
* Available seat count
* Adjacent seat detection
* Seat booking

### `Booking`

Represents a customer's booking and stores:

* Booking ID
* Theatre
* Movie
* Selected seats
* Total price
* Cancellation status

### `Theatre`

Represents a theatre and manages:

* Theatre name
* Available movies

---

##  Seat Categories

Each movie has **40 seats** arranged across four rows:

| Rows | Category | Price |
| ---- | -------- | ----: |
| A, B | Regular  |  ₹150 |
| C, D | Premium  |  ₹250 |

The project automatically creates the seats and assigns their categories and prices.

---

##  Smart Seat Suggestion

One of the main features of SmartTicket is the **adjacent-seat recommendation system**.

When a user wants to book multiple seats, the system checks each row for consecutive available seats. If a suitable group is found, those seats are suggested to the user.

The user can either:

1. Accept the suggested seats
2. Select seats manually

If adjacent seats are unavailable, the system automatically allows manual seat selection.

---

##  System Workflow

```text
Start
  ↓
Display Main Menu
  ↓
Select Theatre
  ↓
Select Movie
  ↓
Display Seat Layout
  ↓
Enter Number of Seats
  ↓
Check Adjacent Seats
  ↓
Smart Suggestion / Manual Selection
  ↓
Validate Selected Seats
  ↓
Calculate Total Price
  ↓
Generate Booking ID
  ↓
Display Booking Confirmation
  ↓
Booking History / Cancellation
  ↓
Exit
```

---

##  Booking Process

The user first selects a theatre and movie. The system then displays the available seats and asks how many seats the user wants to book.

For multiple seats, the system searches for adjacent available seats and provides a smart suggestion. The selected seats are validated before being booked, preventing duplicate selections and already-booked seats.

After successful booking, a unique booking ID is generated and the booking details are displayed.

---

##  Cancellation & Refund

Users can cancel a booking by entering the booking ID.

When a booking is cancelled:

* The booked seats are released.
* The booking is marked as cancelled.
* The refund amount is calculated based on the original booking price.
* The cancellation status is updated.

The system also prevents an already-cancelled booking from being cancelled again.

---

##  Technologies Used

* **Python**
* **Object-Oriented Programming (OOP)**
* Classes & Objects
* Lists
* Loops
* Conditional Statements
* Functions
* Exception Handling
* Input Validation

---


## 📋 Main Menu

When the program starts, users can choose:

```text
========== SMART TICKET ==========

1. Book Tickets
2. View Booking History
3. Cancel Booking
4. Exit
```

---

## 🎯 Learning Outcomes

This project helped demonstrate practical implementation of:

* Object-Oriented Programming in Python
* Class relationships and object management
* Real-world problem modelling
* Data validation
* Exception handling
* Seat allocation logic
* Search and selection algorithms
* Building an interactive console application

