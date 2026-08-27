# gemini_chatbot
A Python-based Flight Reservation System with MySQL database integration and Gemini AI assistance for managing flights, passengers, and reservations.

# ✈️ Flight Reservation System

## 📖 About the Project

This is a **Python-based Flight Reservation System** that helps manage flight details, passenger information, and flight reservations through a simple command-line interface.

The application is connected to a **MySQL database** for storing and managing data. It also includes a **Gemini AI Assistant** feature that can explain flight information in simple and user-friendly language.

---

## ✨ Features

* ➕ Add new flights
* 📋 View available flights
* 🔍 Search for a flight
* ✏️ Update flight details
* 🗑️ Delete flights
* 👤 Add passenger details
* 📄 View passenger records
* 🎫 Book a flight
* 📑 View reservations
* ❌ Cancel reservations
* 🤖 Get flight information with Gemini AI
* 💺 Automatically manage available seats

The project supports flight, passenger, and reservation management through its console menu.

---

## 🛠️ Built With

* **Python**
* **MySQL**
* **mysql-connector-python**
* **Google Gemini AI**
* **python-dotenv**

---

## 📂 Project Files

```text
Flight-Reservation-System/
│
├── main.py
├── flight_reservation.py
├── config.py
├── app.py
├── README.md
└── .env
```

The main program provides an interactive dashboard, while the project files handle database operations and Gemini integration.

---

## ⚙️ Installation

### Clone the repository

```bash
git clone <your-repository-link>
```

### Go to the project folder

```bash
cd Flight-Reservation-System
```

### Install required libraries

```bash
pip install mysql-connector-python python-dotenv google-genai
```

---

## 🗄️ Database Setup

Create a MySQL database named:

```sql
CREATE DATABASE flightdb;
USE flightdb;
```

The project uses three main tables:

* `flights`
* `passengers`
* `reservations`

These tables store flight information, passenger details, and booking records.

---

## 🤖 Gemini AI Feature

The system includes a Gemini AI feature that helps explain flight details in simple language.

The process works as follows:

1. The user enters a flight number.
2. The system retrieves the flight information from MySQL.
3. The data is sent to Gemini.
4. Gemini generates a simple explanation of the flight details.

---

## ▶️ Run the Project

Run the following command:

```bash
python main.py
```

You will see a menu where you can manage flights, passengers, reservations, and access the Gemini AI feature.

---

## 🎯 What I Learned

Through this project, I practiced:

* Python programming
* MySQL database connectivity
* CRUD operations
* Flight and passenger management
* Reservation handling
* Database relationships
* API integration
* Using Generative AI with structured data

---

## 👩‍💻 Author

**Sania Mumtaz**

---

⭐ **If you found this project useful, please give it a star!**

