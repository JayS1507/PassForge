import random
import string
import re
import os
from datetime import datetime
import sys

def generate_password(length):
    """Generate a strong password of specified length."""
    if length < 8:
        return None, "Password length must be at least 8 characters."
    
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill remaining length with random characters
    all_chars = lowercase + uppercase + digits + special
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    # Shuffle the password
    random.shuffle(password)
    return ''.join(password), None

def check_password_strength(password):
    """Check the strength of a password and provide feedback."""
    feedback = []
    score = 0
    
    # Length check
    if len(password) < 8:
        feedback.append("Too short (minimum 8 characters).")
    else:
        score += 1
    
    # Character type checks
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Missing lowercase letters.")
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Missing uppercase letters.")
    
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Missing digits.")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Missing special characters.")
    
    # Determine strength
    if score == 5:
        strength = "Strong"
        if not feedback:
            feedback.append("Excellent! Meets all strength criteria.")
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    return strength, feedback

def save_password(password, purpose):
    """Save the generated password with purpose and timestamp."""
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open('passwords.txt', 'a') as f:
            f.write(f"{timestamp} | {purpose} | {password}\n")
        return True, "Password saved to passwords.txt"
    except Exception as e:
        return False, f"Error saving password: {str(e)}"

def retrieve_passwords(purpose):
    """Retrieve passwords by purpose from passwords.txt."""
    try:
        if not os.path.exists('passwords.txt'):
            return False, "No passwords saved yet."
        
        found = False
        results = []
        with open('passwords.txt', 'r') as f:
            for line in f:
                if purpose.lower() in line.lower():
                    results.append(line.strip())
                    found = True
        if found:
            return True, results
        else:
            return False, f"No passwords found for purpose: {purpose}"
    except Exception as e:
        return False, f"Error retrieving passwords: {str(e)}"

def main():
    """Main function with menu-driven interface."""
    while True:
        print("\n=== PassForge 🔒 ===")
        print("1. Generate a strong password")
        print("2. Check password strength")
        print("3. Retrieve saved passwords")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            # Generate password
            while True:
                try:
                    length = input("Enter password length (minimum 8): ").strip()
                    length = int(length)
                    break
                except ValueError:
                    print("Please enter a valid number.")
            
            purpose = input("Enter the purpose of this password (e.g., Email): ").strip()
            if not purpose:
                purpose = "General"
            
            password, error = generate_password(length)
            if error:
                print(f"Error: {error}")
            else:
                print(f"\nGenerated Password: {password}")
                print(f"Purpose: {purpose}")
                # Save password
                success, message = save_password(password, purpose)
                print(message)
        
        elif choice == '2':
            # Check password strength
            password = input("Enter the password to check: ").strip()
            if not password:
                print("Error: Password cannot be empty.")
            else:
                strength, feedback = check_password_strength(password)
                print(f"\nPassword Strength: {strength}")
                print("Feedback:")
                for item in feedback:
                    print(f"- {item}")
        
        elif choice == '3':
            # Retrieve passwords
            purpose = input("Enter the purpose to search for (e.g., Email): ").strip()
            if not purpose:
                purpose = "General"
            
            success, result = retrieve_passwords(purpose)
            if success:
                print("\nMatching Passwords:")
                for line in result:
                    print(line)
            else:
                print(f"\nError: {result}")
        
        elif choice == '4':
            print("Thank you for using PassForge! 👋")
            sys.exit(0)
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()