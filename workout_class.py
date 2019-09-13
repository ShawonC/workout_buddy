import sqlite3
import datetime
import random

class WorkoutBuddy():
    def __init__(
        self,
        muscles,
        data='data/exercises'
    ):
        self.muscles = muscles
        self.database = sqlite3.connect(data)
        self.cursor = self.database.cursor()

    def get_exercises(self):
        base_query = "SELECT exercise FROM exercises WHERE muscle IN (?)"
        sql_query = self.cursor.execute(base_query,(self.muscles,))
        exercises = [row[0] for row in sql_query]
        return exercises

    def update_history(self, exercise):
        self.cursor.execute('''INSERT INTO history(date, exercise, muscle)
                               VALUES(?,?,?)''', (datetime.date.today(), exercise,))
        self.database.commit()

    def check_table(self, exercise):
        base_query = "SELECT exercise FROM exercises WHERE exercise=?"
        sql_query = self.cursor.execute(base_query,(exercise,))
        exercise = [row[0] for row in sql_query]
        if exercise:
            return True
        else:
            return False

    def get_random_exercise(self):
        exercise_list = self.get_exercises()
        daily_exercise = random.choice(exercise_list)
        return daily_exercise

    def choose_exercise(self):
        count = 0
        random_exercise = self.get_random_exercise()
        used = self.check_table(random_exercise)
        while count < 30:
            if used:
                random_exercise = self.get_random_exercise()
                used = self.check_table(random_exercise)
                count = count + 1
            else:
                self.update_history(random_exercise)
                return random_exercise
        else:
            self.update_history(random_exercise)
            return random_exercise
