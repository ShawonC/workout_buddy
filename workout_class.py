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
        sql_query = "SELECT exercise FROM exercises WHERE muscle=?"
        self.cursor.execute(sql_query,(self.muscle,))
        exercises = [row[0] for row in self.cursor]
        return exercises

    # def update_db(self):
        # sql_query = ""