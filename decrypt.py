import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")

# Load the stored password
try:
    with open("password.txt", "r") as f:
        stored_password = f.read().strip()
except FileNotFoundError:
    print("Error: Password file not found!")
    exit()

# Get password from the user
pas = input("Enter passcode for decryption: ")

# Check if the password is correct
if stored_password == pas:
    c = {i: chr(i) for i in range(128)}  # Ensure only ASCII decoding

    # Decrypt the message
    message = ""
    n, m, z = 0, 0, 0
    try:
        while True:
            char_value = img[n, m, z]
            if char_value in c:
                char = c[char_value]
                if char == "\0":  # Stop when the null terminator is found
                    break
                message += char
            n += 1
            m += 1
            z = (z + 1) % 3
    except IndexError:
        print("Warning: Reached the end of image while decrypting!")

    print("Decryption successful. Message:", message)
else:
    print("Access Denied: Incorrect password!")
