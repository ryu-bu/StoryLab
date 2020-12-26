from flask import Blueprint, request, jsonify, session
from models.chat import Chat

api = Blueprint('api', __name__)

@api.route('/lines', methods=['GET', 'POST'])
def api_lines():
    if request.method == 'GET':
        line_list = []
        lines = Chat.objects()

        for line in lines:
            line_list.append({
                "user": line.user,
                "message": line.message
            })

        # print(line_list)
        return jsonify(line_list)


def upload_db(item):
    line = Chat(user=item['user'], message=item['message'])
    line.save()
