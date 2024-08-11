import requests
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from time import sleep
import pandas as pd
import os
from src import config
from src.config import URL, ENDPOINT_PORTFOLIO, ENDPOINT_OPERATIONS, ENDPOINT_MARKET, ENDPOINT_TOKENS


class IOLClient():
    def __init__(self):
        self.username = config.IOL_USERNAME
        self.password = config.IOL_PASSWORD
        print("self.username", self.username)
        self.tokens = self.get_tokens("", self.username, self.password)
        self.access_token = self.tokens["access_token"]

    def get_tokens(self, refresh_token, username, password, refresh=False):
        print(username, password)
        if not refresh:
            payload = {
                'username':username,
                'password':password,
                'grant_type':'password'
            }
            print("Not refresh")
        else:
            payload = {
                'refresh_token':refresh_token,
                'grant_type':'refresh_token'
            }
            print("Refreshing")
        r = requests.post(URL+ENDPOINT_TOKENS, data=payload)
        if r.status_code == 200:
            print("Valid response")
            r = r.json()
            tokens = {
                'access_token':r['access_token'],
                'refresh_token':r['refresh_token']
            }
            return tokens
        else:
            print('Failed. Status code:', r.status_code)

    def get_portfolio(self, bearer_token):
        payload = {
            'Authorization':'Bearer ' + bearer_token,
            'Accept': 'application/json'
        }
        r = requests.get(URL+ENDPOINT_PORTFOLIO, headers=payload)
        if r.status_code == 200:
            r = r.json()
            return r
        else:
            print('Failed. Status code:', r.status_code)

    def get_operations(self, bearer_token, date_from, date_to):
        payload = {
            'Authorization':'Bearer ' + bearer_token,
            'Accept': 'application/json'
        }
        date_from_path = f'?filtro.fechaDesde={date_from}'
        date_to_path = f'&filtro.fechaHasta={date_to}'
        request_url = URL + ENDPOINT_OPERATIONS + date_from_path + date_to_path
        r = requests.get(request_url, headers=payload)
        if r.status_code == 200:
            r = r.json()
            return r
        else:
            print('Failed. Status code:', r.status_code)

    def get_current_market_value(self, bearer_token, ticker):
        payload = {
            'Authorization':'Bearer ' + bearer_token,
            'Accept': 'application/json'
        }
        request_url = URL + ENDPOINT_MARKET.format(ticker)
        r = requests.get(request_url, headers=payload)
        if r.status_code == 200:
            r = r.json()
            return r['ultimoPrecio']
        else:
            print('Failed. Status code:', r.status_code)

    def create_operations_dataframe(self, start_date, end_date, output_df_path):

        if type(start_date) == str:
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        if type(end_date) == str:
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        list_operations = []
        while start_date < end_date:
            operations = self.get_operations(
                self.access_token,
                start_date.strftime("%Y-%m-%d"),
                (start_date + relativedelta(months=1)).strftime("%Y-%m-%d")
            )
            list_operations += operations
            start_date = start_date + relativedelta(months=1)
            sleep(0.25)

        df_operations = pd.DataFrame(list_operations)
        df_operations.to_csv(output_df_path, index=False)
