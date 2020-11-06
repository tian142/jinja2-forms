from flask import Flask, request, render_template
import random

app = Flask(__name__)


def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')


@app.route('/froyo')
def choose_froyo():
    return render_template('froyo_form.html')


@app.route('/froyo_results')
def show_froyo_results():
    context = {
        "users_froyo_flavor": request.args.get('flavor'),
        "users_toppings": request.args.get('toppings')
    }

    return render_template('froyo_results.html', **context)


@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action = "/favorites_results" method = "GET" >
        What is your favorite color? < br/>
        <input type = "text" name = "color" > <br/>
        What is your favorite animal? < br/>
        <input type = "text" name = "animal" > <br/>
        What is your favorite city? < br/>
        <input type = "text" name = "city" > <br/>
        <input type = "submit" value = "Submit!" >
    </form >
    """


@app.route('/favorites_results')
def favorites_results():
    users_color = request.args.get('color')
    users_animal = request.args.get('animal')
    users_city = request.args.get('city')
    return f"Wow, I didn't know {users_color} {users_animal} lived in {users_city}!"


@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action = "/message_results" method = "POST" >
        Enter a secret message < br/>
        <input type = "text" name = "message" > <br/>
        <input type = "submit" value = "Submit!" >
    </form >
    """


@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_message = request.form.get('message')
    message = ("Here is your secret message! <br/>"
               f"{users_message}"
               )
    return message


@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')


@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    input1 = request.args.get('operand1')
    input2 = request.args.get('operand2')
    math_operation = request.args.get('operation')

    result = ''

    if math_operation == 'add':
        result = int(input1) + int(input2)
    elif math_operation == 'subtract':
        result = int(input1) - int(input2)
    elif math_operation == 'multiply':
        result = int(input1) * int(input2)
    else:
        result = int(input1) / int(input2)

    context = {
        "input1": request.args.get('operand1'),
        "input2": request.args.get('operand2'),
        "math_operation": request.args.get('operation'),
        "result": result
    }

    return render_template('calculator_results.html', **context)


# List of compliments to be used in the `compliments_results` route (feel free
# to add your own!)
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]


@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')


@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    context = {
        # TODO: Enter your context variables here.
    }

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
