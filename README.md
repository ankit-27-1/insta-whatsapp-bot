🤖 InstaMomBot

A Python bot that automatically likes and comments on your mom’s Instagram posts — using AI trained on your WhatsApp messages to make it sound like you.

⸻

📸 Why?

Your mom just joined Instagram and keeps complaining that you don’t like her posts. You don’t even use Instagram. Instead of reinstalling the app and faking excitement, let this bot handle the love. ❤️

⸻

🚀 Features
	•	✅ Parses your WhatsApp chat export (.txt) with your mom
	•	✅ Trains AI (OpenAI GPT) to talk like you
	•	✅ Logs into Instagram
	•	✅ Automatically finds your mom’s latest post
	•	✅ Likes and posts a comment that sounds like you

⸻

🛠️ Setup Instructions
1. Clone the Repo
   git clone https://github.com/yourusername/InstaMomBot.git
   cd InstaMomBot

2. Install Requirements
   pip install -r requirements.txt

3. Add Your Data

📁 data/whatsapp_chat.txt
	•	Export WhatsApp chat with your mom as .txt and save it to data/whatsapp_chat.txt.
	•	Only your messages are used for training.

⸻

4. Create .env File

In the project root, create a .env file and add:

OPENAI_API_KEY=your-openai-key
INSTA_USERNAME=your-instagram-username
INSTA_PASSWORD=your-instagram-password

🔒 Do NOT put any of these in quotes or semicolons.

⸻

5. Run the Bot
   python main.py

The bot will:
	•	Parse your WhatsApp messages
	•	Log in to Instagram
	•	Grab the latest post from your mom’s profile
	•	Like the post
	•	Post a comment that sounds like you

⸻

📁 Project Structure

instaBot/
│
├── bot/
│   ├── whatsapp_parser.py        # Extracts your messages from WhatsApp chat
│   ├── comment_generator.py      # Uses OpenAI to generate realistic comment
│   ├── instagram_bot.py          # Logs in, fetches latest post, likes & comments
│
├── data/
│   └── whatsapp_chat.txt         # Exported chat with your mom (only your messages used)
│
├── main.py                       # Orchestrates the bot
├── .env                          # API key and login credentials
├── requirements.txt              # Python dependencies
└── README.md                     # This file


🔧 Notes
	•	Only works for public Instagram accounts or accounts you follow.
	•	Comments are generated using OpenAI GPT, trained only on your tone.
	•	You can replace instagrapi with Selenium if the API breaks due to Instagram changes.

⸻

🧠 Example Output

WhatsApp style:

“Aree mummy aap toh star lag rahi ho!”

Instagram Comment:

“Maa queen mode ON 🔥 looking awesome as always 😍”

⸻

❗ Troubleshooting


Problem
Fix
RateLimitError
Your OpenAI free quota expired. Add billing or use a new API key.
extract_user_gql() error
instagrapi is broken. Switch to Selenium or wait for patch.
KeyError: 'data'
Instagram changed their API. Patch required or fallback to manual.


🤷‍♂️ Credits

Idea by someone too lazy to use Instagram — but who loves his mom enough to automate affection. ❤️
