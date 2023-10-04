from flask import Flask, render_template, request

app = Flask(__name__)

# For demonstration purposes, we'll use a list to store food items
food_items = []

@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/add_food', methods=['POST'])
def add_food():
    food_name = request.form['food_name']
    quantity = request.form['quantity']
    expiry_date = request.form['expiry_date']

    # Create a dictionary to represent the food item
    food_item = {
        'name': food_name,
        'quantity': quantity,
        'expiry_date': expiry_date
    }

    # Add the food item to the list
    food_items.append(food_item)

    # Redirect back to the menu after adding food
    return render_template('menu.html')

@app.route('/delete_food', methods=['POST'])
def delete_food():
    food_to_delete = request.form['food_to_delete']

    # Find and remove the food item from the list (by name)
    for food_item in food_items:
        if food_item['name'] == food_to_delete:
            food_items.remove(food_item)

    # Redirect back to the menu after deleting food
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)
