# api_final
Описание: Этот проект позволяет пользователям получать доступ через API к постам, группам,
подписчикам, комментариям и прочему. Создавать, удалять объекты, редактировать их по собственному усмотрению.

Установка: Как завпустить проект: Клонировать репрозиторий и перейти в него в командной  строке.

git clone https://github.com/ChaoChaoRU/api_final_yatube.git

Создать и активировать виртуальное:

python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver


Примеры запросов:

GET api/v1/posts/

Возращает список всех постов


POST api/v1/posts

 Создает пост 
Final API