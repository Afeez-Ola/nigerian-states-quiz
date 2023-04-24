import pandas
import turtle

# Set up screen
screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=900, height=900)
screen.addshape("nigeria40.gif")
turtle.shape("nigeria40.gif")

# Load states data from CSV
states_dict = pandas.read_csv("50_states.csv").to_dict()
states = states_dict["state"]
x_coor = states_dict["x"]
y_coor = states_dict["y"]
state_list = list(states.values())
x_list = list(x_coor.values())
y_list = list(y_coor.values())

# Initialize game variables
attempts = 50
guessed_state = []
missing_states = []


screen.exitonclick()
