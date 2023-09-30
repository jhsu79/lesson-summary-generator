#[Lesson Summary Generator](https://dashboard.heroku.com/apps/lessonsummarygenerator)

## Project Description: 
Lesson Summary Generator is a responsive web application that offers educators an integrated platform where they can effortlessly create student rosters, outline detailed concepts to be covered, record homework performance, document lesson discussions, and assign future tasks with ease. Leveraging the power of OpenAI, LSG provides instant AI-powered summaries, significantly reducing time and effort spent on manual summarization tasks. Furthermore, LSG empowers instructors to tailor these summaries to their unique teaching styles and objectives, ensuring optimal alignment with their students' needs. This project reimagines educational workflows, making them more efficient, effective, and adaptable to individual teaching philosophies.


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
 
### Concepts 
1. To add a concept, click on ``add concept`` in the navigate menu or the home page. 
    a. On the form, provide a name for the concept(required),
    b. Provide a description for the concept (250 words or less). 
    c. Add keywords associated with the concept (optional) 
2. To view a list of all your concepts, click on the ``all concepts`` in the navigate menu or the home page. 
3. To view the details of an individual concept, click on the name of the concept on the ``all concepts`` page. 
4. To edit/delete the concept, click the corresponding button. 
5. After editing the concept, make sure to click save.   
     
<i>Please note that in order to generate a lesson note and summary, you can create a concept first or pull from an existing concept. Also note that concepts are currently shared among <b>all</b> users.</i> 

### Students 
1. To add a student, click on ``add student`` in the navigate menu or the home page. 
    a. On the form, provide the student's first name and last name for the concept(required),
    b. Select the program type: 1-on-1 tutoring, small group, or classroom. 
    c. Select your username to ensure that it saves to your account. 
        <i>Please that <b>ALL</b> users can currently view all other users and save students to their account. Future updates will address this issue.</i>
2. To view a list of all your stduents, click on the ``all students`` in the navigate menu or the home page. 
3. To view the details of an individual student and the last three existing lesson summaries, click on the name of the concept on the ``all students`` page. 
4. On the student's page, you can edit/delete the student's details by clicking the corresponding button. 
5. After editing the student, make sure to click save.        
    <i>Please note that in order to generate a lesson note and summary, you can create a concept first or pull from an existing concept. Also note that concepts are currently shared among <b>ALL</b> users.</i> 

### Lesson Notes and Summaries. 
1. From the student's details page, you can view existing lesson summaries. 
1. To generate a new summary, click on the ``enter a new lesson note`` button.
    a. On the lesson note page, fill in the form. 
    b. Make sure to leave the lesson summary blank.  
    1. Click ``save and generate summary`` to create a lesson summary. 
    1. 



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
        1. Enter your OPEN_AI_KEY. If you do not have one, you will need to sign up for one and create a paying account. 
8. In the terminal, type python3 manage.py runserver.