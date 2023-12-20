''' Projeto desenvolvido para pratica da biblioteca
 Pycaret, onde é utilizado algoritmo de Machine Learning
 para prever o preço do diamante.
 Autor: Thiago Vilarinho Lemes - Engenheiro de Dados
 Data: 20/12/2023
 Para mais informações sobre a biblioteca acesse: https://pycaret.org/'''

import pandas as pd
from flask import Flask
from flask import render_template
from flask import request
from pycaret.regression import load_model, predict_model

# Carregando o modelo treinado
model = load_model('./diamond-pipeline')

app             = Flask(__name__)

# Features dos dados
carat_Weight    = ''
cut             = ''
color           = ''
clarity         = ''
polish          = ''
symmetry        = ''
report          = ''
price           = 0.0   


@app.route('/ml', methods=['GET', 'POST'])
def hello():

    if request.method == 'POST':
        # Carregando os dados enviados do formulário
        carat_weight    = request.form.get('Carat_Weight')
        cut             = request.form.get('Cut')
        color           = request.form.get('Color')
        clarity         = request.form.get('Clarity')
        polish          = request.form.get('Polish')
        symmetry        = request.form.get('Symmetry')
        report          = request.form.get('Report')

        # Previsão dos dados enviados através formulário
        val = predict(carat_weight, cut, color, clarity, polish, symmetry, report)
        # Rederizando a página com a previsão do 
        return render_template('ml.html', price=val)
    
    return render_template('ml.html', price=price)

# Função para prever o valor do diamante    
def predict(carat_weight, cut, color, clarity, polish, symmetry, report):
    data = pd.DataFrame([[carat_weight, cut, color, clarity, polish, symmetry, report]])
    data.columns = ['Carat Weight', 'Cut', 'Color', 'Clarity', 'Polish', 'Symmetry', 'Report']

    predictions = predict_model(model, data=data) 
    valor = float(predictions["prediction_label"][0])
    return 'Previsão do Valor: $ {:.2f}'.format(valor) 

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
      




