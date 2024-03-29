# 🚀Dwitter(Twitter clone) Django App

## Acknowledgements
- This project is a part of the [Gaza Sky Geeks ](https://gazaskygeeks.com/) Training program.
<p align="center">
<img src="https://gazaskygeeks.com/wp-content/uploads/2020/05/gsg-website-logo-colored-280-50.png" width="40%">
</p>

## Introduction
💻 Building a social network web application using the Django framework. 
The focus of this project is to showcase the use of Django models, forms, and the implementation of user-to-user connections and text-based content creation and display.

## Features 🎉
 - 🔗 User-to-user connections: Allows users to connect with each other by following or unfollowing other user profiles.
 - 📝 Content creation and display: Users can post short text-based messages and view the posts of other user profiles they follow.
 - 👥 User profiles: Each user will have their own profile that holds information about which other profiles they follow.
 - 🔒 User authentication: Users can log in and log out and also register as a new user.
 - 👀 Profile information display: Users can view their own profile and the profiles of other users.
 - 💬 Comments: Users can comment on other users' posts.

## Technical Analysis
💻 The application consists of the following components:
  - Models: The main models used in this application are the User, Profile, and Dweet models.
  - Views: The views handle the CRUD operations for the models and also handle user authentication and registration.
  - Templates: The templates handle the display of the content and information in the application.
  - Forms: Forms are used for submitting content and handling user authentication and registration.
  - Signals: Signals are used to automatically create a profile for each new user.

## Back-end
- The back-end of the application is built using Django (Python Framework)

## Frontend
- The frontend of the application is built using Bulma CSS Framework for styling and HTML for the structure.
- The dynamic content is generated using Django template code.

## Requirements 🔧
Django 💻
Python 🐍
SQLite 🗄️

## Usage

To use this dwitter app, follow these steps:

1. Clone the repository to your local machine: 
`git clone https://github.com/Mahmoud-Hijjeh/dwitter_app_django.git`.
2. Create a virtual environment: `python3 -m venv venv`.
3. Activate the virtual environment: `source venv/bin/activate`.
4. Install the required packages with `pip install -r requirements.txt`.
5. Apply migrations: `python manage.py migrate`.
6. Run the development server with `python manage.py runserver`.
7. In your web browser, go to `http://127.0.0.1:8000/` to access the app.

## License
This project is licensed under the MIT License.

## Conclusion
🎉 This project provides a good introduction to building a social network application using the Django framework. It showcases the use of models, views, templates, forms, and signals in a Django application and provides a solid foundation for building more complex applications in the future.

## Images
![1](https://user-images.githubusercontent.com/107920651/218224592-a3fc4487-bb36-487d-9c34-0b10bfe63010.PNG)
![2](https://user-images.githubusercontent.com/107920651/218224598-a2c5468d-0fe0-4d0f-a7e6-922da7665464.PNG)
![3](https://user-images.githubusercontent.com/107920651/218224609-3a6d10cb-fb69-448c-a6ad-ddcb15a570d7.PNG)
![4](https://user-images.githubusercontent.com/107920651/218224616-f21766ff-125a-4a66-9285-b371a4f3d827.PNG)
![5](https://user-images.githubusercontent.com/107920651/218224625-9e1622ba-ce66-4044-a0fb-30244a6d606e.PNG)
![6](https://user-images.githubusercontent.com/107920651/218224630-acd5d2f1-1690-4c5a-a2d4-917bb1a95720.PNG)
![7](https://user-images.githubusercontent.com/107920651/218224639-b9346b4d-7977-43b4-8b29-c4c97fbaf09a.PNG)
![8](https://user-images.githubusercontent.com/107920651/218224646-d32d2120-8227-476c-a410-aee7abbb746e.PNG)
![9](https://user-images.githubusercontent.com/107920651/218224657-00c808ec-b9c9-406d-b6ab-0bc3e5ca9c17.PNG)
![10](https://user-images.githubusercontent.com/107920651/218224669-d6bb3ebd-e4a1-4011-b2d0-bdf381acc0b9.PNG)
