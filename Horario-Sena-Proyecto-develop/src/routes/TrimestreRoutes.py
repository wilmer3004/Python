from flask import Blueprint, jsonify, request

from src.services.TrimestreService import TrimestreService

# Definir el blueprint 
main = Blueprint('trimestre_blueprint',__name__)

# Get
@main.route('/',methods=['GET'])
def get_trimestre():
    try:
        trimestres = TrimestreService.get_timestre()
        if len(trimestres)>0:
            return jsonify({'message':'SUCCESS','success':True,'trimestres':trimestres, 'DATE FORMAT':'%Y-%m-%d' }),200
        else:
            return jsonify({'message':'NOTFOUND','success':True, 'DATE FORMAT':'%Y-%m-%d' }),400
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})

# Post
@main.route('/',methods=['POST'])
def add_trimestre():
    try:
        print(request.json)
        nombreTrimestre = request.json['nombreTrimestre']
        fechaInicio = request.json['fechaInicio']
        fechaFin = request.json['fechaFin']
        estadoTrimestre = request.json['estadoTrimestre']
        if nombreTrimestre and fechaInicio  and fechaFin and estadoTrimestre:
            trimestreAdd = TrimestreService.add_trimestre(nombreTrimestre,fechaInicio,fechaFin,estadoTrimestre)
            if trimestreAdd == True:
                return jsonify({'add':trimestreAdd,'message':'SUCCESS','success':True}),200
            else:
                return jsonify({'add':trimestreAdd,'message':'NOT ADD','success':True, 'DATE FORMAT':'%Y-%m-%d' }),400
    except Exception as ex:
        if nombreTrimestre and fechaInicio  and fechaFin and estadoTrimestre:
            print(ex)
        else:
            return jsonify({'add':"400-Bad-Request",'message':'NOT ADD','success':False }),400
        return jsonify({'message':'ERROR','success':False})
    

# Put
@main.route('/<cod>',methods=['PUT'])
def put_trimestre(cod):
    try:
        print(request.json, cod)
        nombreTrimestre = request.json['nombreTrimestre']
        fechaInicio = request.json['fechaInicio']
        fechaFin = request.json['fechaFin']
        estadoTrimestre = request.json['estadoTrimestre']
        trimestrePut = TrimestreService.put_trimestre(cod,nombreTrimestre,fechaInicio,fechaFin,estadoTrimestre)
        trimestre_get_put = TrimestreService.get_update_Trimestre(cod)
        if trimestrePut == True:
            return jsonify({'put':trimestrePut,'message':'SUCCESS','success':True,"updated data":trimestre_get_put}),200
        else:
            return jsonify({'message':'NOT PUT','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})


# Delete
@main.route('/<cod>',methods=['DELETE'])
def delete_trimestre(cod):
    try:
        trimestreDelete = TrimestreService.delete_trimestre(cod)
        if trimestreDelete == True:
            return jsonify({'delete':trimestreDelete,'message':'SUCCESS','success':True})
        else:
            return jsonify({'message':'NOT DELETE','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})
    
    
# GET PUT
@main.route('/<cod>',methods=['GET'])
def get_update_trimestre(cod):
    try:
        trimestre_get_put = TrimestreService.get_update_Trimestre(cod)
        if len(trimestre_get_put)>0:
            return jsonify({'message':'SUCCESS','success':True,'trimestre':trimestre_get_put})
        else:
            return jsonify({'message':'NOTFOUND','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})

    