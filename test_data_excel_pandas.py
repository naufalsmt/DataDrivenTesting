import pytest
import pandas as pd


def get_data():
    df = pd.read_excel('ExcelFiles/loginfile.xlsx')
    data = df[['Email', 'Password']].values.tolist()
    return data



@pytest.mark.parametrize("email_address, password", get_data())
def test_email_password(email_address, password):
    print(f"My email is: {email_address} and password is: {str(password)}")
