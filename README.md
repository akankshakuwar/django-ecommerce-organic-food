# Fresh Fields

# Inspiration

Organic food, especially fresh fruits and vegetables, is often difficult to find in the market. Most produce is sprayed with pesticides and harmful chemicals, making it a risky choice for health-conscious individuals. Conventional fruits and vegetables are genetically modified, leading to numerous health concerns. Since food is a major component of our lifestyle, even a small change towards organic produce can significantly boost immunity and contribute to a healthier life. This concept inspired the creation of Fresh Fields.
What It Does
Fresh Fields is a web application designed to provide a seamless eCommerce experience for ordering fresh, organic fruits and vegetables directly from farms. The platform allows users to:

# Sign in & login securely.

![Screenshot 2025-03-30 191025](https://github.com/user-attachments/assets/236c22f8-82a8-4ce0-9bbe-7e3482825ae8)
![Screenshot 2025-03-30 194200](https://github.com/user-attachments/assets/828e750a-8c99-401d-9f15-74603ffa8f18)
![Screenshot 2025-03-30 191332](https://github.com/user-attachments/assets/97511dd3-a0aa-4c07-983b-ae9344ad6a56)
![Screenshot 2025-03-30 191400](https://github.com/user-attachments/assets/a6f264f8-d612-4f6d-99a2-e4ad7001af78)


# Browse product details, add items to the cart, and proceed through checkout.
![Screenshot 2025-03-30 191807](https://github.com/user-attachments/assets/2ca219fd-d4c7-448e-a811-0ea2a33f753e)

# Place orders for authentic organic fruits and vegetables, ensuring health and sustainability.
![Screenshot 2025-03-30 191518](https://github.com/user-attachments/assets/b1670dc7-c3de-4228-a28c-a0d984a68afd)
![Screenshot 2025-03-30 192221](https://github.com/user-attachments/assets/4e9c24b2-e1c8-47b9-a63f-d064f94a5c8d)
![Screenshot 2025-03-30 191549](https://github.com/user-attachments/assets/8eca1e4e-60d4-4ecd-b57b-5418c23dc2cc)
![Screenshot 2025-03-30 191609](https://github.com/user-attachments/assets/713602ec-3d9c-440a-a56c-aa9ea816eca9)
![Screenshot 2025-03-30 192410](https://github.com/user-attachments/assets/d7e2a2f6-8b0f-4f48-8dd4-b0f74eb58aac)

# Contact support 24/7.
![Screenshot 2025-03-30 191427](https://github.com/user-attachments/assets/b110836a-0186-499c-a08b-22a3d8e359ce)

# Key features:

Secure sign-in and login system.

Admin can add and manage products easily.

User and data security is guaranteed, with secure database software.

Large-scale order management system for smooth user experience.

Farmers can sell fresh, organic produce directly to various localities.

# How to Execute
Follow these steps to run the Fresh Fields project locally on your machine.

# Prerequisites
Before running the project, ensure you have the following installed:

Python 3.12 – A programming language to run the backend server.

PostgreSQL – The database used to store user and product information.

pip – Python package installer (usually comes with Python).

# Step 1: Clone the Repository
First, clone the repository to your local machine:

git clone https://github.com/akankshakuwar/django-ecommerce-organic-food
cd fresh-fields

# Step 2: Install Dependencies
Use pip to install the required Python packages.

# Step 3: Set Up the Database
Create a PostgreSQL database for the project:

Log in to PostgreSQL:



psql -U postgres
Create a database for your project:

sql

CREATE DATABASE fresh_fields;
Exit PostgreSQL:

sql

\q
Configure the database settings:

In the project directory, navigate to fresh_fields/settings.py and configure the database settings according to your PostgreSQL configuration.

Example:

python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fresh_fields',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Step 4: Apply Migrations
Now, apply the necessary database migrations to set up the database schema:


python manage.py migrate

# Step 5: Create a Superuser (Optional)
To access the Django admin panel, you can create a superuser:


python manage.py createsuperuser
Follow the prompts to create the superuser credentials.

# Step 6: Run the Development Server
Start the Django development server to run the project:


organic python manage.py runserver
The application will now be accessible in your browser at http://127.0.0.1:8000.

# Step 7: Access the Application
User Frontend: Go to http://127.0.0.1:8000 to start browsing and interacting with the platform.

Admin Panel: To access the Django admin panel, go to http://127.0.0.1:8000/admin and log in using the superuser credentials you created.

# Troubleshooting
If you encounter any issues during setup, here are some common solutions:

Database connection errors: Double-check your PostgreSQL settings and ensure your database is created correctly.

Missing dependencies: Ensure you've run pip install -r requirements.txt to install all required Python packages.

Port already in use: If port 8000 is already being used, you can change the port by running:


organic python manage.py runserver 8080

# How I Built It
This project was built using the following technologies:

Backend: Python (Django Framework)

Database: PostgreSQL

Frontend: HTML, CSS, Bootstrap, JavaScript

As this was my first time working with Python and Django, I invested time studying and researching the frameworks to understand the concepts better. Throughout the process, I gained valuable experience in backend and frontend development, making it an enriching learning experience.



