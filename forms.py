# Form handling file

class TodoForm(Form):
    # Add todo form
    add_todo = Field('Add new todo', widget=TextInput())
    # Edit todo form
    edit_todo = Field('Edit todo', widget=TextInput())

    class Meta:
        model = Todo
        fields = ['title', 'description']