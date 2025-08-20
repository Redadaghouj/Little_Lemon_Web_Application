```markdown
# Little Lemon Restaurant Web Application

A full-featured Django web application for the Little Lemon restaurant, featuring API endpoints, user authentication, and database management.

## 🚀 Technologies Used

- **Backend Framework:** Django 4.2.7
- **API Framework:** Django REST Framework 3.14.0
- **Database:** MySQL
- **Authentication:** Djoser + JWT Tokens
- **Social Auth:** Social Auth App Django
- **Frontend:** Django Templates

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- MySQL Server
- pip (Python package manager)
- Git

### System Dependencies

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config libssl-dev
```

**macOS (Homebrew):**
```bash
brew install mysql pkg-config openssl
```

**Windows:**
Install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Redadaghouj/Little_Lemon_Web_Application.git
cd Little_Lemon_Web_Application
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate environment
# macOS/Linux:
source venv/bin/activate
# Windows Command Prompt:
venv\Scripts\activate.bat
# Windows PowerShell:
venv\Scripts\Activate.ps1
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure MySQL Database

**Create MySQL Database and User:**
```bash
mysql -u root -p
```

```sql
CREATE DATABASE littlelemon_db;
CREATE USER 'littlelemon_user'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON littlelemon_db.* TO 'littlelemon_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

**Update Database Configuration:**
Edit `LittleLemon/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon_db',
        'USER': 'littlelemon_user',
        'PASSWORD': 'your_secure_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Apply Database Migrations
```bash
python manage.py migrate
```

### 6. Create Superuser Account
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 7. Run the Development Server
```bash
python manage.py runserver
```

## 🌐 Access Points

- **Main Application:** http://127.0.0.1:8000
- **Django Admin Panel:** http://127.0.0.1:8000/admin
- **REST API:** http://127.0.0.1:8000/api
- **API Documentation:** http://127.0.0.1:8000/api/docs

## 🔐 Authentication Features

- JWT Token Authentication
- Session Authentication
- Social Authentication (Google/Facebook)
- Djoser for user management endpoints
- Password reset functionality

## 📦 Key Dependencies

- Django 4.2.7
- djangorestframework 3.14.0
- mysqlclient 2.2.0
- djoser 2.2.2
- djangorestframework-simplejwt 5.3.0
- social-auth-app-django 5.4.0
- cryptography 41.0.5

## 🐛 Troubleshooting

### Common Issues:

1. **mysqlclient Installation Fails**
   - Ensure system dependencies are installed
   - On Windows, verify Microsoft C++ Build Tools are installed

2. **Database Connection Errors**
   - Verify MySQL server is running
   - Check database credentials in settings.py
   - Ensure database and user exist in MySQL

3. **Port Already in Use**
   ```bash
   python manage.py runserver 8080
   ```

4. **Migration Errors**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## 📁 Project Structure

```
Little_Lemon_Web_Application/
├── LittleLemon/                 # Project settings
├── restaurant/                  # Main app
├── venv/                        # Virtual environment
├── requirements.txt             # Python dependencies
└── manage.py                    # Django management script
```

## 🔄 API Endpoints

- `/api/auth/` - Authentication endpoints
- `/api/menu/` - Menu items management
- `/api/booking/` - Reservation system
- `/api/user/` - User management
