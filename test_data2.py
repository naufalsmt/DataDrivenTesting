import pytest


def get_data():
    return [
        ["test@mail.com", "1234"],
        ["good@mail.com", "9090"],
        ["mark@mail.com", "55555"]
    ]


@pytest.mark.parametrize("email_address, password", get_data())
def test_email_password(email_address, password):
    print("My email is: "+email_address+" and password is: "+password)
