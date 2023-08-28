# Configuration file for the todo app

# Database connection details
DB_HOST = 'localhost'
DB_PORT = 5432
DB_NAME = 'todo_app'
DB_USER = 'root'
DB_PASSWORD = ''

# Default database connection
DATABASE = {
    'host': DB_HOST,
    'port': DB_PORT,
    'database': DB_NAME,
    'user': DB_USER,
    'password': DB_PASSWORD
}

# Route definitions
ROUTES = [
    {'path': '/', 'handler': 'app.routes.index'},
    {'path': '/new', 'handler': 'app.routes.new_todo'},
    {'path': '/edit/:id', 'handler': 'app.routes.edit_todo'},
    {'path': '/show/:id', 'handler': 'app.routes.show_todo'}
]