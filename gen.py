import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''
    
    all_chars = letters + digits + symbols
    
    if not all_chars:
        raise ValueError("Character set is empty. Enable digits or symbols.")
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    
    try:
        length = int(input("Password length (default 12): ") or 12)
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12

    use_digits = input("Include digits? (y/n, default y): ").lower() != 'n'
    use_symbols = input("Include symbols? (y/n, default y): ").lower() != 'n'

    password = generate_password(length, use_digits, use_symbols)
    print("\nGenerated Password:\n", password)

if __name__ == "__main__":
    main()
