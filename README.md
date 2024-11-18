# PP4-Django-Project - Golf Booking System

![Screenshot of the home page of the site](static/images/homepage.png)

## Site Introduction
I have created this golf booking system site as I play and enjoy golf myself. I like to create my projects around my own personal interests as I am able to put more into it and always want to add more features to improve it. The site is a place where users can book a tee time to play a round of golf, add players too, change the date/time and cancel bookings. The project utilites Django, Bootstrap, HTML Templates, CSS and Python code to allow the user to book a time, edit their booking, cancel their booking and upload scores to the leaderboard. The project has an admin account linked which can select what dates and times are available for users to book.

- Burch's Golf Club/Course does not actually exist it is made up using my surname for the purpose of this project.

## Project Planning
Prior to starting this project deciding what to base it on was hard as I had many options such as; restaurant booking system, car sale/buying site and a golf booking system/website for a golf club. I have always played golf and enjoyed it, other projects have been based on my other interests so I thought it was only right to carry on that theme. It really helps me when creating my projects to do this as I can share my love and passion for my interests through my work. I set out to begin deciding what needed to be on the site by drawing out a flow chart with a pen and paper to help me understand what I needed on/from my site. I then began to create my user stories/issues to really understand the needs of both the user and admin. The site needed to include a booking system which only allows a person to book if they have an account registered, a leaderboard for the users to upload their score, a 'profile' so that a user can sign in and manage their bookings and also view previous bookings. 

## User Experience (UX)

### User Needs
- The Burch's Golf Club website needs to allow a site user to create and account to make, manage and view their tee time bookings.
- It must be clear and easy to navigate.
- A site user must be able to find the address and map location of the golf course.
### Colour Scheme
- I decided to use a green/white colour scheme for this project as I think they compliment one another nicely. This creates a great user experience as everything is clear and easily readable. For an unknown reason when doing lighthouse tests on my home page it suggests the the white over the green background is not a good enough contrast, however, this issue does not appear when testing any other pages. I have also recieved many opinions from friends and family to query whether or not they think it is a good contrast and the general response is that the colours are clear against one another.
- I also decided to use green as it is a very fitting colour to use when considering that the site is used for booking a round of golf.

### Using Bootstrap
- I decided to import a basic bootstrap navbar from the bootstrap website then modify it to the needs of my site.

### Images
- All images used on this site are from google images and are random courses as Burch's Golf Course does not exist.

## Features


## Using Agile

## Testing

| What I am testing? | How I tested it| Expected Outcome | Result |
| -- | -- | -- | -- |
| What I am testing? | How I tested it| Expected Outcome | Result |
| What I am testing? | How I tested it| Expected Outcome | Result |
| What I am testing? | How I tested it| Expected Outcome | Result |
| What I am testing? | How I tested it| Expected Outcome | Result |


## Bugs and Fixes

- I had a problem when making my django models for making a booking where once a user had filled out the booking form it was not saving properly to the database and creating the booking, this made me rethink and rewrite my code for the whole booking process to solve it. Once I had re written the code it was working how I wanted it too.

### Problems I Had
- Getting the 'book' submit button on the create_booking form view to work, I was able to create/add a booking in the admin view and have it display in the my bookings section when a user was logged in but not able to save a booking correctly when signed in on the 'book a tee' page. 

### Deployment

<!-- These are the steps I followed to deploy my live project
- Firstly I had to type 'pip3 freeze > requirements.txt' into the terminal in my code space to add the requirements for Heroku to download to run my program so that it works.
- Next I went onto the Heroku website, went to my dashboard and selected 'Create New App' from the 'New' dropdown menu in the top right.
- I then named my app and selected 'create new app' to continue, I then selected the settings tab
- Next I selected the deploy tab, I then linked my github profile and searched for my project repository and linked it ready for deployment.
- Finally I opted to have automatic deploys so that my live program updates each time I push my code to github. I then clicked deploy branch to get my live site. -->

Link to the live site : https://pp4-django-project-082841c8663e.herokuapp.com/

## Using Django
- Talk about how I decided to change my models completely and struggles with having to change all of the code that linked together to get it to the front end as I could not figure out how to get the bookings to post/save to the backend without use of the admin panel.
- Talk about how I then had to add an edit button to allow users to edit their booking

### Django Models
- I have a django model that I have created myself that allow an admin to select dates that are available for booking via the admin panel, once the dates have been added to the database any user is then able to see them on a drop down menu when creating a booking.
- I also have another django model created by myself which allows a user to select a time from 4 different time slots to create a booking, these bookings can be viewed when logged in.

### Django Views





## Future Enhancements

