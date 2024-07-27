# Telegram Referral Bot

A Telegram bot that integrates with a MySQL database to handle user registrations and track referral counts. The bot provides users with a custom keyboard and allows them to manage their referrals and registrations.

## Features

- **User Registration:** Users can register with the bot and have their information stored in a MySQL database.
- **Referral Tracking:** Users can invite others to join, and the bot tracks the number of referrals for each user.
- **Custom Keyboard:** A user-friendly custom keyboard is provided for interaction.

## Requirements

- **Python 3.x:** Ensure Python 3 is installed on your system.
- **Libraries:** The following Python libraries are required:
  - `pyTelegramBotAPI` (for interacting with the Telegram API)
  - `mysql-connector-python` (for connecting to the MySQL database)

## Setup

1. **Install Prerequisites:**
   ```bash
   pip install pyTelegramBotAPI
   pip install mysql-connector-python
   ```
---
2. **Configuration:**
   - Put your robot token in this section
     ```pythone
     bot = telebot.TeleBot("TOKEN")
     ```
---
3. **Run:**
   ```bash
   python3 onlyf.py
   ```
---
4. **Configure the Database:**
   ```bash
   cnx = mysql.connector.connect(user='your_user', password='your_password', host='127.0.0.1', database='your_database')
   ```
---
## Contact

For any questions or feedback, feel free to contact me at aliwwwmo@gmail.com or Telegram : https://t.me/aliwwwmo


