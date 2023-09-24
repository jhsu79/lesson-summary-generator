# The Lesson Summary Generator
 
## Project Summary 
<b>The Lesson Summary Generator (LSG)</b> is a tool for a user (likely an instructor, teacher, or a tutor) to create a list of students and list of concepts the instructor will cover. The user can then use a form to enter a student's performance on homework, the concepts covered during the lesson, and assignments for the next lesson. Using that form, LSG will create summaries using OpenAI. Ultimately, these summaries can then be modified or edited for clarity or length as needed. 

## Technologies Used 
1. Django 
1. OpenAI 
1. React 

## Wireframes: 


## Relevant Links: 
Link to GitHub Repo: https://github.com/jhsu79/lesson-note-generator

Link to API Documentation: https://platform.openai.com/docs/api-reference

## Models: 


## Basic ERD:  

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

## Links to documentation for Stretch Goals: 
