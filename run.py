from random import choice
from time import sleep
from TTS import *
import os
import argparse


def do_exercise(exercise):
    """
    Guides the user through a given exercise.
    :param exercise: the exercise to perform.
    :return:
    """
    read("Next up, 30 seconds of {}.".format(exercise))
    read_begin()
    sleep(15)
    if exercise in {"side plank", "clean and press"}:
        read("Switch sides")
    else:
        read(choice(["Halfway done", "keep it up", "15 seconds left", "finish_strong"]))
        read_motivation()
    sleep(15)
    read(choice(["exercise complete","exercise finished"]))

def print_exercise(exercise_index, exercises):
    """
    Prints out the list of exercises in the workout
    with an arrow pointing to the current exercise.
    :param exercise_index: the index of the current exercise in the workout
    :param exercises: the list of exercises in the workout
    :return:
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    for e in range(0, len(exercises)):
        if e == exercise_index:
            print("Exercise {}: {} <---*".format(e+1, exercises[e]))
        else:
            print("Exercise {}: {}".format(e+1, exercises[e]))

def workout(exercises):
    """
    Guides the user through a workout given the list of exercises.
    :param exercises: the list of exercises in the workout
    :return:
    """
    for exercise_index in range(0, len(exercises)):
        print_exercise(exercise_index, exercises)
        do_exercise(exercises[exercise_index])

def back():
    """
    :return: a random back exercise from a list of back exercises
    """
    return choice(["two hand swings", "one hand swings", "bent over row", "deadlift", "pullups", "bridge"])

def chest():
    """
    :return: a random chest exercise from a list of chest exercises
    """
    # half moon push up
    return choice(["push ups", "kettlebell press alternating", "kettlebell press together",\
               "single kettlebell squeeze press", "decline pushup", "incline pushup", "decline kettlebell press"])

def shoulders():
    """
    :return: a random shoulder exercise from a list of shoulder exercises
    """
    return choice(["shoulder press", "clean and press", "L raise", "crab walk", "pike push up"])

def core():
    """
    :return: a random core exercise from a list of core exercises
    """
    return choice(["plank", "side plank", "ab wheel", "mountain climbers", "circle rock"])

def legs():
    """
    :return: a random leg exercise from a list of leg exercises
    """
    # hindu squat, archer squat
    return choice(["squat", "clean", "one leg squat", "lunge", "calf raise"])

def biceps():
    """
    :return: a random bicep exercise from a list of bicep exercises
    """
    return choice(["bicep curl", "bowl curl", "chin up"])
 
def triceps():
    """
    :return: a reandom tricep exercise from a list of tricep exercises
    """
    return choice(["tricep pushup", "skull crusher", "chair dips"])

def pullup_bar():
    """
    :return: a random pullup-bar exercise from a list of pullup-bar exercises
    """
    return choice(["wide grip pullups", "chinups", "close grip pull ups", "hang", "neutral grip hang", "neutral grip pull up"])

def seven_minute_workout():
    """
    Guides the user through the classic seven minute workout.
    :return:
    """
    read("Seven Minute Workout, here we go!")
    exercises = ["jumping jacks", "wall sit", "push ups", "sit-ups"\
                "step ups", " air squats", "chair dips", "plank"   \
                "running in place", "lunges", "push up and rotate", "side plank"]
    workout(exercises)

def upper_body_anterior_workout(rounds):
    """
    Guides the user through an upper body, anterior (front half) workout.
    Exercises consist of chest, shoulders, biceps, and core.
    :param rounds: the number of rounds to perform.
    :return:
    """
    read("Upper body anterior workout, here we go!")
    exercises = list()
    for round in range(0, rounds):
        exercises.extend([chest(), shoulders(), biceps()])
    exercises.extend([core(), core(), core()])
    workout(exercises)

def upper_body_posterior_workout(rounds):
    """
    Guides the user through an upper body, posterior (back half) workout.
    Exercises consist of back and triceps.
    :param rounds: the number of rounds to perform.
    :return:
    """
    read("Upper body posterior workout, here we go!")
    exercises = list()
    for round in range(0, rounds):
        exercises.extend([back(), triceps(), back()])
    workout(exercises)

def upper_body_antagonist_workout(rounds):
    """
    Guides the user through an upper body, antagonist workout.
    Exercises go from check -> back and then biceps -> triceps.
    :param rounds: the number of rounds to perform.
    :return:
    """
    read("Upper body antagonist workout, here we go!")
    exercises = list()
    for round in range(0, rounds):
        exercises.extend([chest(), back(), biceps(), triceps()])
    workout(exercises)

def lower_body_workout(rounds):
    """
    Guides the user through a lower body workout.
    Exercises are all legs.
    :param rounds: the number of rounds to perform.
    :return:
    """
    read("Lower body workout, here we go!")
    exercises = list()
    for round in range(0, rounds):
        exercises.extend([legs(), legs(), legs()])
    workout(exercises)

def random_workout(rounds):
    """
    Guides the user through a random workout.
    Exercise are random.
    :param rounds: the number of rounds to perform
    :return:
    """
    read("Random workout,let's get it!")
    exercises = list()
    for round in range(0, rounds*3):
        exercises.append(choice([back(), chest(), shoulders(), core(), biceps(), triceps()]))
    workout(exercises)

def pullup_bar_workout(rounds):
    """
    Guides the user through a pullup bar workout.
    Exercises are all on the pullup bar.
    :param rounds: the number of rounds to perform
    :return:
    """
    read("Pull up bar workout, here we go!")
    exercises = list()
    for round in range(0, rounds):
        exercises.extend([pullup_bar(), pullup_bar(), pullup_bar()])
    workout(exercises)

def core_workout(rounds):
    """
    Guides to user through a core/abdominal workout.
    Exercises are all core.
    :param rounds: the number of rounds to perform
    :return:
    """
    read("Core workout, here we go!")
    exercises = list()
    for round in range(0, rounds):
        exercises.extend([core(), core(), core()])
    workout(exercises)

def main():
    """
    Parses the command line options for the number of rounds and the selected workout.
    Guides the user through the selected workout for the selected number of rounds.
    :return:
    """
    parser = argparse.ArgumentParser(description='Select a workout.', epilog="Kill your workout.")
    parser.version = "1.0"
    parser.add_argument("-r", "--rounds", type=int, action="store", help="Rounds of workout to do.", choices=range(1, 6), default=3)

    # create a mutually exclusive group of options
    workouts = parser.add_mutually_exclusive_group(required=True)
    workouts.add_argument("--seven-minute", action="store_true", help="classic seven minute workout")
    workouts.add_argument("--upper-body-front", action="store_true", help="upper body, anterior workout")
    workouts.add_argument("--upper-body-back", action="store_true", help="upper body, posterior workout")
    workouts.add_argument("--upper-body-antagonist", action="store_true", help="upper body, antagonist workout")
    workouts.add_argument("--lower-body", action="store_true", help="lower body workout")
    workouts.add_argument("--pullup-bar", action="store_true", help="pullup bar workout")
    workouts.add_argument("--core", action="store_true", help="core/abdominal workout")
    workouts.add_argument("--random", action="store_true", help="random workout")

    # parse the arguments
    args = parser.parse_args()

    # get the rounds
    rounds = args.rounds

    init_tts()

    if args.seven_minute:
        seven_minute_workout()
    elif args.upper_body_front:
        upper_body_anterior_workout(rounds)
    elif args.upper_body_back:
        upper_body_posterior_workout(rounds)
    elif args.upper_body_antagonist:
        upper_body_antagonist_workout(rounds)
    elif args.lower_body:
        lower_body_workout(rounds)
    elif args.pullup_bar:
        pullup_bar_workout(rounds)
    elif args.core:
        core_workout(rounds)
    elif args.random:
        random_workout(rounds)

    stop_tts()

if __name__ == "__main__":
    main()
