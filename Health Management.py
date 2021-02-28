import pygame
import datetime
import time


def play_music_loop(file, stopper):
    ''' Takes a Music File and stopper as input and plays it until stopper is given '''
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while True:
        stopper_input_of_user = input()
        if stopper_input_of_user == stopper:
            pygame.mixer.music.stop()
            break
        if stopper_input_of_user == "q":
            exit(0)


def log_time(msg):
    '''Logs Time when Particular work is done'''
    f = open("data.txt", "a")
    f.write(f"{msg} {datetime.datetime.now()} \n")


if __name__ == "__main__":
    init_water = time.time()
    init_eyes = time.time()
    init_exercise = time.time()
    water_interval = 30*60
    eye_exercise_interval = 40*60
    physical_exercise_interval = 50*60

    while True:
        if time.time() - init_water > water_interval:
            print(f"Go And Drink Water. Type \"drank\" To Stop and \"q\" to exit.")
            play_music_loop("pubg.mp3", "drank")
            init_water = time.time()
            log_time("Water Drank at: ")

        if time.time() - init_eyes > eye_exercise_interval:
            print(f"Its Eye Exercise Time. Type \"eyesdone\" To Stop and \"q\" to exit.")
            play_music_loop("pubg.mp3", "eyesdone")
            init_eyes = time.time()
            log_time("Eye Exercise Done at: ")

        if time.time() - init_exercise > physical_exercise_interval:
            print(f"Physical Exercise Time. Type \"exercisedone\" To Stop and \"q\" to exit.")
            play_music_loop("pubg.mp3", "exercisedone")
            init_exercise = time.time()
            log_time("Physical Exercise Done at: ")

