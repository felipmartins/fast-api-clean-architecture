import os


APP_CONFIG = {
    "SECRET_KEY": os.environ.get("SECRET_KEY", "secret-key"),
    "DB_NAME": os.environ.get("DB_NAME", "felpsdb"),
    "DB_URL": os.environ.get("DB_URL", "localhost"),
    "DB_PORT": os.environ.get("DB_PORT", "3306"),
    "DB_USER": os.environ.get("DB_USER", "root"),
    "DB_PASSWORD": os.environ.get("DB_PASSWORD", "password"),
}
