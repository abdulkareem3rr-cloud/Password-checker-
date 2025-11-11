import re
import random
import string
import math

def check_password_strength(password):
    """
    Checks the strength of a password and provides feedback on missing elements.
    """
    feedback = []
    
    # Check length
    if len(password) < 8:
        feedback.append("Make the password at least 8 characters long.")
    
    # Check for uppercase
    if not re.search(r'[A-Z]', password):
        feedback.append("Add at least one uppercase letter (A-Z).")
    
    # Check for lowercase
    if not re.search(r'[a-z]', password):
        feedback.append("Add at least one lowercase letter (a-z).")
    
    # Check for digit
    if not re.search(r'\d', password):
        feedback.append("Add at least one number (0-9).")
    
    # Check for special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Add at least one special character (e.g., !@#$%^&*).")
    
    # Additional suggestion for leetspeak
    feedback.append("Consider using leetspeak (e.g., replace 'a' with '4', 'e' with '3', 'o' with '0') to make your password more complex and harder to guess.")
    
    # Determine overall strength
    met_criteria = sum([
        len(password) >= 8,
        bool(re.search(r'[A-Z]', password)),
        bool(re.search(r'[a-z]', password)),
        bool(re.search(r'\d', password)),
        bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    ])
    
    if met_criteria <= 2:
        strength = "Weak"
    elif met_criteria == 3:
        strength = "Medium"
    else:
        strength = "Strong"
    
    return strength, feedback

def estimate_crack_time(password):
    """
    Estimates the time to crack the password via brute force.
    Assumptions: 10 billion guesses per second (rough estimate for modern hardware).
    """
    length = len(password)
    if length == 0:
        return "Instantly (empty password)"
    
    # Determine character set size based on password content
    charset_size = 0
    if re.search(r'[a-z]', password):
        charset_size += 26  # lowercase
    if re.search(r'[A-Z]', password):
        charset_size += 26  # uppercase
    if re.search(r'\d', password):
        charset_size += 10  # digits
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset_size += len("!@#$%^&*(),.?\":{}|<>")  # special chars
    
    # If no variety, assume basic set (e.g., all lowercase)
    if charset_size == 0:
        charset_size = 26
    
    # Total combinations
    combinations = charset_size ** length
    
    # Cracking speed (guesses per second) - rough estimate
    guesses_per_second = 10**10  # 10 billion
    
    # Time in seconds
    time_seconds = combinations / guesses_per_second
    
    # Convert to readable format
    if time_seconds < 1:
        return "Less than 1 second"
    elif time_seconds < 60:
        return f"{time_seconds:.2f} seconds"
    elif time_seconds < 3600:
        return f"{time_seconds / 60:.2f} minutes"
    elif time_seconds < 86400:
        return f"{time_seconds / 3600:.2f} hours"
    elif time_seconds < 31536000:
        return f"{time_seconds / 86400:.2f} days"
    else:
        years = time_seconds / 31536000
        return f"{years:.2f} years"

def generate_suggested_password(length=12):
    """
    Generates a random, complex password suggestion.
    """
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    specials = "!@#$%^&*(),.?\":{}|<>"
    
    # Ensure at least one of each type
    password_chars = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(specials)
    ]
    
    # Fill the rest randomly
    all_chars = lower + upper + digits + specials
    password_chars += random.choices(all_chars, k=length - 4)
    
    # Shuffle to randomize order
    random.shuffle(password_chars)
    
    return ''.join(password_chars)

# Main program
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength, feedback = check_password_strength(password)
    crack_time = estimate_crack_time(password)
    
    print(f"Password strength: {strength}")
    print(f"Estimated time to crack via brute force: {crack_time}")
    print("(Note: This is a rough estimate assuming modern hardware and brute-force attack. Actual time varies.)")
    
    if feedback:
        print("\nSuggestions to improve:")
        for suggestion in feedback:
            print(f"- {suggestion}")
        # Generate and suggest a more complex password
        suggested = generate_suggested_password()
        print(f"\nHere's a suggested stronger password: {suggested}")
        print("Note: This is randomly generated. Use it as inspiration or modify it.")
    else:
        print("Your password is strong! No improvements needed.")
