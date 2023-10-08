
from flask import Blueprint, jsonify, request

from src.services.ProgramaService import ProgramaService

main = Blueprint('programa_blueprint',__name__)

@main.route('/',methods=['GET'])
def get_programa():
    print("ENTRO000000000000000000")
    try:
        print("ENTRO000000000000000000 AL TRY")
        programas = ProgramaService.get_programa()
        if len(programas)>0:
            return jsonify({'message':'SUCCESS','success':True,'programas':programas, 'DATE FORMAT':'%Y-%m-%d' })
        else:
            return jsonify({'message':'NOTFOUND','success':True, 'DATE FORMAT':'%Y-%m-%d' })
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})


@main.route('/',methods=['POST'])
def add_Jornada():
    try:
        print(request.json)
        nombrePrograma = request.json['nombrePrograma']
        descripcionProgram = request.json['descripcionProgram']
        versionPrograma = request.json['versionPrograma']
        estadoPrograma = request.json['estadoPrograma']
        programaAdd = ProgramaService.add_Programa(nombrePrograma,descripcionProgram,versionPrograma,estadoPrograma)
        print(programaAdd)
        if programaAdd == True:
            return jsonify({'add':programaAdd,'message':'SUCCESS','success':True})
        else:
            return jsonify({'message':'NOT ADD','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})

@main.route('/',methods=['PUT'])
def put_typeDoc():
    try:
        idPrograma= request.json['idPrograma']
        nombrePrograma = request.json['nombrePrograma']
        descripcionProgram = request.json['descripcionProgram']
        versionPrograma = request.json['versionPrograma']
        estadoPrograma = request.json['estadoPrograma']
        programaPut = ProgramaService.put_programa(idPrograma,nombrePrograma,descripcionProgram,versionPrograma,estadoPrograma)
        if programaPut == True:
            return jsonify({'put':programaPut,'message':'SUCCESS','success':True})
        else:
            return jsonify({'message':'NOT PUT','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})

@main.route('/Delete/<cod>',methods=['DELETE'])
def delete_programa(cod):
    try:
        programaDelete = ProgramaService.delete_programa(cod)
        if programaDelete == True:
            return jsonify({'put':programaDelete,'message':'SUCCESS','success':True})
        else:
            return jsonify({'message':'NOT PUT','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})

# GET PUT
@main.route('/<cod>',methods=['GET'])
def get_update_programa(cod):
    try:
        print(request.json)
        programa_get_put = ProgramaService.get_update_Programa(cod)
        if len(programa_get_put)>0:
            return jsonify({'message':'SUCCESS','success':True,'trimestre':programa_get_put})
        else:
            return jsonify({'message':'NOTFOUND','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})
