import hashlib

def check_password_strength(password):
    strength = 0
    
    # Check length
    if len(password) >= 8:
        strength += 1
    
    # Check for uppercase and lowercase letters
    if any(char.isupper() for char in password) and any(char.islower() for char in password):
        strength += 1
    
    # Check for digits
    if any(char.isdigit() for char in password):
        strength += 1
    
    # Check for special characters
    special_chars = "!@#$%^&*()-_+=[]{}|;:,.<>?/"
    if any(char in special_chars for char in password):
        strength += 1
    
    return strength

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    
    # Log password strength on a 1-5 scale
    print("Password strength (1-5 scale):", strength)
    
    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    print("Hashed password:", hashed_password)

if _name_ == "_main_":
    main()