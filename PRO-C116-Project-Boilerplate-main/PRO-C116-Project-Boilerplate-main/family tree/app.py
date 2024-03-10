# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Divjot" # write your name
    age = "13" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def home_1():

    name = "Ram" # write your name
    age = "42" # write your age

    return render_template('index.html' , name = name , age = age)


# define the route to mother webpage
@app.route("/mother")
def home_2():

    name = "Laxmi" # write your name
    age = "38" # write your age

    return render_template('index.html' , name = name , age = age)


# define the route to friends webpage
@app.route("/friend")
def home_3():

    name = "God, Jesus, Bhagwaan, Allah, Sai, Parmatma, Vishnu, MahaDev, Waheguru, Rabb, Gautam Budh." # write your name
    age = "He is beyond time, death, birth, fear. " # write your age

    return render_template('index.html' , name = name , age = age)


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
