from flask import Blueprint, request, jsonify, render_template
from model.huffmanCode.huffman import encode_message, decode_message

compress_bp = Blueprint('compress', __name__)

@compress_bp.route('/compress', methods=['POST', 'GET'])
def compress():
    if request.method == 'POST':
        data = request.json
        input_text = data.get('texto')
        if input_text:
            try:
                encoded_text, encoding_dict = encode_message(input_text)
                return jsonify({'texto_comprimido': encoded_text, 'diccionario': encoding_dict})
            except Exception as e:
                return jsonify({'error': str(e)})
        return jsonify({'error': 'No se recibió el texto a comprimir'})
    return render_template('index.html')

@compress_bp.route('/decompress', methods=['POST'])
def decompress():
    data = request.json
    input_text = data.get('texto')
    encoding_dict = data.get('diccionario')
    if input_text and encoding_dict:
        try:
            decoded_text = decode_message(input_text, encoding_dict)
            return jsonify({'texto_descomprimido': decoded_text})
        except Exception as e:
            return jsonify({'error': str(e)})
    return jsonify({'error': 'No se recibió el texto a descomprimir o el diccionario de codificación'})
