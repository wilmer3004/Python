from flask import Blueprint,jsonify

main = Blueprint('index_blueprint',__name__)

@main.route('/')
def index():
    try:
        return jsonify({"Direccionamiento":"http://127.0.0.1:5000","Routes-cruds    ":{
            # Tipo Documento
            "Tipo de documento":"/TypeDoc",
            # Jornada
            "Jornada":"/Jornada",
            # Ambiente
            "Ambiente":{
                "Get" :"/Ambiente",
                "Post":"/Ambiente",
                "Put":"/Ambiente/Put/<cod>",
                "Delete":"Ambiente/Delete/<cod>",
                "GetPut":"Ambiente/get_update_ambiente/<cod>"
                },
            # Trimestre
            "Trimestre":{
                "Get" :"/Trimestre",
                "Post":"/Trimestre",
                "Put":"/Trimestre/<cod>",
                "Delete":"Trimestre/<cod>",
                "GetPut":"Trimestre/<cod>"
                },
        }})
    except Exception as ex:
        print(ex)





