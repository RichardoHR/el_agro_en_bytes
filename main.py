from flask import Flask, render_template, request, session
from database import User


app = Flask(__name__)
app.secret_key = ''


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/registro/', methods = ['GET', 'POST'])
def registro():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:
            user = User.create(username = username, password = password)
            session['user'] = user.username

 
    return render_template("registro.html")

@app.route('/login/')
def login():
#    if request.method == "POST":
#        username = request.form.get('username')
#       password = request.form.get('password')

    return "Sección en construccion"



@app.route('/hilera_sencilla/', methods = ['GET', 'POST'])
def hilera_sencilla():
    while True:
        try:
            ancho_cama_siembra = float(request.form.get('ancho', True ))
            if ancho_cama_siembra <= 0:
                return render_template ("aviso_1.html")
            metros_lineales = 10000 / ancho_cama_siembra
            sem_recom_ha = int(request.form.get('semillas', True))
            if sem_recom_ha <= 0:
                return render_template ("aviso_2.html")
            dist_entre_semillas = round((metros_lineales / sem_recom_ha) * 100, 2)
            return render_template('hilera.html', salida_hilera_sencilla = f"La distancia recomendada para establecer las semillas o plantas a hilera sencilla es de: {dist_entre_semillas} centimetros *CALIBRE SU SEMBRADORA*")
            break
        except ValueError:
            return render_template('hilera.html', salida_hilera_sencilla = f"¡¡¡AVISO!!!. Por favor ingrese solamente NÚMEROS. Verifique su información e inténtelo de nuevo.")


@app.route('/hilera_fertil/', methods = ['GET', 'POST'])
def hilera_fertil():
    while True:
        try:
            ancho_cama_siembra = float(request.form.get('ancho', True))
            metros_lineales = 10000 / ancho_cama_siembra
            cant_fert_ha = float(request.form.get('fertilizante', True))
            fert_metro_lineal = round((cant_fert_ha / metros_lineales) * 1000, 2)
            return render_template('hilera.html', salida_fert_metro_lineal = f"La cantidad a aplicar de fertilizante por METRO LINEAL es de {fert_metro_lineal} gramos. *CALIBRE SU FERTILIZADORA*")
            break
        except ValueError:
            return "Se esperan solamente numeros positivos. Intente otra vez"
        

@app.route('/grano_pequeño/', methods = ['GET', 'POST'])
def grano_pequeño():
    while True:
        try:
            ancho_cama_siembra = float(request.form.get('ancho', True))
            metros_lineales = 10000 / ancho_cama_siembra
            sem_ha = float(request.form.get('semilla', True))
            sem_metro_lineal = sem_ha / metros_lineales
            NUM_HILERAS = 2
            gramos_metro_lineal = round((sem_metro_lineal / NUM_HILERAS) * 1000, 2)
            return render_template('grano_pequeño.html', salida_gramos_metro_lineal = f"La cantidad de semilla o fertilizante a utilizar para siembra a DOBLE HILERA por METRO LINEAL es de {gramos_metro_lineal} gramos por chuzo. *CALIBRE SU SEMBRADORA/FERTILIZADORA*")
            break
        except ValueError:
            return "Se esperan solamente numeros positivos. Intente otra vez"


@app.route('/grano_peq_plano/', methods = ['GET', 'POST'])
def grano_peq_plano():
    while True:
        try:
            distancia_entre_chusos = float(request.form.get('distancia_chuzos', True))
            metros_lineales = 10000 / distancia_entre_chusos
            sem_fert_ha = float(request.form.get('semilla_fertilizante', True))
            sem_fert_metro_lineal = round((sem_fert_ha / metros_lineales) * 1000, 2)
            return render_template('grano_pequeño.html', salida_sem_fert_metro_lineal = f"La cantidad de semilla o fertilizante a utilizar para siembra en PLANO por METRO LINEAL es de {sem_fert_metro_lineal} gramos por chuzo. *CALIBRE SU SEMBRADORA/FERTILIZADORA*")
            break
        except ValueError:
            return "Se esperan solamente numero positivos. Intente otra vez"
        

@app.route('/tresbolillo/', methods = ['GET', 'POST'])
def tresbolillo():
    while True:
        try:
            dist_arb = float(request.form.get('distancia', True))
            cant_arb_m2 = dist_arb * dist_arb * 0.866
            arb_ha = round(10000 / cant_arb_m2)
            return render_template('tresbolillo.html', salida_tresbolillo = f"La cantidad de arboles a establecer por hectarea es de {arb_ha}, a una distancia de {dist_arb} metros")
            break
        except ValueError:
            return "Se esperan solamente numeros positivos. Intente otra vez"


@app.route('/marco_cuadrarectangular/', methods = ['GET', 'POST'])
def marco_cuadrarectangular():
    while True:
        try:
            distancia_entre_plantas = float(request.form.get('distancia', True))
            ancho_cama_siembra = float(request.form.get('ancho', True))
            arb_ha = round(10000 / (ancho_cama_siembra * distancia_entre_plantas))
            return render_template('tresbolillo.html', salida_cuadrarectangular = f"El número de árboles para establecimiento por hectárea es de {arb_ha} con un ancho de cama de siembra de {ancho_cama_siembra} metros y una distancia entre plantas de {distancia_entre_plantas} metros")
            break
        except ValueError:
            return "Se esperan solomente numeros positivos. Intente otra vez"
        

@app.route('/fertilizante_por_arbol/', methods = ['GET', 'POST'])
def fertilizante_por_arbol():
    while True:
        try :
            fert_ha = float(request.form.get('fertilizante', True))
            arb_ha = int(request.form.get('arboles', True))
            fert_arbol = round(fert_ha / arb_ha, 2)
            return render_template('tresbolillo.html', salida_fert_arbol = f"La cantidad de fertilizante a aplicar por arbol es de {fert_arbol} kg")
            break
        except ValueError:
            return "Se esperan solamente numeros positivos. Intente otra vez"
        

@app.route('/eficiencia/', methods = ['GET', 'POST'])
def eficiencia(valor_max = 0):
    #while True:
        try:
            valor_max = float(request.form.get('maxima', True))
            valor_min = float(request.form.get('minima', True))
            eficiencia = round((valor_min * 100) / valor_max, 2)
            if eficiencia >= 95:
                return render_template('eficiencia.html', salida_eficiencia = f"La eficiencia es del {eficiencia} %. ¡¡CALIBRACION LISTA. ES UN BUEN MOMENTO PARA TRABAJAR!!")
            if eficiencia <= 94.9:
                return render_template('eficiencia.html', salida_eficiencia = f"La eficiencia es del {eficiencia} % ¡¡FALTA UN POCO MAS PARA PODER TRABAJAR, LA CALIBRACION TODAVIA NO ESTA LISTA!!")
            #break
        except ValueError:
            return "Se esperan solamente numeros positivos. Intente otra vez"


@app.route('/acerca/')
def acerca1():
    return render_template('acerca_de.html')


if __name__ == '__main__':
    app.run(debug = True)