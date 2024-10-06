import nicegui

class TodoApp:
    def __init__(self):
        self.tasks = []
    
    @nicegui.http('/', layout='vertical')
    async def todo_list(self):
        return {
            "title": "Todo List",
            "columns": ["Task", "Status"],
            "rows": [
                {"text": task["description"], "status": task.get("done", False)}
                for task in self.tasks
            ],
            "actions": [
                {"label": "+ Add Task", "callback": self.add_task}
            ]
        }
    
    @nicegui.http('/add_task', layout='horizontal')
    async def add_task(self):
        form = {
            "description": "",
            "done": False,
        }
        return {
            "title": "Add Task",
            "fields": [
                {"label": "Description", "name": "description", "type": "text"},
                {"label": "Done?", "name": "done", "type": "checkbox"}
            ],
            "button": {"label": "Save", "callback": self.save_task}
        }
    
    async def save_task(self, fields):
        task = {
            "description": fields["description"],
            "done": fields.get("done")
        }
        self.tasks.append(task)
        nicegui.update('/')
        return {"message": "Task saved!"}
    
    @nicegui.http('/edit_task/{task_id}', layout='horizontal')
    async def edit_task(self, task_id):
        task = self.tasks[int(task_id)]
        form = {
            "description": task["description"],
            "done": task.get("done", False)
        }
        return {
            "title": f"Edit Task {task_id}",
            "fields": [
                {"label": "Description", "name": "description", "type": "text"},
                {"label": "Done?", "name": "done", "type": "checkbox"}
            ],
            "button": {"label": "Save", "callback": self.save_edited_task, data={"task_id": task_id}}
        }
    
    async def save_edited_task(self, fields, data):
        task = {
            "description": fields["description"],
            "done": fields.get("done")
        }
        old_task = self.tasks[int(data["task_id"])]
        self.tasks[int(data["task_id"])] = task
        nicegui.update('/')
        return {"message": "Task saved!"}
    
    @nicegui.http('/remove_task/{task_id}', layout='horizontal')
    async def remove_task(self, task_id):
        del self.tasks[int(task_id)]
        nicegui.update('/')
        return {"message": "Task removed!"}

if __name__ == '__main__':
    TodoApp().run()
