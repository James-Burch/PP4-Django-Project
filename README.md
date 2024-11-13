# PP4-Django-Project - Golf Booking System

## Site Introduction
I have created this golf booking system site as I play and enjoy golf myself. I like to create my projects around my own personal interests as I am able to put more into it and always want to add more features to improve it. The site is a place where users can book a tee time to play a round of golf and share their scores from the round to compare to other users. The project utilites Django and Python code to allow the user to book a time, edit their booking, cancel their booking and upload scores to the leaderboard. The project has an admin account linked which can select what dates and times are available for users to book, once the time has been booked it can not be booked by another user. Once the user has finished their round they can upload the score they got on their round to be displayed on the leaderboard. 

- Burch's Golf Club/Course does not actually exist it is made up using my surname for the purpose of this project.

## Project Planning
Prior to starting this project deciding what to base it on was hard as I had many options such as; restaurant booking system, car sale/buying site and a golf booking system/website for a golf club. I have always played golf and enjoyed it, other projects have been based on my other interests so I thought it was only right to carry on that theme. It really helps me when creating my projects to do this as I can share my love and passion for my interests through my work. I set out to begin deciding what needed to be on the site by drawing out a flow chart with a pen and paper to help me understand what I needed on/from my site. I then began to create my user stories/issues to really understand the needs of both the user and admin. The site needed to include a booking system which only allows a person to book if they have an account registered, a leaderboard for the users to upload their score, a 'profile' so that a user can sign in and manage their bookings and also view previous bookings. 

## Using Django

### Django Models
- I have a django model that I have created myself that allow an admin to select dates that are available for booking via the admin panel, once the dates have been added to the database any user is then able to see them on a drop down menu when creating a booking.
- I also have another django model created by myself which allows a user to select a time from 4 different time slots to create a booking, these bookings can be viewed when logged in.

### Django Views


### Problems I Had
- Getting the 'book' submit button on the create_booking form view to work, I was able to create/add a booking in the admin view and have it display in the my bookings section when a user was logged in but not able to save a booking correctly when signed in on the 'book a tee' page. 

### Using Bootstrap
- I decided to import a basic bootstrap navbar from the bootstrap website then modify it to the needs of my site.

### Images
- All images used on this site are from google images and are random courses as Burch's Golf Course does not exist.

### Colour Scheme
- I decided to use a green/white colour scheme for this project as I think they compliment one another nicely. This creates a great user experience as everything is clear and easily readable.
- I also decided to use green as it is a very fitting colour to use when considering that the site is used for booking a round of golf.