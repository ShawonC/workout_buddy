import sqlite3

class WorkoutBuddy():
    def __init__(
        self,
        muscle,
        data='data/exercises'
    ):
        self.muscle = muscle
        self.database = sqlite3.connect(data)
        self.cursor = self.database.cursor()

    def get_exercises(self):
        base_query = "SELECT exercise FROM exercises WHERE muscle=?"
        sql_query = self.cursor.execute(base_query,(self.muscle,))
        exercises = [row[0] for row in sql_query]
        return exercises

    # def update_db(self):
        # sql_query = ""