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