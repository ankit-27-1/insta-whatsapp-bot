import re

def extract_user_messages(file_path, user_name):
    messages = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        if re.match(r'\d{1,2}/\d{1,2}/\d{2,4},', line):
            if f"{user_name}:" in line:
                msg = line.split(":", 2)[2].strip()
                if msg:
                    messages.append(msg)
    return messages