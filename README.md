<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Bidding System | Bidnamic Full Stack Project</h3>

<div align="center">

</div>

---

<p align="center"> Bidding App with Authentication (Login, Signup & Profile update) & Bidding Creation, Viewing, Update, and Deletion
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

The following are the satisfied requirements:

### From Tasks
1. Create a multipart form wizard which collects the following data
2. Collect the data and insert into a database as a single entity.
3. Add validation.
  3. 1. Done
  3. 2. Done
  3. 3. Added validation for the following fields: firstname & lastname, city, state, telephone, dob (cannot be over 150 years old) 
4. Develop an HTML template to show applications which have been submitted and a way for them to be deleted.
  * Note: I listed out applications, and a way for them to be deleted for each user but I'm not sure if this is what you wanted

### From Bonuses

1. We really value neatness and things being put in place to aid local development and continuous integration.
  * Note: Did my best with the time I had to put things neatly but I appreciate that there is alot more that can be done from refracting PoV (Like proper renaming) 

2. Needless to say, we like tests.
  * Note: Added a test folder that tested some of the URLs & Views and the Model & Form
          I believe i have added some tests to demonstrate knowledge on the subject but if they were not enough, I'll be happy to add more.

3. Hooking up some authentication into the app would be nice.
  * Note: Added an account creation, login, and a profile editing feature.
  Also given to each user the ability to store and delete their own biddings

4. Making it look nice with a UI framework such as Twitter Bootstrap. 
  * Note: Used Bootstrap

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

```
Python
Django
```

### Installing & Running

A step by step series of examples that tell you how to get a development env running.


1. Create environment 
2. Install requirements.txt script
3. cd inside the bidnamic app
4. create superuser with 'py manage.py createsuperuser'
5. run 'py manage.py runserver'
6. use created login to use the app

I'm happy to record a video with the installation instructions.

## 🔧 Running the tests <a name = "tests"></a>

To run the tests make sure you're in the bidnamic folder then run 'py manage.py test'

### Break down into end to end tests

Tested the following:
1. 2 URLs to demonstrate knowledge of testing URLs
2. Bidding model to make sure user is added properly and to demonstrate knowledge of testing models
3. Views
  - Testing the listing of all biddings and
  - viewing single biddings
  - and the creation of new biddings
4. Forms
  - Bidding form valid
  - Bidding form invalid


These tests are in no way the final and enough number of tests that will be used in production. but they are to demonstrate ability to work with them

Did not implement integration testing.

## 🎈 Usage <a name="usage"></a>

Make sure everything is migrated.

Create a super user
use these details to use log in to program as admin
or
Run server and create account
then login
then edit profile

Then create bidding
then view bidding
then update bidding
then create another bidding
then view list of biddings

then logout
then create a new account
then log in with new account
then find that this account has no bidding
then create new bidding
then view list of bidding

then logout
then login with first account

then see different biddings.

## 🚀 Deployment <a name = "deployment"></a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using"></a>

- [SQlite] - Database
- [Django] - Server Framework

## ✍️ Authors <a name = "authors"></a>

- [@SalmanHussein](https://github.com/SalmanBiceps) - Idea & Initial work

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Thank you for the opportunity given to carry out this small project.
