#[Lesson Summary Generator](https://dashboard.heroku.com/apps/lessonsummarygenerator)
Created by Joshua N Hsu
[GitHub](https://github.com/jhsu79) | [Linkedin](https://www.linkedin.com/in/joshuanhsu/) | [Portfolio](https://joshuahsu.netlify.app/)

## Project Description: 
Lesson Summary Generator is a mobile-ready, responsive web application that offers educational professionals an integrated platform where they can effortlessly create student rosters, outline detailed concepts to be covered, record homework performance, document lesson discussions, and assign future tasks with ease. Leveraging the power of OpenAI, LSG provides instant AI-powered summaries, significantly reducing time and effort spent on manual summarization tasks. Furthermore, LSG empowers instructors to tailor these summaries to their unique teaching styles and objectives, ensuring optimal alignment with their students' needs. This project reimagines educational workflows, making them more efficient, effective, and adaptable to individual teaching philosophies.

## Screenshots
<img width="500" alt="Screenshot 2023-09-29 at 10 18 04 PM" src="https://github.com/jhsu79/lesson-note-generator/assets/137417888/ebf57290-65ce-45b9-9b70-97ffd9fc1d0f">
<img width="500" alt="Screenshot 2023-09-29 at 10 18 04 PM" src="https://github.com/jhsu79/lesson-note-generator/assets/137417888/6939bc24-7b7c-4e57-84c8-aec332d51e76">
<img width="500" alt="Screenshot 2023-09-29 at 10 18 37 PM" src="https://github.com/jhsu79/lesson-note-generator/assets/137417888/c0959e62-dc2d-4f96-bd7e-99427ba340e1">

## How to use Lesson Summary Generator 
1. Click [here](https://dashboard.heroku.com/apps/lessonsummarygenerator
) to access the site.  
2. Once the page has loaded, if you do not have an account, ``sign up`` for an account. After sign up, you will be automatically logged in. 
3. If you have an account, ``log-in`` to access the page. 
4. Once logged in, you can do any of the following from the navigation menu or the home page:
    - ``Add a concept``
    - ``Add a student`` 
    - ``View all your students``
    - ``View all concepts`` 
 
#### Concepts 
1. To add a concept, click on ``add concept`` in the navigate menu or the home page. 
    a. On the form, provide a name for the concept(required),
    b. Provide a description for the concept (250 words or less). 
    c. Add keywords associated with the concept (optional) 
2. To view a list of all your concepts, click on the ``all concepts`` in the navigate menu or the home page. 
3. To view the details of an individual concept, click on the name of the concept on the ``all concepts`` page. 
4. To edit/delete the concept, click the corresponding button. 
5. After editing the concept, make sure to click save.   
     
<i>Please note that in order to generate a lesson note and summary, you can create a concept first or pull from an existing concept. Also note that concepts are currently shared among <b>all</b> users.</i> 

#### Students 
1. To add a student, click on ``add student`` in the navigate menu or the home page. 
    a. On the form, provide the student's first name and last name for the concept(required),
    b. Select the program type: 1-on-1 tutoring, small group, or classroom. 
    c. Select your username to ensure that it saves to your account. 
        <i>-Please note that <b>ALL</b> users can currently view all other users and save students to their account. Future updates will address this issue.</i>
2. To view a list of all your stduents, click on the ``all students`` in the navigate menu or the home page. 
3. To view the details of an individual student and the last three existing lesson summaries, click on the name of the concept on the ``all students`` page. 
4. On the student's page, you can edit/delete the student's details by clicking the corresponding button. 
5. After editing the student, make sure to click save.        
    <i>-Please note that in order to generate a lesson note and summary, you can create a concept first or pull from an existing concept. Also note that concepts are currently shared among <b>ALL</b> users.</i> 

#### Lesson Notes and Summaries. 
1. From the student's details page, you can view existing lesson summaries. 
2. To generate a new summary, click on the ``enter a new lesson note`` button.
    a. On the lesson note page, fill in the form. As you do so, please keep in mind the following.      
    1.  You can only select the student that is provided.
    1. Enter the month, date, year as MM/DD/YYYY.  
    1. For accuracy level, we recommend you use a percentage but you may use words. 
    1. For concepts, you may select as many as you need. 
    1. For all comments, feel free to be as descriptive or brief as needed. 
    1. Private notes are necessary.  
    1. Structure the homework as an ordered list.   
    1.  Make sure to <b>leave the lesson summary blank.</b>  
1. Click ``save and generate summary`` to create a lesson summary. 
1. Once the summary has been generated, you can view and edit the notes and summary. 
    <i>-Please note that the summary will not generate only once.</i>
1. You can also delete the notes and summary with the corresponding button.
    <i> -Please note that this action cannot be undone. </i>
1. You can now view all saved summaries on the student's detail page. 

## Technologies Used & Documentation  
1. [Python](https://www.python.org/doc/)
2. [Django](https://docs.djangoproject.com/en/4.2/)  
3. [PostgreSQL](https://www.postgresql.org/docs/)
4. [OpenAI API](https://platform.openai.com/docs/)
5. [Bootstrap (CSS Framework)](https://getbootstrap.com/docs/5.3/getting-started/introduction/)


## Instructions to use your own version of LSG    
1. Clone a copy of this repository. 
2. Ensure that you have Python and Django installed. 
3. Create a PostgreSQL database. 
4. In the shell, ensure that your database is linked to the local PostgreSQL database. 
5. Install the following dependencies: 
        a. OpenAI  
        b. Python dotenv 
6. Ensure that all other dependencies are present. 
7. Touch a dotenv file. 
        1. Enter the local django SECRET_KEY. 
        1. Enter your OPEN_AI_KEY. If you do not have one, you will need to sign up for one and provide a credit card. 
8. Create a superuser in the terminal.
9. In the terminal, type ``python3 manage.py runserver``.
10.  Ensure that your credentials work at localhost:8000/admin.
11. If desired, Modify the ``max_tokens`` for the summaries in ``main_app/views.py`` as needed. It is currently set to the maximum. For more info about the appropriate number of tokens and billing, view the [documentation]((https://platform.openai.com/docs/)).

## Future Features 
as of 10/1/2023

#### Planned Structural Changes.  
1. Include a Front-end [REACT Framework](https://react.dev/) and switch to a [Django REST Framework](https://www.django-rest-framework.org/). 
1. Explore the use of [Tailwind CSS Framwework](https://tailwindcss.com/) and [Sass](https://sass-lang.com/) for more direct CSS customization.
1. Explore integration of [Grammarly API](https://developer.grammarly.com/) when writing concepts or editing notes 

#### Quality of Life Improvements 
1. Update the student form view to only allow for the current user to be selected. 
2. Update the student detail view to include concepts covered from previous lessons.  
3. Update the student model to include more details about the student. 
4. Update the student detail view to offer pagination. 
5. Allow users to search for concepts using keywords. 
6. Finesse the inputs for the lesson note form and finesse the prompt for the summary. 
7. Include calendar widgets. 
8. Allow users to provide direct links to homework. 
9. Upgrade accessibility features. 
10. Adding grammar, tone and style buttons that can prompt the LSG to revise summaries based on the preferences of the instructor and needs of the student's families

#### Want to contribute to this project? 
Contact me on [GitHub](https://github.com/jhsu79) or on [Linkedin](https://www.linkedin.com/in/joshuanhsu/)
