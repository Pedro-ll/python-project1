import random


# Can't reinitialize game after losing all lives 
# Can't handle inputs that arent A,B,C,D 


# define rooms

game_room = {
    "name": "game room",
    "type": "room",
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "bedroom",
}


bedroom_2 = {
    "name": "bedroom 2",
    "type": "bedroom",
}

living_room = {
    "name": "living room",
    "type": "room",
}

outside = {
  "name": "outside"
}


#Define Items

#Itmens in game room

couch = {
    "name": "couch",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

piano = {
    "name": "piano",
    "type": "furniture",
}


#Items bedroom 1

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}


door_b = {
    "name": "door b",
    "type": "door",
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}


door_c = {
    "name": "door c",
    "type": "door",
}

# Items in bedroom 2

double_bed = {
    "name": "double bed",
    "type": "furniture",
}


dresser = {
    "name": "dresser",
    "type": "furniture",
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}


door_d = {
    "name": "door d",
    "type": "door",
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}



#Items in Living Room

dining_table = {
    "name": "dining table",
    "type": "furniture",
}




from optparse import Values
import PySimpleGUI as sg
def interface_1(a,b):
    event, values = sg.Window(a, [[sg.Text('Interface')],[sg.Text(b)], [sg.Input()], [sg.OK(), sg.Cancel()] ], size=(600,110)).read(close=True)
    print(values[0])
    return values[0]



def interface_2(a):
    event, values = sg.Window('Interface', [[sg.Text(a)], [sg.Input()], [sg.OK(), sg.Cancel()] ],size=(600,110) ).read(close=True)
    return 


all_rooms = [game_room,bedroom_1,bedroom_2,living_room, outside]

all_doors = [door_a,door_b,door_c,door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "piano": [key_a],
    "door a": [game_room, bedroom_1],
    "bedroom 1": [door_a,door_b,door_c,queen_bed],
    "queen bed":[key_b],
    "door b":[bedroom_1,bedroom_2],
    "bedroom 2":[door_b,double_bed,dresser],
    "dresser":[key_d],
    "double bed":[key_c],
    "door c":[bedroom_1,living_room],
    "living room":[door_c,dining_table,door_d],
    "door d":[living_room,outside]
}


# Questions dict and variables


question = {"Which character was first played by Arnold Schwarzenegger in a 1984 film?":
            {"A": "A: The Demonstrator", "B": "B: The Instigator", "C": "C: The Investigator", "D": "D: The Terminator", "correct": "D"}, 
            'what name is given to the person who traditionally attends the groom on his wedding day?': {"A": "A: Best man", "B": "B: Top man", "C": "Old man", "D": "Poor man", "correct": "A"}, 
           "California has alomost the same population as...": {"A": "A: The United Kingdom", "B": "B: Spain", "C": "C: Italy", "D": "D: Poland", "correct": "D"},"Which is a chain of international hotels?": {"A": "A: Four Tops","B":"B: Four Pennies","C": "C: Four Seasons","D":"D:Four Posters","correct": "C"} }


question_presented = 0
options = 0
correct_answer = 0 


# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside,
    "lives": 5
}

# define variable game_state
game_state={"current_room":game_room}



def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    interface_2("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. \n You don't remember why you are here and what had happened before. You feel some unknown danger is approaching \n and you must get out of the house, NOW! \n Press Ok")
    #print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        interface_2("Congrats! You escaped the room!")
        #print("Congrats! You escaped the room!")
    else:
        interface_2("You are now in " + room["name"] +"\n Press OK")
        #print("You are now in " + room["name"])
        intended_action =interface_1("What would you like to do? Type 'explore' or 'examine'?","What would you like to do? Type 'explore' or 'examine'?").strip()
        #intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        linebreak()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(interface_1("What would you like to examine?","What would you like to examine?").strip())
            #examine_item(input("What would you like to examine?").strip())
            linebreak()
        else:
            interface_2("Not sure what you mean. Type 'explore' or 'examine'. \n Press OK")
            # print("Not sure what you mean. Type 'explore' or 'examine'.")
            linebreak()
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    interface_2("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items)+"\n Press OK")
    #print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))
    linebreak()

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            interface_2("You examine " + item_name + ". \n Press ok")
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    give_question = randomize_question() 
                    interface_2("You unlock it with a key you have. \n Press ok")
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    interface_2("It is locked but you don't have the key. \n Press ok")
                    output += "It is locked but you don't have the key."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    interface_2("You find " + item_found["name"] + "."+"Press OK")
                    output += "You find " + item_found["name"] + "."
                else:
                    interface_2("There isn't anything interesting about it.")
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if(output is None):
        interface_2("The item you requested is not found in the current room. \n Press Ok")
        #print("The item you requested is not found in the current room.")
        linebreak()
    
    if(next_room and interface_1("Do you want to go to " + next_room['name'] + "? Enter 'yes' or 'no'","Do you want to go to " + next_room['name'] + "? Enter 'yes' or 'no'").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)

def answer_question ():
    
    while game_state['lives']> 0:
        
        interface_2("You have the key! But don't get ahead of yourself, you have to answer a little question first!")
            
        a = interface_1(question_presented + "\n" + options[0] + " " + options[1] + " " + options[2] + " " + options[3] + " answer A, B, C or D",question_presented + "\n" + options[0] + " " + options[1] + " " + options[2] + " " + options[3] + " answer A, B, C or D")

        if a == correct_answer:
            interface_2("That's correct, the door has unlocked!")       
        
        elif a != correct_answer:
            game_state['lives'] -= 1
            interface_2("Wrong! Try again!")
            interface_2("you have " + str(game_state["lives"]) + " lives left!")
            randomize_question()

    
        
        else: 
            interface_2("wrong answer, type A, B, C or D")
            answer_question()
    return interface_2('You have lost the game!!!! Better luck next time') 
        
def randomize_question():
    
    global question_presented 
    global options
    global correct_answer
    


    question_presented = random.choice(list(question.keys()))
    options = [i for i in question[question_presented].values()][:-1]
    correct_answer = question[question_presented]['correct']
   
    input_question = answer_question() 


game_state = INIT_GAME_STATE.copy()


while game_state['lives']>0:
    start_game()




