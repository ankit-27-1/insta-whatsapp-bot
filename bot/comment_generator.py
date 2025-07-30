from openai import OpenAI
import os
from dotenv import load_dotenv
import random

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_comment(caption, message_samples):
    sample_msgs = random.sample(message_samples, min(5, len(message_samples)))

    prompt = f"""
    Based on the way I talk to my _____(examples below), write a sweet Instagram comment for this post caption: "{caption}"

    Examples:
    {" | ".join(sample_msgs)}

    Instagram Comment:
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=60
    )

    return response.choices[0].message.content.strip()