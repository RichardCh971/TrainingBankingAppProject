import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import service
import pytest

def testGetAllCustomers():
    result = service.getAllCustomers()

    # Verify the result is a list
    assert isinstance(result, list)
    
    # Verify the list is not empty
    assert len(result) > 0
    
    # Verify each customer has required fields
    for customer in result:
        assert "id" in customer
        assert "name" in customer
        assert "accounts" in customer

def testGetAllCustomerById():
    result = service.getCustomerByID(1)

    assert result["id"] == 1

def testgetAllAccounts():
    result = service.getAllAccounts()

    assert len(result) > 0
