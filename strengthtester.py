import re
import random
import string
import math

def calculate_entropy(password):
    # Calculate the entropy of the password
    characters = string.ascii_letters + string.digits + string.punctuation
    entropy = 0
    for char in set(password):
        if char in characters:
            entropy += math.log2(len(characters))
    return entropy

def analyze_password(password):
    # Check length
    length_score = min(10, len(password))  # Max score of 10 for length
    
    # Check character diversity (entropy)
    entropy = calculate_entropy(password)
    diversity_score = min(10, entropy)  # Max score of 10 for entropy
    
    # Check for common patterns or dictionary words
    pattern_score = 0
    common_patterns = ['123', 'password', 'qwerty', '123456']
    for pattern in common_patterns:
        if pattern in password.lower():
            pattern_score -= 5  # Deduct score for each common pattern found
    
    # Calculate total score
    total_score = length_score + diversity_score + pattern_score
    
    # Classify password strength
    if total_score < 10:
        strength = "Weak"
        feedback = "Your password is weak. It should be longer and avoid common patterns."
    elif total_score < 15:
        strength = "Moderate"
        feedback = "Your password is moderate. Consider adding more characters and avoiding common patterns."
    else:
        strength = "Strong"
        feedback = "Your password is strong. Good job!"
    
    return strength, total_score, feedback

def generate_password(length=12):
    # Generate a random password of specified length
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Strength Tester")
    print("-----------------------")
    
    while True:
        print("\nOptions:")3
        
        print("1. Analyze Password")
        print("2. Generate Strong Password")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            password = input("\nEnter your password: ")
            strength, score, feedback = analyze_password(password)
            print(f"\nPassword strength: {strength}")
            print(f"Score: {score}/20")
            print(f"Feedback: {feedback}")
        elif choice == '2':
            length = int(input("\nEnter the length of the password: "))
            if length <= 0:
                print("Length must be a positive integer.")
                continue
            password = generate_password(length)
            print(f"\nGenerated password: {password}")
            strength, score, feedback = analyze_password(password)
            print(f"Password strength: {strength}")
            print(f"Score: {score}/20")
            print(f"Feedback: {feedback}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
