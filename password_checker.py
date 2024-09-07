import re

# Function to check if the password contains a sequence like 'abcd', '1234', etc.
def is_common_pattern(password):
    common_patterns = ['abcd1234', '123456', 'abcdef', '1234abcd']
    return password in common_patterns


# Function to assess the password strength
def assess_password_strength(password):
    feedback = {
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "digit": False,
        "special_char": False,
        "common_pattern": False
    }
    
    # Check length at least 8 character
    if len(password) >= 8:
        feedback["length"] = True
    
    # Check uppercase letters
    if re.search(r'[A-Z]', password):
        feedback["uppercase"] = True
    
    # Check lowercase letters
    if re.search(r'[a-z]', password):
        feedback["lowercase"] = True
    
    # Check digits
    if re.search(r'[0-9]', password):
        feedback["digit"] = True
    
    # Check special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback["special_char"] = True
    
    # Check if password is a common pattern
    if not is_common_pattern(password):
        feedback["common_pattern"] = True

    # Return feedback dictionary
    return feedback


# Function to check if all conditions are met
def is_strong_password(feedback):
    return all(feedback.values())        # Return True only if all feedback conditions are True


# Function to display feedback
def display_feedback(feedback):
    print(f"Uppercase: {'yes' if feedback['uppercase'] else 'no'}")
    print(f"Lowercase: {'yes' if feedback['lowercase'] else 'no'}")
    print(f"Digit: {'yes' if feedback['digit'] else 'no'}")
    print(f"Special Character: {'yes' if feedback['special_char'] else 'no'}")
    print(f"Length (minimum 8): {'yes' if feedback['length'] else 'no'}")
   

    # Check if password is a common weak pattern
    if not feedback["common_pattern"]:
        print("The password is too common ('abcd1234', '123456', 'abcdef', '1234abcd')")


# Main function to handle the switch-case retry logic
def main():
    while True:     # Infinite loop to keep asking for password input
        password = input("Enter your password: ")
        feedback = assess_password_strength(password)
        
        # Display feedback
        display_feedback(feedback)
        
        # Check if password is strong
        if is_strong_password(feedback):
            print("\n======= Password is strong =======\n")
        else:
            print("\nPassword is not strong......! \nwhich filled you missed please used this filed and make strong and uniqu password .......! Please try again.\n")
        
        # Ask user if they want to try again
        retry = input("Would you like to try again? (yes/no): ").strip().lower()
        if retry != 'yes':   # If user does not want to retry, exit the loop
            break


if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly





