Name : SWARUPANANDA DAS

Company : CODTECH IT SOLUTIONS

ID : CT12DS1922

Domain : CYBER SECURITY & ETHICAL HACKING

Duration : July 20th 2024 to september 20th 2024

Mentor : MUZAMMIL AHMED










OVER VIEW OF PROJECT 

Project Name: PASSWORD STRENGTH CHECKER

Objective:
The purpose of this project is to develop a Python-based tool that assesses the strength of 
passwords entered by users. The tool analyzes factors such as length, complexity (presence of 
uppercase, lowercase, digits, and special characters), and uniqueness (no common weak 
passwords) to provide feedback and help users create strong passwords.


Key Features:

1. Password Analysis :
The tool assesses the password based on the following conditions:
  ⦁ Password length (must be at least 8 characters).
  ⦁ Must contain at least one uppercase letter.
  ⦁ Must contain at least one lowercase letter.
  ⦁ Must contain at least one digit.
  ⦁ Must contain at least one special character.
  ⦁ Must not be a common or weak password such as abcd1234, 123456, or abcdef etc.

2. User Feedback :
   The tool provides real-time feedback on each of the conditions. If a condition is not met, it 
   informs the user which part of the password is missing.

3. Retry Logic:
  After every password attempt, the user is asked if they want to try again. The user can enter a 
  new password if the previous one is weak, or exit the program if they do not want to continue.

4. Customizable Common Passwords:
  The tool checks against a predefined list of common weak passwords. This list can easily be 
  expanded or modified by changing the common_patterns list in the is_common_pattern 
  function.


How It Works :

1. Password Input:
  The user is prompted to enter a password.

2. Password Analysis:
  The tool evaluates the entered password by:
    ⦁ Checking if it meets the minimum length requirement.
    ⦁ Checking if it includes at least one uppercase letter.
    ⦁ Checking if it includes at least one lowercase letter.
    ⦁ Checking if it includes at least one digit.
    ⦁ Checking if it includes at least one special character.
    ⦁ Checking if it is not one of the common or weak passwords.
  
3. Feedback Display:
   The tool provides a feedback message showing which of the above conditions are satisfied (e.g., 
   Uppercase: yes, Lowercase: no).

4. Password Strength Assessment:
  If all the conditions are met, the password is deemed strong, and a success message is 
  displayed. Otherwise, the user is informed of the missing elements.

5.Retry Mechanism:
  The user is asked whether they want to try entering another password. If they choose yes, the 
  program loops back to step 1; otherwise, it exits.



Technologies Used :

Python: The project is developed in Python and makes use of basic functions and regular 
        expressions for pattern matching.
Regex: Regular expressions are used to match patterns in the password (e.g., checking for 
       uppercase, lowercase, digits, and special characters).

