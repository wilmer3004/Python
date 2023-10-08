from flask import Blueprint, jsonify, request

from src.services.JornadaService import JornadaService

main = Blueprint('jornada_blueprint',__name__)

@main.route('/',methods=['GET'])
def get_jornada():
    try:
        typesJornada = JornadaService.get_jornada()
        if len(typesJornada)>0:
            return jsonify({'typesjornada':typesJornada,'message':'SUCCESS','success':True})
        else:
            return jsonify({'message':'NOTFOUND','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})
    
@main.route('/',methods=['POST'])
def add_Jornada():
    try:
        print(request.json)
        nameJornada = request.json['nameJornada']
        diaIniJor = request.json['diaIniJor']
        diaFinJor = request.json['diaFinJor']
        estadoJornada = request.json['estadoJornada']
        jornadaAdd = JornadaService.add_Jornada(nameJornada,diaIniJor,diaFinJor,estadoJornada)
        print(jornadaAdd)
        if jornadaAdd == True:
            return jsonify({'add':jornadaAdd,'message':'SUCCESS','success':True})
        else:
            return jsonify({'message':'NOT ADD','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})
    

@main.route('/',methods=['PUT'])
def put_Jornada():
    try:
        idJornada = request.json['idJornada']
        nameJornada = request.json['nameJornada']
        diaIniJor = request.json['diaIniJor']
        diaFinJor = request.json['diaFinJor']
        estadoJornada = request.json['estadoJornada']
        jornadaPut = JornadaService.put_jornada(idJornada,nameJornada,diaIniJor,diaFinJor,estadoJornada)
        if jornadaPut == True:
            return jsonify({'put':jornadaPut,'message':'SUCCESS','success':True})
        else:
            return jsonify({'message':'NOT PUT','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})


# delete
@main.route('/DeleteJornada/<cod>',methods=['DELETE'])
def delete_typeDoc(cod):
    try:
        JornadaDelete = JornadaService.delete_jornada(cod)
        if JornadaDelete == True:
            return jsonify({'delete':JornadaDelete,'message':'SUCCESS','success':True})
        else:
            return jsonify({'message':'NOT DELETE','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})
    
