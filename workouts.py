from pick import pick
import random
from workout_class import WorkoutBuddy

legs = ['hamstrings', 'glutes', 'abductors', 'calves', 'adductors', 'quadriceps']
chest = ['chest']
shoulders = ['shoulders', 'traps', 'neck']
arms = ['forearms', 'biceps', 'triceps']
back = ['middle back', 'lats', 'lower back']
abdominals = ['abdominals']

def make_exercise_list(muscle_group: list):
    group_length = len(muscle_group)
    if group_length > 3:
        exercises = []
        data = random.sample(muscle_group, k=3)
        for entry in data:
            wb = WorkoutBuddy(muscle=entry)
            exercises.append(wb.choose_exercise())
    elif group_length == 1:
        count = 0
        exercises = []
        wb = WorkoutBuddy(muscle=muscle_group[0])
        while count < 3:
            exercises.append(wb.choose_exercise())
            count += 1
    else:
        exercises = []
        for entry in muscle_group:
            wb = WorkoutBuddy(muscle=entry)
            exercises.append(wb.choose_exercise())
    return exercises

title = "Please choose which muscle group you'd like to workout"
muscles = {
    'Legs': legs,
    'Chest': chest,
    'Shoulders': shoulders,
    'Arms': arms,
    'Back': back,
    'Abdominals': abdominals
}
options = [
    'Legs',
    'Chest',
    'Shoulders',
    'Arms',
    'Back',
    'Abdominals'
]

muscle_pick, index = pick(options, title)
muscle_choice = muscles[muscle_pick]
exercises = make_exercise_list(muscle_choice)

print("Your exercises today are:")
for entry in exercises:
    print(entry)


