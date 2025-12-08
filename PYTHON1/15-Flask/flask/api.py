from flask import Flask, jsonify, request
# Import Flask framework, jsonify (to return JSON), and request (to get request data)

app = Flask(__name__)
# Create a Flask application instance


# Initial Data in my to do list
items = [
    {'id': 1, 'name': "Item1", 'description': "This is item 1"},
    {'id': 2, 'name': "Item2", 'description': "This is item 2"},
]
# In-memory list to store to-do items


@app.route('/')
# Route for home page
def home():
    return "Welcome to the To-Do List APP!"
    # Returns a simple welcome message


# Get : Retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)
    # Convert items list to JSON and return it


# Get : Retrieve a specific item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Find item with matching id
    item = next((item for item in items if item["id"] == item_id), None)
    
    if item is None:
        return jsonify({"error": 'Item not found'})
        # Return error if item does not exist
    
    return jsonify(item)
    # Return the found item as JSON


# Post : Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    # Check if request body exists and contains 'name'
    if not request.json or 'name' not in request.json:
        return jsonify({"error": "Item not found"})
    
    # Create a new item dictionary
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,  # Auto-increment id
        "name": request.json['name'],              # Get name from request
        "description": request.json.get('description')  # Get description if present
    }
    
    items.append(new_item)
    # Add new item to list
    
    return jsonify(new_item)
    # Return newly added item


# Put : Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    # Find the item to update
    item = next((item for item in items if item["id"] == item_id), None)

    if item is None:
        return jsonify({"error": "Item not found"})
        # Return error if item not found
    
    # Update item fields if provided
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])

    return jsonify(item)
    # Return updated item


# Delete : Remove an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    # Replace items list excluding the deleted item
    items = [item for item in items if item["id"] != item_id]
    
    return jsonify({"result": "Item deleted"})
    # Confirm deletion


if __name__ == '__main__':
    app.run(debug=True)
    # Run Flask app in debug mode
