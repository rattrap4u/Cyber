# Steganography-Based Encryption Project

## Overview
This project implements image-based steganography to hide and retrieve secret messages inside an image. The approach ensures secure communication by embedding a message into an image without altering its visible appearance.

## Features
- Encrypts messages into an image using pixel manipulation.
- Decrypts the hidden message using a passcode.
- Uses Least Significant Bit (LSB) steganography for embedding data.
- Supports password protection for secure access.
- Works with common image formats such as JPG and PNG.

## How It Works
### 1. Encryption:
   - The user inputs a secret message and a passcode.
   - Each character is converted to its ASCII value and stored within pixel values.
   - The modified image is saved as `encryptedImage.jpg`.

### 2. Decryption:
   - The user enters the passcode to retrieve the hidden message.
   - The program extracts the ASCII values from the image and reconstructs the original message.
   - If the password is incorrect, access is denied.

## Installation & Usage
### Prerequisites
Ensure you have Python 3.x installed along with the required dependencies:
```sh
pip install opencv-python
```

### Steps to Run the Project
1. Clone this repository or download the script files.
2. Place the image (`mypic.jpg`) in the project folder.
3. Run the encryption script:
   ```sh
   python encrypt.py
   ```
4. Run the decryption script:
   ```sh
   python decrypt.py
   ```

## Project Structure
```
├── encrypt.py              # Script to hide the message inside an image
├── decrypt.py              # Script to extract the hidden message
├── password.txt            # Stores the password for decryption
├── tree.jpg                # Original image used for encoding
├── encryptedImage.jpg      # Image with hidden message
├── README.md               # Project documentation
```

## Future Enhancements
- **Advanced Encryption:** Use AES/RSA encryption before embedding.
- **Better Steganography:** Implement multi-channel LSB techniques.
- **Error Handling:** Improve detection of corrupted or altered images.
- **GUI Interface:** Develop a user-friendly application for ease of use.
- **Cloud Storage:** Implement secure cloud-based storage for encrypted images.

## License
This project is licensed under the MIT License. Feel free to modify and contribute!
