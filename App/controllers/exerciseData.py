from App.database import db
import App.models.exerciseData as E
import json

def add_exerciseData(exercise):
    db_exercise = E.ExerciseData(name=exercise['name'], bodyPart=exercise['bodyPart'], equipment=exercise['equipment'], target=exercise['target'], gifUrl=exercise['gifUrl'])
    db.session.add(db_exercise)
    db.session.commit()
    return db_exercise

def add_allExerciseData():
    with open("App/exercises.json") as file:
        data = json.load(file)

    for item in data:
        # exercise()
        bob = add_exerciseData(item)
        # print(item)

# returns exerciseData based on its id
def get_exerciseData(id):
    exercise = E.ExerciseData.query.filter_by(id = id).first()
    if exercise:
        return exercise
    return None

def get_exerciseData_json(id):
    exercise = get_exerciseData(id)
    if exercise:
        return exercise.get_json()
    return None

    

def get_all_exercises():
    return E.ExerciseData.query.all()

def get_all_exercises_json():
    exercises = get_all_exercises()
    if not exercises:
        return []
    exerciseList = [ exercise.get_json() for exercise in exercises]
    return exerciseList