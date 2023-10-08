from flask import Blueprint, jsonify, request

from src.services.AmbienteService import AmbienteService

# Definir el blueprint 
main = Blueprint('ambiente_blueprint',__name__)

# Get
@main.route('/',methods=['GET'])
def get_ambiente():
    try:
        ambientes = AmbienteService.get_ambiente()
        if len(ambientes)>0:
            return jsonify({'message':'SUCCESS','success':True,'ambientes':ambientes})
        else:
            return jsonify({'message':'NOTFOUND','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})

# Post
@main.route('/',methods=['POST'])
def add_ambiente():
    try:
        print(request.json)
        numeroAmbiente = request.json['numeroAmbiente']
        horasDisponibles = request.json['horasDisponibles']
        estadoAmbiente = request.json['estadoAmbiente']
        idSedeFK = request.json['idSedeFK']
        print(numeroAmbiente,horasDisponibles,estadoAmbiente,idSedeFK)
        if numeroAmbiente and horasDisponibles  and estadoAmbiente and idSedeFK:
            ambienteAdd = AmbienteService.add_ambiente(numeroAmbiente,horasDisponibles,estadoAmbiente,idSedeFK)
            if ambienteAdd==404:
                return jsonify({'sede':ambienteAdd,'message':'NOT ADD','success':False}),404
            elif ambienteAdd == True:
                return jsonify({'add':ambienteAdd,'message':'SUCCESS','success':True})
            else:
                return jsonify({'add':ambienteAdd,'message':'NOT ADD','success':True })
        
    except Exception as ex:
        if numeroAmbiente and horasDisponibles  and estadoAmbiente and idSedeFK:
            print(ex)
        else:
            return jsonify({'add':"400-Bad-Request",'message':'NOT ADD','success':False }),400
        return jsonify({'message':'ERROR','success':False})
    
# Put
@main.route('/Put/<cod>',methods=['PUT'])
def put_ambiente(cod):
    try:
        print(request.json)
        numeroAmbiente = request.json['numeroAmbiente']
        horasDisponibles = request.json['horasDisponibles']
        estadoAmbiente = request.json['estadoAmbiente']
        idSedeFK = request.json['idSedeFK']
        if cod and numeroAmbiente and horasDisponibles  and estadoAmbiente and idSedeFK:
            ambientePut = AmbienteService.put_ambiente(cod,numeroAmbiente,horasDisponibles,estadoAmbiente,idSedeFK)
            if ambientePut==404:
                return jsonify({'sede':ambientePut,'message':'NOT PUT','success':False})
            if ambientePut == True:
                return jsonify({'put':ambientePut,'message':'SUCCESS','success':True})
            else:
                return jsonify({'message':'NOT PUT','success':True})
    except Exception as ex:
        if cod and numeroAmbiente and horasDisponibles  and estadoAmbiente and idSedeFK:
            print(ex)
        else:
            return jsonify({'put':"400-Bad-Request",'message':'NOT PUT','success':False })
        return jsonify({'message':'ERROR','success':False})

# Delete
@main.route('/Delete/<cod>',methods=['DELETE'])
def delete_ambiente(cod):
    try:
        ambienteDelete = AmbienteService.delete_ambiente(cod)
        if ambienteDelete == True:
            return jsonify({'delete':ambienteDelete,'message':'SUCCESS','success':True})
        else:
            return jsonify({'message':'NOT DELETE','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})
    
    
# GET PUT
@main.route('/get_update_ambiente/<cod>',methods=['GET'])
def get_update_ambiente(cod):
    try:
        ambiente_get_put = AmbienteService.get_update_ambiente(cod)
        if len(ambiente_get_put)>0:
            return jsonify({'message':'SUCCESS','success':True,'ambiente':ambiente_get_put})
        else:
            return jsonify({'message':'NOTFOUND','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})



