from fastapi import APIRouter, HTTPException
import service
from models import Customer, CustomerUpdate, AccountUpdate, AccountCreate
from user import UserRegister, UserLogin

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
def deleteCustomer(customer_id: int):
    deleted = service.deleteCustomer(customer_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Customer not found")

    return {"message": "Customer deleted successfully"}

@router.put("/api/customers/{customer_id}")
def update_customer(customer_id: int, customerUpdate: CustomerUpdate):
    updated = service.updateCustomer(customer_id, customerUpdate)

    if not updated:
        raise HTTPException(status_code=404, detail="Customer not found")

    return {"message": "Customer updated successfully"}
@router.delete("/api/customers/{customer_id}/accounts/{account_id}")
def delete_account(customer_id: int, account_id: int):
    deleted = service.deleteAccount(customer_id, account_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Customer or account not found")

    return {"message": "Account deleted successfully"}


@router.put("/api/customers/{customer_id}/accounts/{account_id}")
def update_account(customer_id: int, account_id: int, accountUpdate: AccountUpdate):
    updated = service.updateAccount(customer_id, account_id, accountUpdate)

    if not updated:
        raise HTTPException(status_code=404, detail="Customer or account not found")

    return {"message": "Account updated successfully"} 


@router.post("/api/register")
def register_user(user: UserRegister):
    try:
        registered_user = service.registerUser(user)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

    new_customer = Customer(
        id=0,
        username=user.username,
        name=user.username,
        accounts=[]
    )

    service.addCustomer(new_customer)

    return registered_user


@router.post("/api/login")
def login_user(user: UserLogin):

    found_user = service.loginUser(user.username)

    if found_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    if found_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid password")

    return {
        "message": "Login successful",
        "username": found_user["username"]
    }

@router.get("/api/customers/username/{username}")
def get_customer_by_username(username: str):

    customer = service.getCustomerByUsername(username)

    if customer is None:
        raise HTTPException(status_code=404, detail="Customer Not Found")
    return customer

@router.post("/api/customers/{customer_id}/accounts")
def add_account(customer_id: int, accountCreate: AccountCreate):
    account = service.addAccount(customer_id,accountCreate)

    if account is None:
        raise HTTPException(status_code=404, detail="Customer Not Found")
    
    return account