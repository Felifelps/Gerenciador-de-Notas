"""Contém funções para carregamento e modificação do arquivo csv."""

from constants import ATTRS, CSV_FILE


def save_data(data):
    """Converte uma lista de tarefas em csv e salva em arquivo externo."""
    result = [",".join(ATTRS)]
    for task in data:
        line = [task[attr] for attr in ATTRS]
        result.append(",".join(line).replace("\n", "\\n"))

    with open(CSV_FILE, 'w', encoding='utf-8') as file:
        file.write("\n".join(result))


def load_data():
    """
    Carrega os dados do arquivo csv e os converte para uma lista de dicionários.\n
    Cria o arquivo caso ele não exista.
    """
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as file:
            lines = file.read().split('\n')

        headers = lines.pop(0).split(',')
        data = []
        for line in lines:
            try:
                values = line.replace("\\n", "\n").split(',')
                data.append({headers[i]: values[i] for i in range(len(headers))})
            except Exception as e:
                pass
        return data

    except FileNotFoundError:
        save_data([])
        return []
