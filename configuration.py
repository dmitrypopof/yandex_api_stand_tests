# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или другим ресурсам.
# Значение должно быть скопировано из настроек или документации сервиса, к которому предоставляется доступ.
# Пример значения: "https://api.example.com"
URL_SERVICE = "https://b8d3595f-5df8-4339-8f09-d5cd04db146b.serverhub.praktikum-services.ru"

# DOC_PATH содержит путь к документации веб-сервиса.
# Этот путь используется для формирования полного URL пути к документации, добавляя его к базовому URL сервиса.
# В результате получится что-то вроде "https://api.example.com/docs/"
DOC_PATH = "/docs/"

LOG_MAIN_PATH = "/api/logs/main/" #  Путь до логов
USERS_TABLE_PATH = "/api/db/resources/user_model.csv" # Путь до таблицы
CREATE_USER_PATH = "/api/v1/users/" # Хранит путь к API-методу для создания нового пользователя
PRODUCTS_KITS_PATH = "/api/v1/products/kits/" #  Путь к API-методу для поиска наборов по продуктам

