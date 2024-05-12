"""average APPS student day"""

import random
from collections import deque

class State:
    """represents my states"""
    SLEEP = 0
    CRY = 1
    EAT = 2
    CODE = 3
    WALK = 4
    PLAY_VIDEOGAME = 5

class RandomEvents:
    """random events that can happen throughout the day"""
    NO_EVENT = 0

    # event №1 - I remember I have a deadline
    REMEMBER_HOMEWORK = 1

    # event №2 - I check my grades
    CHECK_GRADES = 2

    # event №2 - a friend invites me to hang out
    HANGOUT_WITH_FRIENDS = 3


HOURS_QUEUE = deque(range(24)[::-1])


class DaySimulator:
    """simulates one very fun day of my life"""
    def __init__(self) -> None:
        self.state = State.SLEEP # my initial state

        self.mood = 1 # my mood will affect the message at the end of the day

    def simulate_day(self):
        """starts the simulation"""
        while True:
            current_hour = HOURS_QUEUE.pop()

            # now let's generate a random event
            # each event has a different chance of occuring :)
            event = random.choice([0]*75 + [1]*10 + [2]*5 + [3]*10)

            # now let's get the input and begin
            input_ = random.choice((0,1))


            if self.state == State.SLEEP:
                if current_hour == 8 and input_ == 0:
                    print(f"{current_hour}:00 - Good morning! Time to eat some breakfast!")
                    self.state = State.EAT

                elif (8 < current_hour < 12 and input_ == 0) or current_hour == 12:
                    print(f"{current_hour}:00 - Oh no, I slept through the alarm! Now I don't have time for breakfast!")
                    self.state = State.CRY

                else:
                    print(f"{current_hour}:00 - Z-z-z...")


            elif self.state == State.EAT:
                if event == RandomEvents.REMEMBER_HOMEWORK:
                    print(f"{current_hour}:00 - Oh no!!! While eating I remember I have a deadline today!")
                    self.state = State.CODE

                elif event == RandomEvents.CHECK_GRADES:
                    if input_ == 0:
                        print(f"{current_hour}:00 - I check my grades while eating. The are really bad...")
                        self.state = State.CRY

                    else:
                        print(f"{current_hour}:00 - I check my grades while eating. They are great so I'll go do something fun.")
                        self.state = State.PLAY_VIDEOGAME
                elif event == RandomEvents.HANGOUT_WITH_FRIENDS:
                    if input_ == 0:
                        print(f"{current_hour}:00 - A friend texts me while I am eating and is inviting me to hangout. I'm in a good mood so I'll go.")
                        self.state = State.WALK

                    else:
                        print(f"{current_hour}:00 - A friend texts me while I am eating and is inviting me to hangout, but I don't feel like it. I'd rather play a videogame.")
                        self.state = State.PLAY_VIDEOGAME
                elif input_ == 0:
                    print(f"{current_hour}:00 - I eat an amazing meal in trapezna! Now I want to do some CodeWars problems.")
                    self.state = State.CODE

                else:
                    print(f"{current_hour}:00 - I eat an amazing meal in trapezna! Now I want to go for a walk.")
                    self.state = State.WALK


            elif self.state == State.CRY:
                self.mood -= 1
                if current_hour == 22:
                    print(f"{current_hour}:00 - I cry and go to sleep.")
                    self.state = State.SLEEP
                elif event == RandomEvents.REMEMBER_HOMEWORK:
                    print(f"{current_hour}:00 - I cry and then remember I have homework to do. This day is terrible!!!")
                    self.state = State.CODE

                elif event == RandomEvents.CHECK_GRADES:
                    if input_ == 0:
                        print(f"{current_hour}:00 - I cry and then check my grades. They are really bad...")
                    elif current_hour not in (14, 19):
                        print(f"{current_hour}:00 - I cry and then check my grades. They are great so I'll go do something fun.")
                        self.state = State.PLAY_VIDEOGAME

                elif current_hour == 14 or current_hour == 19:
                    print(f"{current_hour}:00 - I cry. Now I'm hungry!")

                elif event == RandomEvents.HANGOUT_WITH_FRIENDS:
                    if input_ == 0:
                        print(f"{current_hour}:00 - I cry. A friend texts me while I am crying and is inviting me to hangout. I want to go.")
                        self.state = State.WALK
                    else:
                        print(f"{current_hour}:00 - I cry. A friend texts me while I am crying and is inviting me to hangout, but I don't feel like it. I'd rather play a videogame.")
                        self.state = State.PLAY_VIDEOGAME
                elif input_ == 0:
                    print(f"{current_hour}:00 - I cry. Now I'll do something fun to boost my mood.")
                    self.state = State.PLAY_VIDEOGAME
                else:
                    print(f"{current_hour}:00 - I cry. Now I'll go for a walk to boost my mood.")
                    self.state = State.WALK


            elif self.state == State.CODE:
                if current_hour == 22:
                    print(f"{current_hour}:00 - I do some coding tasks and go to sleep.")
                    self.state = State.SLEEP

                elif current_hour == 14 or current_hour == 19:
                    print(f"{current_hour}:00 - I do some coding tasks. Now I'm hungry!")
                    self.state = State.EAT

                elif event == RandomEvents.HANGOUT_WITH_FRIENDS:
                    if input_ == 0:
                        print(f"{current_hour}:00 - I do some coding tasks. A friend invites me to hang out and I'm in a good mood so I'll go.")
                        self.state = State.WALK
                    else:
                        print(f"{current_hour}:00 - I do some coding tasks. A friend invites me to hang out but I don't feel like it. I'll go play a videogame instead.")
                        self.state = State.PLAY_VIDEOGAME
                elif event == RandomEvents.CHECK_GRADES:
                    if input_ == 0:
                        print(f"{current_hour}:00 - I do some coding tasks and then check my grades. They are really bad...")
                        self.state = State.CRY
                    else:
                        print(f"{current_hour}:00 - I do some coding tasks and then check my grades. They are great so I'll go do something fun.")
                        self.state = State.PLAY_VIDEOGAME

                elif input_ == 0:
                    print(f"{current_hour}:00 - I do some coding tasks. Now I want to play a videogame.")
                    self.state = State.PLAY_VIDEOGAME

                elif input_ == 1:
                    print(f"{current_hour}:00 - I do some coding tasks. Now I want to go for a walk.")
                    self.state = State.WALK


            elif self.state == State.WALK:
                place = random.choice(["Stryiskyi park", "a forest", "the city centre", "a shopping mall"])

                if current_hour == 22:
                    print(f"{current_hour}:00 - I go on a walk through {place} and go to sleep.")
                    self.state = State.SLEEP

                elif event == RandomEvents.REMEMBER_HOMEWORK:
                    print(f"{current_hour}:00 - I go on a walk through {place} and then remember I have a deadline today. Oh no!")
                    self.state = State.CODE

                elif current_hour == 14 or current_hour == 19:
                    print(f"{current_hour}:00 - I go on a walk through {place}. Now I'm hungry!")
                    self.state = State.EAT

                elif input_ == 0:
                    print(f"{current_hour}:00 - I go on a walk through {place}. Now I want to play a video game.")
                    self.state = State.PLAY_VIDEOGAME

                else:
                    print(f"{current_hour}:00 - I go on a walk through {place}. Now I want to do some CodeWars problems.")
                    self.state = State.CODE


            elif self.state == State.PLAY_VIDEOGAME:
                if current_hour == 22:
                    print(f"{current_hour}:00 - I play some videogames and go to sleep.")
                    self.state = State.SLEEP

                elif event == RandomEvents.REMEMBER_HOMEWORK:
                    print(f"{current_hour}:00 - I play some videogames and then remember I have a deadline today. Oh no!")
                    self.state = State.CODE

                elif current_hour == 14 or current_hour == 19:
                    print(f"{current_hour}:00 - I play some videogames. Now I'm hungry!")
                    self.state = State.EAT

                elif event == RandomEvents.CHECK_GRADES:
                    if input_ == 0:
                        print(f"{current_hour}:00 - I play some videogames and then check my grades. They are really bad...")
                        self.state = State.CRY
                    else:
                        print(f"{current_hour}:00 - I play some videogames and then check my grades. They are great so I'll go for a walk.")
                        self.state = State.WALK

                elif event == RandomEvents.HANGOUT_WITH_FRIENDS:
                    if input_ == 0:
                        print(f"{current_hour}:00 - I play some videogames and then my friend invites me to hang out. I'm in a good mood so I'll go.")
                        self.state = State.WALK
                    else:
                        print(f"{current_hour}:00 - I play some videogames and then my friend invites me to hang out but I don't feel like it. I want to play some more.")

                elif input_ == 0:
                    print(f"{current_hour}:00 - I play some videogames. Now I want to go for a walk.")
                    self.state = State.WALK
                else:
                    print(f"{current_hour}:00 - I play some videogames.")


            if current_hour == 23:
                if self.mood == 1:
                    print("The day is over. It was great!")
                elif self.mood == 0:
                    print("The day is over. It was quite good!")
                else:
                    print("The day is finally over. It was terrible!!!")
                break



if __name__ == "__main__":
    myday = DaySimulator()
    print("Welcome to a day in my life! :)")
    myday.simulate_day()
    print("Goodbye!")
