# Hostel Management System

This project provides an efficient solution for managing student accommodation in hostels, leveraging Python, Tkinter, and MySQL for backend and frontend functionalities. Key features include student registration, automatic room allocation, and comprehensive record management.

---

## Table of Contents
1. [Features](#features)  
2. [Prerequisites](#prerequisites)  
3. [Installation](#installation)  
4. [Usage](#usage)  
5. [Support](#support)

---

## Features
- Student registration and room allocation  
- Management of hostels, departments, and mess facilities  
- Data viewing with intuitive filters  
- Ensures ACID properties for data transactions  
- User-friendly interface using Tkinter  

---

## Prerequisites
- **Python 3.8 or above**  
- **MySQL Server**  
- **Required Python Libraries:**  
  - `mysql-connector-python` (for MySQL connectivity)  
  - `tkinter` (for GUI development, pre-installed with Python)  
  - `os` (pre-installed with Python)  

---

## Installation
1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/vanshjaggi/HOSTEL_MANAGEMENT-RDBMS-PROJECT
   cd HOSTEL_MANAGEMENT-RDBMS-PROJECT
   ```

2. **Install Required Python Modules:**  
   ```bash
   pip install mysql-connector-python
   ```

3. **Set Up MySQL Database:**  
   - Open your MySQL client.  
   - Create the database and tables by running the SQL scripts provided in the project.  

4. **Configure Database Connection:**  
   - Update the database connection parameters in the Python code:  
     ```python
     connection = mysql.connector.connect(
         host="localhost",
         user="your_username",
         password="your_password",
         database="hostel_management"
     )
     ```

---

## Usage
1. Run the main Python script to launch the application:  
   ```bash
   python main.py
   ```

2. Navigate through the Tkinter GUI for various operations:  
   - **Home Page:** Access all main features.  
   - **New Registration:** Register a new student.  
   - **View Records:** View and manage existing records.  
   - **About:** Learn about the system.  

3. Ensure MySQL is running before launching the application.

---

## Support
For any issues or queries, visit the repository:  
[GitHub Repository](https://github.com/vanshjaggi/HOSTEL_MANAGEMENT-RDBMS-PROJECT)
