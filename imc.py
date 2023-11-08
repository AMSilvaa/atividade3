import PySimpleGUI as sg

# Função para calcular o IMC e classificá-lo
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return round(imc, 2), classificar_imc(imc)

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    else:
        return "Acima do peso"

layout = [
    [sg.Text('Nome do Paciente'), sg.Input(key='nome')],
    [sg.Text('Endereço Completo'), sg.Input(key='endereco')],
    [sg.Text('Altura (cm)'), sg.Input(key='altura')],
    [sg.Text('Peso (Kg)'), sg.Input(key='peso')],
    [sg.Button('Calcular'), sg.Button('Reiniciar'), sg.Button('Sair')],
]

result_layout = [
    [sg.Text('Resultado')],
    [sg.Text('Nome:', size=(40, 1), key='resultado_nome')],
    [sg.Text('Endereço:', size=(60, 1), key='resultado_endereco')],
    [sg.Text('IMC:', size=(15, 1), key='resultado_imc', font=('Any', 14, 'bold'))],
    [sg.Text('Classificação:', size=(40, 1), key='classificacao_imc')],
]

window = sg.Window('Calculadora de IMC', layout)
result_window = None

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    if event == 'Calcular':
        try:
            nome = values['nome']
            endereco = values['endereco']
            altura = float(values['altura'])
            peso = float(values['peso'])
            imc, classificacao = calcular_imc(peso, altura / 100)  # Converter altura para metros

            if result_window is not None:
                result_window.close()

            result_window = sg.Window('Resultado do IMC', result_layout, finalize=True)
            result_window['resultado_nome'].update(f'Nome: {nome}')
            result_window['resultado_endereco'].update(f'Endereço: {endereco}')
            result_window['resultado_imc'].update(f'IMC: {imc:.2f}')
            result_window['classificacao_imc'].update(f'Classificação IMC: {classificacao}')
        except ValueError:
            sg.popup_error('Por favor, insira valores válidos para altura e peso.')

    if event == 'Reiniciar':
        window['nome'].update('')
        window['endereco'].update('')
        window['altura'].update('')
        window['peso'].update('')
        if result_window is not None:
            result_window.close()

window.close()
