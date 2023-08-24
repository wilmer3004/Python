from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})
from products import products

@app.route('/ping')
def ping():
    return jsonify({"mensaje":"Pong"})

@app.route('/products',methods=['GET','POST'])  
def getProducts():
    data={"products":products}
    return jsonify(data)

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product ['name']== product_name]
    if (len(productsFound)>0):
        return jsonify({'product':productsFound[0]})
    return jsonify({'message':'Product not found'})



if __name__ == '__main__':
    app.run(debug=True,port=5000)

