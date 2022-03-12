import pytest
# To test SMPT connection
import smtplib

@pytest.fixture
def important_value():
   important = True
   return important

# Modularization
@pytest.fixture
def me():
    return "me"

@pytest.fixture
def together(me):
    return "you and " + me

# Two fixtures requested

@pytest.fixture
def happy():
    return " are happy."

@pytest.fixture
def complete(together, happy):
    return together + happy   

# Auotouse

@pytest.fixture(autouse=True)
def meaning_of_life():
    return 42   

# To test SMPT connection

@pytest.fixture(scope = "module")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout  =5)