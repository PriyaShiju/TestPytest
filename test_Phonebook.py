import pytest
from PhoneBook import PhoneBook
# python -m pytest  or py.test
# pytest --fixtures
# instead of setUp we use decorator foe pytest fixture and pass it as parameter in other functions


@pytest.fixture  
def phonebook(tmpdir):   
    """Provides empty PhoneBook"""
    return PhoneBook(tmpdir)
    #yield phonebook
    #phonebook.clear()


def test_phonebook_lookupnames(phonebook):    
    phonebook.add("Bob","123456")
    assert "123456" == phonebook.lookup("Bob")
    
def test_phonebook_containnames(phonebook):    
    phonebook.add("Bob","123456")
    assert "Bob" in phonebook.names()
    
def test_missingname_raiseerror(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
        
    