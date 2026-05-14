from fastapi import APIRouter, HTTPException
import service
from models import Customer, CustomerUpdate, AccountUpdate

router = APIRouter()

@router.get("/api/customers")
def getallcustoemrs():
    return service.getAllCustomers()

@router.get("/api/customers/{customerId}")
def getCustomerById(customerId: int):
    customer = service.getCustomerByID(customerId)

    if customer is None:
        raise HTTPException(status_code=404, detail="Customer Not Found")
    
    return customer

@router.get("/api/accounts")
def getAllAccounts():
    return service.getAllAccounts()

@router.get("/api/customers/{customerId}/accounts")
def getAccountsByCustomerId(customerId: int):
    accounts = service.getAccountsByCustomerId(customerId)

    if accounts is None:
        raise HTTPException(status_code=404, detail="Customer Not Found")
    
    return accounts
@router.get("/api/accounts/premium")
def getPremiumAccounts():
    return service.getPremiumAccount()

@router.post("/api/customers")
def addCustomer(customer: Customer):
    return service.addCustomer(customer)

@router.delete("/api/customers/{customer_id}")
def deleteCustomer(customerId: int):
    deleted = service.delete_customer(customerId)

    if not deleted:
        raise HTTPException(status_code=404, detail="Customer not found")

    return {"message": "Customer deleted successfully"}
    
@router.put("/api/customers/{customer_id}")
def update_customer(customerId: int, customerUpdate: CustomerUpdate):
    updated = service.update_customer(customerId, customerUpdate)

    if not updated:
        raise HTTPException(status_code=404, detail="Customer not found or no changes made")

    return {"message": "Customer updated successfully"}


@router.delete("/api/customers/{customer_id}/accounts/{account_id}")
def delete_account(customerId: int, accountId: int):
    deleted = service.delete_account(customerId, accountId)

    if not deleted:
        raise HTTPException(status_code=404, detail="Customer or account not found")

    return {"message": "Account deleted successfully"}


@router.put("/api/customers/{customer_id}/accounts/{account_id}")
def update_account(customerId: int, accountId: int, accountUpdate: AccountUpdate):
    updated = service.update_account(customerId, accountId, accountUpdate)

    if not updated:
        raise HTTPException(status_code=404, detail="Customer or account not found, or no changes made")

    return {"message": "Account updated successfully"} 