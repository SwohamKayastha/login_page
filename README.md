# Full-Stack Project: Login, Register, and Profile Pages

This project is a full-stack web application built with **React** (frontend), **Django** (backend), and **Supabase** (database). The application includes the following features:
- **Login Page**: Allows users to log into their accounts.
- **Register Page**: Enables users to create new accounts.
- **Profile Page**: Displays user-specific information.

---

## Technologies Used
### Frontend:
- React (Vite for development)
- CSS for styling

### Backend:
- Django
- Django REST Framework
- Simple JWT for authentication

### Database:
- Supabase (PostgreSQL-based backend as a service)

---

## How to Run the Project

### Clone the Repository
```bash
git clone <repository_url>
cd <repository_directory>
````

### Set up environment variables in .env:
```bash
DEBUG=True
user = db_username
password = db_password
host = host
port = port
dbname = postgres

django_security_key = django_secret_key
````

# Project Screenshots
### Login Page:
![Login Page](https://github.com/SwohamKayastha/login_page/blob/main/img/Login2.png)

### Register Page:
![Register Page](https://github.com/SwohamKayastha/login_page/blob/main/img/Register.png)

### Profile Page:
![Profile Page](https://github.com/SwohamKayastha/login_page/blob/main/img/Profile.png)

# Running the Servers
## Backend:

````bash
cd backend
python manage.py runserver
````

## Frontend
````bash
cd frontend
npm install
npm run dev
````
