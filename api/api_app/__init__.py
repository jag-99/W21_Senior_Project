# https://fastapi.tiangolo.com/tutorial/sql-databases/

CONFIG = {
    "db_user": "estate",
    "db_pw": "password",
    "db_host": "127.0.0.1",
    "db_port": " 3306",
    "db_name": "real_estate"
}


DB_URI = f'mysql+mysqlconnector://{CONFIG.get("db_user")}:{CONFIG.get("db_pw")}@ \
    {CONFIG.get("db_host")}:{CONFIG.get("db_port")}/{CONFIG.get("db_name")}'

# ?check_same_thread=False