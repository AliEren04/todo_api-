from flask import Blueprint
from flask import jsonify, request
todo = Blueprint("todo", __name__, url_prefix="/api/todos/")


@todo.route("/view", methods=["GET"])
def get_todos():
    return jsonify({"success": True, "todos": []}), 200


@todo.route("/view/<todo_id>", methods=["GET"])
#Example just implement real db context later
def get_todo(todo_id):
    
    if(int(todo_id) == 0):
        return jsonify({"Success": False, "Message": "Todo not found"}), 404
    else: 
        return jsonify({"Success": True, "Todo": todo_id}), 200


@todo.route("/create", methods=["POST"])
#Example just implement real db context later
def create_todo():
    data = request.get_json()
    return jsonify({"Success": True, "Created Todo": data}), 201


@todo.route("/update/<todo_id>", methods=["PUT"])
#Example just implement real db context later
def update_todo(todo_id):

    data = request.get_json()

    if(int(todo_id) == 0):
        return jsonify({"Success": False, "Message": "Todo not found"}), 404
    else:
        return jsonify({"Success": True, "Updated Todo's ID": int(todo_id), "Updated Todo": data}), 200


@todo.route("/delete/<todo_id>", methods=["DELETE"])
#Example just implement real db context later
def delete_todo(todo_id):
    data = request.get_json()
    if(int(todo_id) == 0):
        return jsonify({"Success": False, "Message": "Todo not found"}), 404
    else:
        return jsonify({"Success": True, "Deleted Todo's ID": int(todo_id), "Deleted Todo": data}), 200

