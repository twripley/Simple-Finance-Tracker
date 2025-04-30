DB_HOST = "sql.domain.com"
DB_NAME = "SFT"
DB_USER = "username"
DB_PASS = "password"

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://" + DB_USER + ":" + DB_PASS + "@" + DB_HOST + "/" + DB_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False
