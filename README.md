# Encryptionbot
Welcome to EncryptionBot, a simple Telegram bot written in Python that can crack encrypted files or hashed text using brute force. EncryptionBot utilizes multithreading to improve performance and store his data in MongoDB. Additionally, it provides a user-friendly Telegram interface with keyboard buttons for easy interaction.

Running the Bot:
To run EncryptionBot, execute the following command:
python main.py

Telegram Interface:
EncryptionBot provides a Telegram interface for easy interaction. You can start a conversation with the bot by searching for it on Telegram and clicking "Start." The bot will guide you through the password cracking process using keyboard buttons.

EncryptionBot supports the following commands:
"1"-(this command still in developing) Cracking Encryption File: Use this command to initiate the cracking process for an encrypted file. Follow the bot's prompts to provide the necessary file.
"2"-Cracking Hashed MD5 Passwords: This command is for cracking MD5 hashed passwords. Enter the hashed password when prompted by the bot.
Please note that after executing these commands, you will need to provide the relevant file or password for the bot to perform its work.

Note: EncryptionBot assumes that the encrypted files or hashed text are relatively easy to crack, MD5 encryption and 8-character passwords of letters and numbers only. Additionally, it supports common file types like PDF, ZIP, and TXT encrypted using simple methods. More complex encryption methods and file types may require additional customization.

Enjoy using EncryptionBot, and happy password cracking!
