import random

def generate_workout(goal, level):
    workouts = {
        "strength": {"beginner": ["Push-ups", "Squats"], "intermediate": ["Bench Press", "Deadlifts"], "advanced": ["Snatch", "Muscle-ups"]},
        "cardio": {"beginner": ["Jump Rope", "Cycling"], "intermediate": ["Jogging", "Burpees"], "advanced": ["Running", "HIIT"]},
        "weight_loss": {"beginner": ["Plank", "Jump Rope"], "intermediate": ["Burpees", "Treadmill Sprints"], "advanced": ["HIIT", "Box Jumps"]}
    }
    return random.choice(workouts.get(goal, {}).get(level, ["Invalid input"]))

print(generate_workout(input("Goal: ").lower(), input("Level: ").lower()))
