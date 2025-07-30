from instagrapi import Client
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

def like_and_comment(target_username, comment_func, messages):
    cl = Client()
    cl.login(USERNAME, PASSWORD)

    user_id = cl.user_id_from_username(target_username)
    medias = cl.user_medias(user_id, 1)
    latest = medias[0]

    comment = comment_func(latest.caption_text, messages)

    cl.media_like(latest.id)
    cl.media_comment(latest.id, comment)