from workout_class import WorkoutBuddy

legs = ['hamstrings', 'glutes', 'abductors', 'calves', 'adductors', 'glutes', 'quadriceps']
chest = ['chest']
shoulders = ['shoulders', 'traps', 'neck']
arms = ['forearms', 'biceps', 'triceps']
back = ['middle back', 'lats', 'lower back']
abdominals = ['abdominals']

wb = WorkoutBuddy(muscle='chest')

exercises = wb.get_exercises()
# print(exercises)