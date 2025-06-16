from flask import Flask, render_template, request
import math
import pandas as pd

app = Flask(__name__)

def angulo_ideal(latitude):
    return abs(latitude) * 0.9 + 3.1  # Fórmula adaptada

def placas_possiveis(area_total, area_placa):
    return math.floor(area_total / area_placa)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    mapa = None

    if request.method == "POST":
        lat = float(request.form["lat"])
        lon = float(request.form["lon"])
        area_disponivel = float(request.form["area_disponivel"])
        tamanho_placa_m2 = float(request.form["tamanho_placa_m2"])
        potencia_placa_w = float(request.form["potencia_placa_w"])

        angulo = angulo_ideal(lat)
        num_placas = placas_possiveis(area_disponivel, tamanho_placa_m2)
        potencia_total_kw = (num_placas * potencia_placa_w) / 1000

        resultado = {
            "angulo": round(angulo, 1),
            "num_placas": num_placas,
            "potencia_total_kw": round(potencia_total_kw, 2),
            "lat": lat,
            "lon": lon
        }

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
