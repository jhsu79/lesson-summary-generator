# The Lesson Summary Generator
 
## Project Summary 
<b>The Lesson Summary Generator (LSG)</b> is a tool for a user (likely an instructor, teacher, or a tutor) to create a list of students and list of concepts the instructor will cover. The user can then use a form to enter a student's performance on homework, the concepts covered during the lesson, and assignments for the next lesson. Using that form, LSG will create summaries using OpenAI. Ultimately, these summaries can then be modified or edited for clarity or length as needed. 

## Technologies Used 
1. Django 
1. OpenAI 

## Wireframes: 
<img width="500" alt="Screenshot 2023-09-23 at 11 46 33 PM" src="https://github.com/jhsu79/lesson-note-generator/assets/137417888/9244c54c-563e-4616-a74d-7d8f0bc9dec2">
<br>
<img width="500" alt="Screenshot 2023-09-23 at 11 46 39 PM" src="https://github.com/jhsu79/lesson-note-generator/assets/137417888/fd12af44-91ef-4dc5-9132-5952fd431bab">
<img width="500" alt="Screenshot 2023-09-23 at 11 38 22 PM" src="https://github.com/jhsu79/lesson-note-generator/assets/137417888/eedc0658-54e5-4398-9507-354e273e1b95">
<img width="500" alt="Screenshot 2023-09-23 at 11 38 52 PM" src="https://github.com/jhsu79/lesson-note-generator/assets/137417888/0cf27143-4e91-4282-8fd3-3c80d935f124">
<img width="500" alt="Screenshot 2023-09-23 at 11 38 32 PM" src="https://github.com/jhsu79/lesson-note-generator/assets/137417888/d79a9f0e-0891-4670-b2c0-fb0e10fedad9">
<img width="500" alt="Screenshot 2023-09-23 at 11 39 02 PM" src="https://github.com/jhsu79/lesson-note-generator/assets/137417888/9961cfc0-6ab9-463f-93aa-dfbf6f3bc073">
<img width="500" alt="Screenshot 2023-09-23 at 11 39 09 PM" src="https://github.com/jhsu79/lesson-note-generator/assets/137417888/d6679e53-4460-40e6-9323-7188197aa601">


Link to Wireframes: https://lucid.app/lucidspark/db9dd6dc-0323-49a8-9144-aee51fee253f/edit?page=0_0&invitationId=inv_9f52bceb-7de6-4005-bc8d-0ad7ce572c8a#

## Relevant Links: 
Link to GitHub Repo: https://github.com/jhsu79/lesson-note-generator

Link to API Documentation: https://platform.openai.com/docs/api-reference

## Models
| Instructor    | Type Of Data  |
|---------------|---------------|
| instructor_id | id            |
| first_name    | CharField     |
| last_name     | CharField     |

| Student          | Type of Data |
|------------------|--------------|
| student_id       | id           |
| last_name        | CharField    |
| graduation_year  | DateField    |
| program_type     | TextField    |

| Concept                       | Type of Data |
|-------------------------------|--------------|
| concept_id                    | id           |
| concept_mame                  | CharField    |
| concept_description           | TextField    |

| Lessons               | Type of Data              |
|-----------------------|---------------------------|
| lesson_id             | id                        |
| instructor_id         | instructor_id             |
| student_id            | student_id                |
| lesson_date           | DateField                 |
| hw_completed_lvl      | NumField                  |
| homework_accuracy_lvl | NumField                  |
| homework_notes        | TextField                 |
| concept1              | concept_id (Select from)  |
| concept2              | concept_id (Select from)  |
| concept3              | concept_id (Select from)  |
| concept1_notes.       | Text Field                |
| concept2_notes.       | Text Field                |
| concept3_notes.       | Text Field                |
| hw_assigned           | BooleanField              |
| next_homework         | TextField                 |
| next_lesson_date      | DateField                 |

| Lesson Summaries   | Type of Data   |
|--------------------|----------------|
| lesson_summary_id  | id             |
| lesson_id          | lesson_note-id |
| instructor_id      | instructor_id  |
| student_id         | student_id     |
| concept_id         | concept_id     |
| homework_summary   | TextField      |
| concept_summary    | TextField      |
| assignments        | TextField      |
| next_homework      | TextField      |
| next_lesson_date   | TextField      |



## Basic ERD:  
![Lesson Note Generator](https://github.com/jhsu79/lesson-note-generator/assets/137417888/5086882a-21ac-42d9-aebb-def899ce355a)

## Routes
https://docs.google.com/spreadsheets/d/1J8kdKBCMRNBt6ToQFSdZv2q6IDWnzzFOg8Q9sNNe7yA/edit#gid=1241829581
## User Stories: 
There are four layers to the stories: concepts, students, lesson notes, 

#### (A) Concepts
- As a user, I want to be able to add a concept (alongside a description of that concept) to a list that I will later reference in my lesson notes.  
- As a user, I want to be able to edit the title or description of that concept or delete the concept (and any associated content), 

#### (B) Students
- As a user(AAU), I want to be able to add a student to my student list. 
- AAU, I want to edit the students details.  
- AAU, I want to view a list of all my students students. 
- AAU, I want to view the details of a specific student and any lesson summaries associated with that student.  

#### (C) Lesson Notes 
- AAU, I want to to view a form where I can quickly summarize my impressions of a lesson, including a student's performance on homework, the concepts covered during the lesson, and the student's assignments for the next lesson.  
- AAU, I want to be able to save and edit that form. 

#### (D) Lesson Summaries 
- AAU, I want to be able to use the saved note to generate a three-paragraph summary, highlighting the student's homework performance, the concepts covered, and assignments.  
- AAU, I want to save that content to the student's page.
- AAU, I want to be able to edit and update that summary. 
- AAU, I want to be able to delete both the lesson summary and corresponding lesson note. 

## Stretch Goals: 
1. OAuth that allows for multiple instructors 
2. Adding Subtopics with their own distinct keywords for Concepts. 
3. Refactor template components into React. 
1. Adding grammar, tone and style buttons that can prompt the LSG to revise summaries based on the preferences of the instructor and needs of the student's families. 
1. Adding calendar widgets to date settings.    

## Links to documentation for Stretch Goals: 
1. OAuth: https://django-oauth-toolkit.readthedocs.io/en/latest/getting_started.html 
2. Calendar Widgets: https://forum.djangoproject.com/t/how-to-set-data-calendar-widget-for-datefield-and-datetimefield-with-format-day-month-year-dd-mm-yyyy/7243
