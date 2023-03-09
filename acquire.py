from env import get_db_url
import pandas as pd

def get_titanic_data():
    try:
        csv_info = pd.read_csv('titanic_db.csv')
        return csv_info
    except FileNotFoundError:
        url = get_db_url("titanic_db")
        info = pd.read_sql("select * from passengers", url)
        return info


def get_iris_data():
    try:
        csv_info = pd.read_csv('iris_db.scv')
        return csv_info
    except FileNotFoundError:
        url = get_db_url('iris_db')
        info = pd.read_sql('''select * from species
        right join measurements using (species_id)''', url)
        return info


def get_telco_data():
    try:
        csv_info = pd.read_csv('telco_churn.csv')
        return csv_info
    except FileNotFoundError:
        url = get_db_url('telco_churn')
        info = pd.read_sql('''
            select * from customers
        join contract_types using(contract_type_id)
        join internet_service_types using(internet_service_type_id)
        join payment_types using (payment_type_id);
        ''', url)
        return info

