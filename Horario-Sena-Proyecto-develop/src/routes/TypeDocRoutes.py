# Importaciones flask
from flask import Blueprint, jsonify, request
# Importaciones de service
from src.services.TypeDocService import TypeDocService

# Definir el blueprint 
main = Blueprint('typedoc_blueprint',__name__)

# Get
@main.route('/',methods=['GET'])
def get_typeDoc():
    try:
        typesDocs = TypeDocService.get_typeDoc()
        if len(typesDocs)>0:
            return jsonify({'typesdocs':typesDocs,'message':'SUCCESS','success':True})
        else:
            return jsonify({'message':'NOTFOUND','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})

# Post
@main.route('/',methods=['POST'])
def add_typeDoc():
    try:
        print(request.json)
        nameTypeDoc = request.json['nameTypeDoc']
        stateTypeDoc = request.json['stateTypeDoc']
        typeDocAdd = TypeDocService.add_typeDoc(nameTypeDoc,stateTypeDoc)
        print(typeDocAdd)
        if typeDocAdd == True:
            return jsonify({'add':typeDocAdd,'message':'SUCCESS','success':True})
        else:
            return jsonify({'message':'NOT ADD','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})
    

# Put
@main.route('/',methods=['PUT'])
def put_typeDoc():
    try:
        idTypeDoc = request.json['idTypeDoc']
        nameTypeDoc = request.json['nameTypeDoc']
        stateTypeDoc = request.json['stateTypeDoc']
        typeDocPut = TypeDocService.put_typeDoc(idTypeDoc, nameTypeDoc,stateTypeDoc)
        if typeDocPut == True:
            return jsonify({'put':typeDocPut,'message':'SUCCESS','success':True})
        else:
            return jsonify({'message':'NOT PUT','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})


# Delete
@main.route('/',methods=['DELETE'])
def delete_typeDoc():
    try:
        id = request.json['id']
        typeDocDelete = TypeDocService.delete_typeDoc(id)
        if typeDocDelete == True:
            return jsonify({'delete':typeDocDelete,'message':'SUCCESS','success':True})
        else:
            return jsonify({'message':'NOT DELETE','success':True})
    except Exception as ex:
        return jsonify({'message':'ERROR','success':False})
    