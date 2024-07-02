import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
feedbacks = os.getenv("FEEDBACKS_LINK")
feedbacks_group = os.getenv("FEEDBACKS")
admin = os.getenv("ADMIN")
