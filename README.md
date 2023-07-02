# School app

### Развертывание проекта с использованием Docker
Этот руководство описывает шаги для развертывания проекта с использованием Docker. Проект использует Docker Compose для управления контейнерами и настройки окружения. Вам потребуется установить Docker и Docker Compose перед началом.

### Предварительные требования
Перед началом установки убедитесь, что на вашем компьютере установлены следующие компоненты:
 - Docker: Установка Docker
 - Docker Compose: Установка Docker Compose

### Шаг 1: Клонирование репозитория
Сначала склонируйте репозиторий проекта на свою локальную машину:
```
git clone https://github.com/your-repository.git
cd your-repository
```
### Шаг 2: Создание файла .env
В корневой директории проекта создайте файл с именем .env. В этом файле вы можете задать конфигурационные переменные для вашего проекта, включая настройки базы данных. Вот пример содержимого файла .env:
```
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=pgdb
DB_PORT=5432
```
Замените значения your_database_name, your_database_user и your_database_password на свои собственные настройки базы данных.

### Шаг 3: Настройка Docker Compose
Откройте файл docker-compose.yml в корневой директории проекта. Убедитесь, что следующие параметры присутствуют в разделе services -> pgdb -> environment:
```
services:
  pgdb:
    environment:
      - POSTGRES_DB=${DATABASE_NAME}
      - POSTGRES_USER=${DATABASE_USER}
      - POSTGRES_PASSWORD=${DATABASE_PASSWORD}
```

### Шаг 4: Запуск проекта
Теперь вы готовы запустить проект с помощью Docker Compose. В командной строке, находясь в корневой директории проекта, выполните следующую команду:
```
docker-compose up --build
```
Docker Compose выполнит сборку и запуск контейнеров, включая контейнер с вашим приложением Django. Вы увидите вывод, который показывает, что контейнеры успешно запущены и работают.
### Шаг 5: Проверка работы приложения
Откройте веб-браузер и перейдите по адресу http://localhost:8000, чтобы увидеть работающее приложение. Вы должны увидеть домашнюю страницу вашего проекта.

### Примечеание
Не забудьте применить миграцию, выполнив команды, находясь в корне проекта:
```
docker-compose run django python manage.py makemigrations
docker-compose run django python manage.py migrate
```
Также создать суперпользователя, выполнив команду:
```
docker-compose run django python manage.py createsuperuser
```

### Заключение
Поздравляю! Вы успешно развернули проект с использованием Docker. Теперь вы можете работать с вашим приложением в изолированной среде и легко масштабировать его при необходимости. Если вам нужно изменить настройки базы данных или