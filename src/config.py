import os
from dotenv import load_dotenv

load_dotenv()

URL = 'https://api.invertironline.com'
ENDPOINT_TOKENS = '/token'
ENDPOINT_PORTFOLIO = '/api/v2/estadocuenta'
ENDPOINT_OPERATIONS = '/api/v2/operaciones'
ENDPOINT_MARKET = '/api/v2/bCBA/Titulos/{}/CotizacionDetalle'
IOL_USERNAME = os.getenv("IOL_USERNAME")
IOL_PASSWORD = os.getenv("IOL_PASSWORD")
GET_OPERATIONS_START_DATE = "2020-01-01"
GET_OPERATIONS_END_DATE = "2024-08-01"
OPERATIONS_CSV_PATH = "data/transactions.csv"
