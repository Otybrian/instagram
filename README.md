## Instagram
## Author

Brian Otieno

## Description
This is a clone of Instagram where people share their images for other users to view. Users can sign up, login, view and post photos, search, follow and follow other users.

## User Story
Sign in to the application to start using.
Upload a pictures to the application.
Search for different users using their usernames.
See your profile with all your pictures.
Follow other users and see their pictures on my timeline.

## Screenshots
### homepage
![home](https://user-images.githubusercontent.com/93243367/161722539-e658a6d5-2795-4866-8845-3f4c74f0a0a6.png)

### login page
![login](https://user-images.githubusercontent.com/93243367/161722672-bffe4b17-9727-4904-9cc2-8928e31d3e8a.png)

### page for posting
![post-details](https://user-images.githubusercontent.com/93243367/161722703-f437bc6f-3cd1-4b91-a5fb-08ab6b4d1897.png)

### profile page
![profile](https://user-images.githubusercontent.com/93243367/161722744-36e767b8-c5d9-4193-a083-2458c7458f91.png)

## Setup and Installation
To get the project .......

## Cloning the repository:
https://https://github.com/Otybrian/instagram.git 
Navigate into the folder and install requirements
cd insta pip install -r requirements.txt 
Install and activate Virtual
- python3 -m venv virtual - source virtual/bin/activate  
Install Dependencies
pip install -r requirements.txt 
Setup Database
SetUp your database User,Password, Host then make migrate

python manage.py makemigrations instagram
Now Migrate

python manage.py migrate 
Run the application
python manage.py runserver 
Running the application
python manage.py server 
Testing the application
python manage.py test 
Open the application on your browser 127.0.0.1:8000.

## Technology used
Python3.8
Django 2.0
Heroku

## Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug

## License
This is under MIT License
