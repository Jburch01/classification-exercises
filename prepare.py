from acquire import *
from sklearn.model_selection import train_test_split

def prep_iris():
    # Get the iris data into pandas dataframe
    df = get_iris_data()
    # Drop the species_id and measurement_id columns.
    df = df.drop(["species_id", 'measurement_id'], axis=1)
    # Rename species column
    df = df.rename(columns={"species_name": "species"})
    # Encode the species column
    df = pd.concat(
        [df,
         pd.get_dummies(df['species'], drop_first=True)],
        axis=1)
    return df


def prep_titanic():
    # Get titanic db
    titanic_db = get_titanic_data()
    # fill the NA age with mean age
    titanic_db['age'] = titanic_db['age'].fillna(titanic_db.age.mean())
    # remove columns that are unnecessary
    titanic_db.drop(['class', 'embarked', 'deck'], axis=1, inplace=True)
    titanic_db = pd.concat(
        [titanic_db,
         pd.get_dummies(titanic_db[['sex', 'embark_town']], drop_first=True)],
        axis=1)
    return titanic_db


def prep_telco():
    # Get telco db
    telco_db = get_telco_data()
    # change dtype of total charges
    telco_db['total_charges'] = (telco_db['total_charges']) + '0'
    telco_db['total_charges'] = telco_db['total_charges'].astype(float)
    # drop columns
    telco_db.drop(['payment_type_id', 'internet_service_type_id', 'contract_type_id'], axis=1, inplace=True)
    telco_db = pd.concat(
        [telco_db,
         pd.get_dummies((telco_db.select_dtypes(include='object').drop(columns='customer_id')), drop_first=True)],
        axis=1)
    return telco_db


def train_test_validate(df, target):
    train_val, test = train_test_split(df,
                                       train_size=0.8,
                                       random_state=706,
                                       stratify=df[target])
    train, validate = train_test_split(train_val,
                                       train_size=0.7,
                                       random_state=706,
                                       stratify=train_val[target])
    return train, validate, test






