import os
from dotenv import load_dotenv

load_dotenv()
SENTRY_DSN = os.getenv("SENTRY_DSN")

SLACK_WEBHOOK = "https://hooks.slack.com/services/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"

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")
AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET")

MONGO_URI = os.getenv("MONGO_URI")
# Database name.
MONGO_DB = os.getenv("MONGO_DB")

MONGO_URI_LOCAL = os.getenv("MONGO_URI_LOCAL")
MONGO_DB_LOCAL = os.getenv("MONGO_DB_LOCAL")


#Key API Lineru
LINERU_SERVICE_KEY = os.getenv("LINERU_SERVICE_KEY")
LINERU_SERVICE_URL = os.getenv("LINERU_SERVICE_URL")

#FGA API
FGA_API_KEY_URL = os.getenv("FGA_API_KEY_URL")
USERNAME_API_KEY_FGA = os.getenv("USERNAME_API_KEY_FGA")
PASSWORD_API_KEY_FGA = os.getenv("PASSWORD_API_KEY_FGA")
FGA_UPDATE_BALANCE_URL = os.getenv("FGA_UPDATE_BALANCE_URL")

# NIT
NIT = os.getenv("NIT")
