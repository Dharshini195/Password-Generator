import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    try:
        length = int(input("Enter the desired length for your password: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        
        password = generate_password(length)
        print("\nGenerated Password: ", password)
    
    except ValueError as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    main()
