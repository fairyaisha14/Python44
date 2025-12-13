import random

def generate_password(length=12):
    # Define the character sets manually
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    
    # Combine all character sets
    char_set = lowercase + uppercase + digits
    
    # Generate a random password
    password = ''.join(random.choice(char_set) for _ in range(length))
    
    # Shuffle the generated password
    password = ''.join(random.sample(password, len(password)))
    
    return password

# Example usage
password = generate_password(12)
print("Generated Password:", password)
