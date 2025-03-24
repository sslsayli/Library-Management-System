

# Library Management System

## Overview
The **Library Management System** is a Django-based web application that provides a structured way to manage library books and student access. The system allows administrators to perform CRUD (Create, Read, Update, Delete) operations on books and enables students to view available books through a simple interface.

## Features
- **Admin Panel:**
  - Secure login for administrators
  - Manage books (add, update, delete, view)
  - Track book availability
- **Student View:**
  - Retrieve book records
  - View book details
- **Django REST Framework (DRF):**
  - API endpoints for book management
- **Database:**
  - MySQL as the backend database
- **CORS Support:**
  - Allows frontend integration with the backend

## Prerequisites
Before running the project, ensure you have the following installed:
- **Python 3.8+**
- **MySQL Server** (via XAMPP or MySQL Workbench)
- **pip** (Python package manager)
- **Git** (for version control, if using GitHub)

## Installation & Setup

### Step 1: Clone or Extract the Project
If you downloaded a ZIP file, extract it. If using Git:
```sh
git clone <repository_url>
cd <project_folder>
```

### Step 2: Create a Virtual Environment
```sh
python -m venv venv
```
Activate it:
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```sh
  source venv/bin/activate
  ```

### Step 3: Install Dependencies
```sh
pip install -r req.txt
```

### Step 4: Configure Database
1. Open `settings.py` and update the `DATABASES` section with your MySQL credentials.
2. Run database migrations:
   ```sh
   python manage.py migrate
   ```

### Step 5: Create a Superuser (Admin Access)
```sh
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### Step 6: Run the Development Server
```sh
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** in your browser.

## API Endpoints
| Method | Endpoint        | Description           |
|--------|----------------|-----------------------|
| GET    | `/api/books/`  | Retrieve all books   |
| POST   | `/api/books/`  | Add a new book       |
| PUT    | `/api/books/{id}/` | Update book details |
| DELETE | `/api/books/{id}/` | Delete a book      |

## Technologies Used
- **Django 5.0.4**
- **Django REST Framework**
- **MySQL**
- **Python 3.8+**
- **CORS Headers**

## Future Enhancements
- Implement **JWT authentication** for secure login.
- Add **frontend integration** using React.js or Angular.
- Implement **book search and filtering**.
- Enable **user roles and permissions** for enhanced security.

## License
This project is open-source under the **MIT License**. Feel free to contribute and enhance the system!

## Contributors
- **Your Name** (Developer)
- Open to community contributions!

## Contact
For any issues or suggestions, reach out at **your-email@example.com** or create an issue on GitHub.


      

