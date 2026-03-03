import os
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    # --------------------------------------------------
    # Core Security
    # --------------------------------------------------
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # --------------------------------------------------
    # Azure Blob Storage
    # --------------------------------------------------
    BLOB_ACCOUNT = os.environ.get("BLOB_ACCOUNT")
    BLOB_STORAGE_KEY = os.environ.get("BLOB_STORAGE_KEY")
    BLOB_CONTAINER = os.environ.get("BLOB_CONTAINER")

    # --------------------------------------------------
    # Azure SQL Database
    # --------------------------------------------------
    SQL_SERVER = os.environ.get("SQL_SERVER")
    SQL_DATABASE = os.environ.get("SQL_DATABASE")
    SQL_USER_NAME = os.environ.get("SQL_USER_NAME")
    SQL_PASSWORD = os.environ.get("SQL_PASSWORD")

    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}"
        f"@{SQL_SERVER}:1433/{SQL_DATABASE}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --------------------------------------------------
    # Microsoft Authentication (MSAL)
    # --------------------------------------------------
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    AUTHORITY = os.environ.get("AUTHORITY")

    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"