from flask import Flask, request

from regresionLogistica import prediccion

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET","POST"])
def home():
    errors = ""
    if request.method == "POST":
        edad = None
        sexo = None
        cuidado_intensivo = None
        asistencia_respiratoria = None
        try:
            edad = float(request.form["edad"])
        except:
            errors += "<p>{!r} no es una edad valida.</p>\n".format(request.form["edad"])
        try:
            sexo = float(request.form["sexo"])
        except:
            errors += "<p>{!r} no es una opción valida.</p>\n".format(request.form["sexo"])
        try:
            cuidado_intensivo = float(request.form["cuidado_intensivo"])
        except:
            errors += "<p>{!r} no es una opción valida.</p>\n".format(request.form["cuidado_intensivo"])
        try:
            asistencia_respiratoria = float(request.form["asistencia_respiratoria"])
        except:
            errors += "<p>{!r} no es una opción valida.</p>\n".format(request.form["asistencia_respiratoria"])
        if edad is not None and sexo is not None and cuidado_intensivo is not None and asistencia_respiratoria is not None:
            resultado = prediccion(edad, sexo, cuidado_intensivo, asistencia_respiratoria)
            resultado_formateado = "{:,.2f}%".format(resultado)
            return '''
                <html>
                    <body>
                        <h1>Resultado de la predicción:</h1>
                        <p>Tiene un {resultado} de chances de fallecimiento.</p>
                        <p><a href="/">Click acá para volver al inicio</a>
                    </body>
                </html>
            '''.format(resultado=resultado_formateado)
    return '''
    <!DOCTYPE html>
    <html>
        <body>
            {errors}
            <form method="post" action=".">
                Edad: <input type="text" name="edad"><br>
                Sexo: <select name="sexo">
                    <option value=0>Hombre</option>
                    <option value=1>Mujer</option>
                </select> <br>
                Cuidado intensivo: <select name="cuidado_intensivo">
                    <option value=0>No</option>
                    <option value=1>Si</option>
                </select> <br>
                Asistencia respiratoria: <select name="asistencia_respiratoria">
                    <option value=0>No</option>
                    <option value=1>Si</option>
                </select> <br>
                <input type="submit" value="Predecir" />
            </form>
        </body>
    </html>
    '''.format(errors=errors)
