from bot.whatsapp_parser import extract_user_messages
from bot.comment_generator import generate_comment
from bot.instagram_bot import like_and_comment

if __name__ == "__main__":
    messages = extract_user_messages("data/whatsapp.txt", "Barbie")  # Replace Barbie with your WhatsApp name
    like_and_comment("friend_username", generate_comment, messages)