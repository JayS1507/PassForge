# PassForge 🔒

PassForge is a powerful Python tool designed to generate strong passwords, evaluate password strength, tag passwords with their purpose, and retrieve saved passwords. Perfect for educational projects in cybersecurity, PassForge helps users manage passwords with ease and precision. 🚀

## Features ✨
- 🔐 Generates strong passwords with user-specified length (minimum 8 characters).
- 🛡️ Includes uppercase, lowercase, digits, and special characters for maximum strength.
- 📊 Evaluates password strength with detailed feedback (Weak, Moderate, Strong).
- 🏷️ Tags generated passwords with a purpose (e.g., "Email") for organization.
- 🔎 Retrieves saved passwords by searching for their purpose.
- 💾 Saves passwords to a file with timestamps and purposes for record-keeping.
- 🖥️ Intuitive command-line menu for seamless interaction.
- ✅ Validates inputs to prevent errors and ensure reliability.

## Prerequisites 📋
- **Python 3.x**: Install Python from [python.org](https://www.python.org/downloads/) if not already installed. 🐍
- No external libraries required; uses standard Python modules (`random`, `string`, `re`, `os`, `datetime`, `sys`).

## Installation 🛠️
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/PassForge.git
   ```
2. Navigate to the project directory:
   ```bash
   cd PassForge
   ```

## Usage 🎮
1. Run the script with Python:
   ```bash
   python passforge.py
   ```
2. Choose an option from the menu:
   - **1. Generate a strong password**: Enter the desired length (≥8) and purpose (e.g., "Email"). The password is saved to `passwords.txt`.
   - **2. Check password strength**: Enter a password to get its strength rating and feedback.
   - **3. Retrieve saved passwords**: Enter a purpose to view all matching passwords.
   - **4. Exit**: Close the program.
3. Follow the prompts to interact with the tool.

### Example 📝
```bash
=== PassForge 🔒 ===
1. Generate a strong password
2. Check password strength
3. Retrieve saved passwords
4. Exit
Enter your choice (1-4): 1
Enter password length (minimum 8): 12
Enter the purpose of this password (e.g., Email): Email

Generated Password: K7@mP#nL9$xQ
Purpose: Email
Password saved to passwords.txt

=== PassForge 🔒 ===
1. Generate a strong password
2. Check password strength
3. Retrieve saved passwords
4. Exit
Enter your choice (1-4): 3
Enter the purpose to search for (e.g., Email): Email

Matching Passwords:
2025-05-04 12:30:45 | Email | K7@mP#nL9$xQ

=== PassForge 🔒 ===
1. Generate a strong password
2. Check password strength
3. Retrieve saved passwords
4. Exit
Enter your choice (1-4): 2
Enter the password to check: password123

Password Strength: Weak
Feedback:
- Too short (minimum 8 characters).
- Missing uppercase letters.
- Missing special characters.
```

## Saved Passwords 💾
- Generated passwords are stored in `passwords.txt` in the project directory.
- Format: `Timestamp | Purpose | Password` (e.g., `2025-05-04 12:30:45 | Email | K7@mP#nL9$xQ`).
- The file is appended, not overwritten, to maintain a history.
- Use the "Retrieve saved passwords" option to view passwords by purpose.

## Notes ⚠️
- **Security**: Do not share `passwords.txt` publicly, as it contains sensitive data. The `.gitignore` file prevents it from being uploaded to GitHub. 🛑
- **Password Strength**: The checker evaluates length, uppercase, lowercase, digits, and special characters. A score of 5/5 indicates a strong password.
- **Purpose Tagging**: If no purpose is provided, it defaults to "General". Searches are case-insensitive.
- **Ethical Use**: Use PassForge responsibly for educational purposes or personal security. 🚨
- **File Storage**: Ensure write permissions in the project directory for saving passwords.

## Contributing 🤝
Contributions are welcome to enhance PassForge! To contribute:
1. Fork the repository. 🍴
2. Create a feature branch (`git checkout -b feature-branch`). 🌿
3. Commit your changes (`git commit -m "Add feature"`). 💾
4. Push to the branch (`git push origin feature-branch`). 📤
5. Submit a pull request. 📬

## License 📜
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer 🚫
PassForge is intended for educational use only. The author is not liable for any misuse or damages resulting from this tool. Securely manage saved passwords to prevent unauthorized access.