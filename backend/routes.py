from app import app, db
from flask import request, jsonify
from models import Friend

# Get all friends
@app.route("/api/friends", methods=["GET"])
def get_friends():
    friends = Friend.query.all() # = "SELECT * FROM FRIENDS"
    print(friends)
    result = [friend.to_json() for friend in friends]
    return jsonify(result), 200

# Create a friend
@app.route("/api/friends", methods=["POST"])
def create_friend():
    try:
        data = request.json # opposite of jsonify
        
        name = data.get("name")
        role = data.get("role")
        description = data.get("description")
        gender = data.get("gender")

        # Fetch avatar image based on gender
        if gender == "male":
            img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
        elif gender == "female":
            img_url = f"https://avatar.iran.liara.run/public/girl?username={name}"
            pass
        else:
            img_url = None # always have a fallback just in case

        new_friend = Friend(name=name, role=role, description=description, gender=gender, img_url=img_url)
        db.session.add(new_friend)
        db.session.commit()

        return jsonify({"msg": "Friend created successfully"}), 201 # resource created
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500
    
# int:id is flask syntax that creates a dynamic variable
@app.route("/api/friends/<int:id>",methods=["DELETE"])
def delete_friend(id):
    print(id)
    try:
        friend = Friend.query.get(id)
        if friend is None:
            return jsonify({"error":"Friend not found"}), 404

        db.session.delete(friend)
        db.session.commit()
        return jsonify({"msg":"friend deleted"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error":str(e)}), 500