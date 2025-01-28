# PulseCord

PulseCord is a web application designed for students to connect, collaborate, and communicate seamlessly, similar to Discord. It facilitates text and voice communication, topic-based discussions, and resource sharing in a secure and user-friendly environment.

---

## Features

- **Real-Time Communication**: Chat with others in rooms categorized by topics.
- **User Authentication**: Secure login and registration system.
- **Room Management**:
  - Create, edit, and delete discussion rooms.
  - Topic-based room categorization.
- **Recent Activity Feed**: Track recent messages and interactions.
- **User Profiles**: View user-specific activity and room participation.

---

## Tech Stack

### **Frontend**:
- HTML
- CSS
- JavaScript

### **Backend**:
- Django (Python Framework)
- SQLite (Database)

### **Other Tools**:
- Virtual Environment (`env`)
- Git for version control

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd phase2
   ```

3. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate # For Windows: env\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000`.

---

## Screenshots

### Homepage
![Homepage Screenshot](#)
Description: Overview of available rooms and recent activities.

### Login Page
![Login Page Screenshot](#)
Description: Secure user login with username and password.

### Room Page
![Room Page Screenshot](#)
Description: Real-time conversation with participants.

---

## Project Structure

```
PulseCord/
├── base/
│   ├── templates/      # HTML templates
│   ├── static/         # CSS, JS, and image files
│   ├── models.py       # Database models
│   ├── views.py        # View functions
│   └── urls.py         # URL routing
├── manage.py           # Django project management
├── db.sqlite3          # SQLite database
└── requirements.txt    # Python dependencies
```


---

## Contact
For any inquiries or contributions, feel free to reach out:
- Email: [your-email@example.com]
- GitHub: [GitHub Profile Link]

