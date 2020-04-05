from flask import Flask, request
from flask import Response
from database.db import initialize_db
from database.models import User

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/register-box'
}

initialize_db(app)


@app.route('/box')
def get_boxes():
    """
    This route will be get all boxes records
    """
    boxes = User.objects().to_json()

    return Response(boxes, mimetype="application/json", status=200)


@app.route('/box', methods=['POST'])
def add_record():
    banknotes = [100, 50, 10, 5, 1]
    coins = [0.50, 0.10, 0.05, 0.01]

    body = request.get_json()
    total_value = body.get('total_value')
    payment_value = body.get('payment_value')

    if payment_value < total_value:
        raise Exception(f'The amount paid is less than total')
    else:
        count = 0
        while total_value > 0:
            value = (total_value / banknotes[count]) / coins[count]
            n = (total_value % banknotes[count]) / coins[count]

            if int(value) is not 0:
                return '%d banknotes of $ %.2f' % (n, banknotes[count])

            count += 1


@app.route('/box', methods=['PUT'])
def update_register():
    body = request.get_json()

    reg = User.objects.get(id=id).update(**body)

    if reg is not None:
        return '', 200
    else:
        raise Exception('This register not exists')


@app.route('/box/<id>', methods=['DELETE'])
def delete_register(id):
    reg = User.objects.get(id).delete()

    if reg is not None:
        return '', 200
    else:
        raise Exception('This register not exists')


app.run()
