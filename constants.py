"""Guarda constantes usadas nos arquivos"""

ATTRS = {
    'id': 'Id',
    'description': 'Descrição',
    'status': 'Status',
    'deadline': 'Prazo',
}
ATTRS_OPTIONS = {
    'status': ['Pendente', 'Iniciada', 'Concluída', 'Cancelada']
}
CSV_FILE = 'data.csv'
DATE_FORMAT = '%d/%m/%Y'
DATE_FORMAT_LABEL = 'DD/MM/AAAA'
HEADERS = list(ATTRS)
MAX_TABLE_VALUE_LENGTH = 50
