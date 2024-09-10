from cryptography.fernet import Fernet

# Generate a key and save it to a file (only needed once)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# Load the previously generated key
def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("Key file not found. Please generate a key first.")
        return None

# Encrypt a message using the loaded key
def encrypt_message(message):
    key = load_key()
    if key is None:
        return None  # Exit if key is not found
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

# Decrypt a message using the loaded key
def decrypt_message(encrypted_message):
    key = load_key()
    if key is None:
        return None  # Exit if key is not found
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# To generate a key (only needed once), uncomment the line below:
# key = generate_key()

# Example usage
message = "Hello, World!"
print("Original message:", message)

# Encrypt the message
encrypted = encrypt_message(message)
if encrypted:
    print("Encrypted message:", encrypted)

    # Decrypt the message
    decrypted = decrypt_message(encrypted)
    if decrypted:
        print("Decrypted message:", decrypted)
