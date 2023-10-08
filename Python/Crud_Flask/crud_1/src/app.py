from flask import Flask, render_template, request, redirect, session, url_for
import os 
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src','templates')

app = Flask(__name__ ,template_folder = template_dir)

# Rutas de la aplicación

@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM usuario")
    myresult = cursor.fetchall()
    # convertir lo datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames,record)))
    cursor.close()
    return render_template('index.html', data=insertObject)


# Ingresar usuarios en la base de datos

@app.route('/user', methods=['POST'])
def addUser():
    username = request.form['username']
    password = request.form['password']
    
    if username and password:
        cursor = db.database.cursor()
        sql = "INSERT INTO usuario (NombreUsuario, ContrasenaUsuario) VALUES (%s,%s)"
        data = (username, password)
        cursor.execute(sql,data)
        db.database.commit()
    return redirect(url_for('home'))
        
# -------------------------------------------
# Eliminar
@app.route('/delete/<string:id>')

def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM usuario WHERE IdUsuario=%s"
    data = (id,)
    cursor.execute(sql,data)
    db.database.commit()
    return redirect(url_for('home'))

# -------------------------------------------
# Editar
@app.route('/edit/<string:id>',methods=['POST'])

def edit(id):
    username = request.form['username']
    password = request.form['password']
    
    if username and password:
        cursor = db.database.cursor()
        sql = "UPDATE usuario SET NombreUsuario = %s, ContrasenaUsuario= %s WHERE IdUsuario = %s"
        data = (username, password,id)
        cursor.execute(sql,data)
        db.database.commit()
    return redirect(url_for('home'))


# -------------------------------------------
# redireccion a la pagina login
@app.route('/login')
def login():
    return render_template('/view/login.html')
# -------------------------------------------
# redireccion a la pagina admin
@app.route('/admin')
def admin():
    return render_template('/view/admin.html')
# ----------------------------------------
# validación login
@app.route('/login1',methods=['GET','POST'])
def login1():
    
    if 'txtusername' in request.form and 'txtpassword':
        username = request.form['txtusername']
        password = request.form['txtpassword']
        cursor = db.database.cursor()
        sql = "SELECT * FROM usuario WHERE NombreUsuario = %s AND ContrasenaUsuario= %s"
        data = (username, password,)
        cursor.execute(sql,data)
        account = cursor.fetchone()
        print(account)
        if account:
            session['logueado']=True
            session['IdUsuario'] = account[0]
            return render_template('/view/admin.html')
        else:
            return redirect(url_for('home'))
        

# ----------------------------------------------
# puerto para correr el código de manera local

if __name__ == '__main__':
    app.secret_key="This is a secret"
    app.run(debug=True, port=5000)


# -------------------------------------------------------------





