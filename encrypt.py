import cv2
import os

# Load the image
img = cv2.imread("tree.png")  # Replace with the correct image path

# Get user input
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Ensure only valid ASCII characters (0-127) are stored
d = {chr(i): i for i in range(128)}

# Append a null terminator at the end of the message
msg += "\0"

# Encrypt the message into the image
n, m, z = 0, 0, 0
for char in msg:
    if char in d:
        img[n, m, z] = d[char]
    else:
        print(f"Warning: Character '{char}' cannot be encoded.")
    n += 1
    m += 1
    z = (z + 1) % 3

# Save the encrypted image in PNG format (prevents compression issues)
cv2.imwrite("encryptedImage.png", img)  
os.system("start encryptedImage.png")  # Open the image on Windows

# Save the password
with open("password.txt", "w") as f:
    f.write(password)

print("Encryption completed. Encrypted image saved as 'encryptedImage.png'.")
