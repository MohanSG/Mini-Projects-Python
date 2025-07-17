import turtle
import pandas

score = 0
guessed_states = []
missed_states = []

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.bgpic(image)

turtle.penup()
turtle.color('black')
turtle.hideturtle()

data = pandas.read_csv("50_states.csv")
states_dict = data.to_dict(orient="records")
all_states = data['state'].to_list()

def check_answer(user_answer):
    for state in states_dict:
        if state['state'] == user_answer:
            return True

def get_state_coords(answer):
    for state in states_dict:
        if state['state'] == answer:
            return (state['x'], state['y'])
        
def export_missed_states():
    for state in all_states:
        for guessed_state in guessed_states:
            if state == guessed_state:
                all_states.remove(guessed_state)
    
    list_to_export = pandas.DataFrame(all_states)
    list_to_export.to_csv('missed_states.csv')


while score < 50:
    guess = turtle.textinput(title="Guess the state", prompt=f"{score}/50 states correct")
    answer = guess.title()
    
    if guess == "exit":
        export_missed_states()
        break
    if check_answer(answer):
        guessed_states.append(answer)
        score += 1
        turtle.goto(get_state_coords(answer))
        turtle.write(answer, move=False, align="center", font= ("Arial", 10, "normal"))

screen.mainloop()