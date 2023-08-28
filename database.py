import sqlite3

class TodoDatabase:
    def __init__(self):
        self.db = sqlite3.connect('todo_app.db')
        self.cursor = self.db.cursor()
    
    def add_todo(self, text):
        self.cursor.execute('INSERT INTO todos (text) VALUES (?)', (text,))
        self.db.commit()
    
    def get_todos(self):
        self.cursor.execute('SELECT * FROM todos')
        return self.cursor.fetchall()
    
    def delete_todo(self, text):
        self.cursor.execute('DELETE FROM todos WHERE text = ?', (text,))
        self.db.commit()