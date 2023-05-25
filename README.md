# Todo-list
### A page for keeping a list of tasks, adding relevant tags with an existing binding to the date.
## Running the program locally

1. Clone the source code:

```bash
git clone https://github.com/Thirteenthskyi/todo_list.git
cd todo_list
```

2. Install modules and dependencies:

```bash
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```

3. `.env_sample` 
This is a sample .env file for use in local development.
Duplicate this file as .env in the root of the project
and update the environment variables to match your
desired config. You can use [djecrety.ir](https://djecrety.ir/)

4. Use the command to configure the database and tables:

```bash
python manage.py migrate
```

5. Start the app:

```bash
python manage.py runserver
```
6. Use the following command to load prepared data from fixture:

```bash
python manage.py loaddata todo_list_db_data.json
```

- You can use following superuser (or create another one by yourself using the admin page):
    - Login: `admin.user`
    - Password: `Us2ddTX7`
