import random
from workout_class import WorkoutBuddy

legs = ['hamstrings', 'glutes', 'abductors', 'calves', 'adductors', 'glutes', 'quadriceps']
chest = ['chest']
shoulders = ['shoulders', 'traps', 'neck']
arms = ['forearms', 'biceps', 'triceps']
back = ['middle back', 'lats', 'lower back']
abdominals = ['abdominals']

for muscle in back:
    wb = WorkoutBuddy(muscle=muscle)
    exercise = wb.choose_exercise()
    print(exercise)
