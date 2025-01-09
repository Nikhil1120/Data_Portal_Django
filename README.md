# MySQL Django Data Portal
A web application built using Django (Python) and MySQL to efficiently manage and retrieve employee/student data. This project provides full CRUD operations with secure user authentication, data validation, search and filter options, and an intuitive UI.

# Key Features
CRUD Operations: Perform Create, Read, Update, and Delete actions on employee/student data.
Secure User Authentication: Users must log in to access the portal, with data validation for security.
Search and Filter: Easily search and filter through the data to find specific records quickly.
Responsive UI: Built with HTML/CSS to ensure the portal works seamlessly on both desktop and mobile devices.
# Technologies Used
Django: Python web framework for backend development.
MySQL: Relational database for reliable and scalable data storage.
HTML/CSS: For building a responsive and user-friendly interface.
# Setup and Installation
Prerequisites
Before running the project, ensure that you have the following installed:

Python 3.x
MySQL Server
pip (Python package installer)
# Steps to Run the Project
 1.Clone the Repository
Clone the project to your local machine using the following command:


git clone https://github.com/yourusername/mysql-django-data-portal.git
cd mysql-django-data-portal

 2.Create and Activate a Virtual Environment It's a good practice to create a virtual environment to manage dependencies:


python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows

 3.Install Dependencies
Install the necessary Python dependencies listed in requirements.txt:


pip install -r requirements.txt

 4.Set Up MySQL Database Create a MySQL database for the project:


CREATE DATABASE django_data_portal;

 5.Update your MySQL database credentials in the settings.py file:


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_data_portal',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

 6.Apply Database Migrations Run Django migrations to set up the database schema:


python manage.py migrate
Create a Superuser

 7.To access the admin panel, create a superuser:


python manage.py createsuperuser

 8.Run the Development Server
Start the Django development server:

python manage.py runserver

 9.Access the Portal
Open your browser and go to http://127.0.0.1:8000 to view the portal. You can log in with the superuser account or any other user credentials.

# outputs:

![Screenshot 2024-12-13 231649](https://github.com/user-attachments/assets/11686032-fc28-4555-beff-722bdf69492a)


![Screenshot 2024-12-13 231703](https://github.com/user-attachments/assets/7e116903-ae83-493d-bf71-f3787481bb57)



# Acknowledgements
Sathish Gupta Sir for the continuous guidance and support throughout the project.
NareshIT for providing the essential resources and training that helped bring this project to life.
License
This project is licensed under the MIT License - see the LICENSE file for details.

