import pytest
from utilities import ExcelFiles


# parametrize is using to pass 2 values which mentioned from excell files mentioned in utilities.
@pytest.mark.parametrize("email_address, password",
                         ExcelFiles.get_data_from_excell('ExcelFiles/loginfile.xlsx', 'LoginPage'))
def test_email_password(email_address, password):
    print(f"My email is: {email_address} and password is: {str(password)}")
