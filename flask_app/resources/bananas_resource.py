"""
Bananas API
"""
from flask import jsonify

from flask_app.extensions import app
from flask_app.models import Bananas
from flask_app.exceptions import NotFound


@app.route('/bananas', methods=['GET'])
def get_bananas():
    """
    Get all the bananas
    """
    bananas_data = Bananas.query.order_by(Bananas.id)
    bananas = list()
    for banana in bananas_data:
        bananas.append({
            'id': banana.id,
            'name': banana.name,
            'color': banana.color,
            'weight': banana.weight
        })
    return jsonify(bananas)


@app.route('/bananas/<int:banana_id>', methods=['GET'])
def get_banana(banana_id):
    """
    Get all the bananas
    """
    banana_record = Bananas.query.get(banana_id)
    if not banana_record:
        raise NotFound(banana_id)
    banana = {
        'id': banana_record.id,
        'name': banana_record.name,
        'color': banana_record.color,
        'weight': banana_record.weight
    }
    return jsonify(banana)
