from turtle import Screen, Turtle
import pandas
screen = Screen()
turtle = Turtle()
screen.title("U.S States Game")
file_path_of_the_image = "blank_states_img.gif"
screen.addshape(file_path_of_the_image)
turtle.shape(file_path_of_the_image)

data = pandas.read_csv("50_states.csv")
# list_of_states = list(data.state)
# print(list_of_states)

def check_the_answer(answer_state):
    if answer_state in data.state.to_list():
        return True
    else:
        return False

def write_the_state_on_the_map(answer_state):
    state_with_coordinates = data[data.state == answer_state]
    print(type(state_with_coordinates.x))
    coordinates_x = int(state_with_coordinates.x)
    coordinates_y = int(state_with_coordinates.y)
    coordinates_of_x_and_y = (coordinates_x, coordinates_y)
    return coordinates_of_x_and_y

all_states = data.state.to_list()
missing_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    state = check_the_answer(answer_state)
    if answer_state == "Exit":
        break
    if state:
        guessed_states.append(answer_state)
        coordinates = write_the_state_on_the_map(answer_state)
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(coordinates)
        new_turtle.write(answer_state)
        missing_states.remove(answer_state)

with open ("missing_states.csv", mode="w") as file:
    print(missing_states)
    new_data = pandas.DataFrame(missing_states)
    print(new_data)
    new_data.to_csv("states_to_learn.csv")

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()