<h1>ByteBites Restaurant</h1>
<h2> Deployed Project : https://bytebites-c7354208ea8f.herokuapp.com/ </h2>


<h2>1. Purpose of the Project</h2>
<p>The purpose of this project is to create an efficient and user-friendly restaurant website that enhances the dining experience for customers. It aims to provide a platform for users to easily make reservations, explore the menu, and order online while allowing restaurant staff to efficiently manage bookings and menu items. Ultimately, the project seeks to streamline restaurant operations and improve customer engagement.</p>


<h1> Wireframes </h1>

<h3> PC View Not Logged in </h3>

![NotLoggedPC](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/4dddb484-e024-41f0-b945-2d02d76b6b55)

<h3> Phone View Not Logged in </h3>

![NotLoggedPhone](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/eb1bdab9-c6a6-463d-ae77-bd0a8bd67ee5)

<h3> PC View Logged in </h3>

![LoggedPC drawio](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/6c85fa6c-06ee-4825-996a-b446f1387dd3)

<h3> Phone View Logged in </h3>

![LoggedPhoneHome](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/d59c620b-163b-4030-aaf5-06f5ed68844b)

<h3> My Bookings PC View </h3>

![MYBOOKINGSPC (1)](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/7cbea5ee-fca0-4d8f-8c7d-840369933f7d)

<h3> My Bookings Phone View </h3>

![PhoneMyBookings](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/a88f40cb-6339-4d92-8b8a-5fa903e6697c)

<h1> Entity & Relationship Diagram </h1>

![ERDIAGRAM drawio](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/15e64b4a-c75d-4aee-8be5-13887d8ad823)



<h2>2. User Stories</h2>

  
 <em> As a Guest User (Non-Logged In): </em>
<ul> 
<li>As a guest, I want to access the registration and login pages to create an account or log in.</li>
<li>As a guest, I want to access the restaurant menu.</li>
</ul>

 
<em> As a Registered User (Logged In): </em>
<ul>
<li>As a registered user, I want to log in using my credentials.</li>
<li>As a registered user, I want to view my booking history and upcoming reservations.</li>
<li>As a registered user, I want to edit or cancel my existing bookings.</li>
</ul>
<em> As a Restaurant Staff Member (Admin): </em>
<ul>
<li>As a staff member, I want to access the admin panel to manage bookings and reservations.</li>

  ![image](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/54ac56c4-b8ce-495f-a1e7-4110565102bb)

</ul>
<h2>3. Features</h2>
<ul>
  <li>User-friendly navigation menu</li>

  ![Screenshot 2024-01-17 at 21 41 46](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/0d97704e-f801-4508-96a3-446edfd084fb)

  <li>Responsive design for mobile and desktop</li>

![Untitled-1](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/8d610cf7-ba23-4b8b-a5ec-094da48e0371)
  
  <li>User registration and login</li>

![Screenshot 2024-01-17 at 21 43 56](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/847506a5-6fe8-4f6d-9538-707284edea00)

  
  <li>View and manage bookings</li>

![Screenshot 2024-01-17 at 21 44 52](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/1c838522-f981-4b67-91bf-d8d2da7e186f)

  
  <li>Booking confirmation and cancellation</li>

  ![Screenshot 2024-01-17 at 21 44 38](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/6b47d49e-5b57-465f-8dc9-268f74b426dd)

  <li>Integration of restaurant menu</li>
  
![Screenshot 2024-01-17 at 21 45 13](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/8c2edd7f-cd22-40d5-9fa1-1cd1132ab7ef)

  
</ul>
<h2>4. Future Features</h2>
<ul>
 <li>Review and rating system</li>
  <li>Search and filtering options</li>
  <li>Online ordering and payment processing</li>

  
 </ul>
<h2>5. Technology</h2>
<ul>
  <li> GitHub</li>
  <li> CodeAnywhere</li>
  <li> Heroku</li>
  <li>ElephantSQL</li>
</ul>
<h2>6 Testing</h2>

<h3> 6.1 Manual Testing </h3>

| Test                | Expected Result              | Actual Result                | Resolved by          |
|---------------------|------------------------------|------------------------------|----------------------|
| Booking the same date twice or more         | Throw an error for booking already exists | Users could book the same date over and over again  | Added overlerlapping booking validation in the function in Booking app. This Date already exists message was introduced    |
| Booking a date in the past      | Show only the date from the current date onwards | Users could book dates in the past  | Added JS script to get the current day data and to show date from the current date onwards    |
| User to be able to update booking dates  | Update the date and redirect back to My Bookings | Date would get updated but it wouldn't redirect back to My Bookings  | Return redirect had a wrong argument. Once fixed, it worked perfectly     |


<h3> 6.2 Test Cases (User Story Based with Screenshots)</h3>
<ul>
  <li> As a user I'd like to be able create an account and make a booking </li>
  
  ![image](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/9766834d-75fc-4ee5-872c-91d71b271e6e)

  <li> As a user I'd like to be able to log into my account </li>
  
  ![image](https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/3a852726-3f58-46be-b076-2009c96b9280)

  <li> As a user I'd like to be able to see, update and delete my bookings </li>

  <img width="1159" alt="Screenshot 2024-01-17 at 22 19 38" src="https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/0c97790e-05e7-44a6-8036-5660fd292d2f">


<h2> 6.3 Validator Testing </h2>
<h3> HTML Validator </h3>
<img width="1952" alt="Screenshot 2024-01-17 at 22 15 03" src="https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/249923e3-5e53-42fa-864a-a23baface263">
<h3> CSS Validator </h3>

<img width="1987" alt="image" src="https://github.com/AEmin96/Project4-CI-ByteBitesWebsite/assets/126208272/4dae6325-97a2-43a5-8fdd-545189317235">

  
</ul>
<h3> 6.4 Fixed Bugs</h3>
  <li> Added validator for the date in My Bookings as users could choose dates in the past </li>
  <li> There was a line in base.html that was missing a closing tag. This was fixed after the validator check </li>
  <li> DEBUG mode was TRUE when the page was deployed the first time. This was fixed in the most current deployment </li>
 
<h3>7. Deployment </h3>
<h4> This project was deployed to Heroku using these steps: </h4>
1. Fork or clone this repository  <br>
2. Create a new Heroku app  <br>
3. Set the buildpacks to Python  <br>
4. Set the config vars for your database connection and API keys  <br>
4. Link the Heroku app to the repository  <br>
5. Click on deploy  <br>

<h3> 8. Credits</h3>
Code Institute
