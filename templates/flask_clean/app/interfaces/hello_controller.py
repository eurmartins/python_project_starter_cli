from flask import Blueprint, jsonify, request
from ..usecases.hello_usecase import HelloUseCase

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'World')
    usecase = HelloUseCase()
    message = usecase.execute(name)
    return jsonify({'message': message})