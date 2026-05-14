import repo

def getAllCustomers():
    return repo.getAllCustomers()

def getCustomerByID(customerId: int):
    return repo.getCustomerByID(customerId)

def getAllAccounts():
    return repo.getAllAccounts()

def getAccountsByCustomerId(customerId: int):
    return repo.getAccountsByCustomerId(customerId)

def getPremiumAccount():
    return repo.getPremiumAccounts()

def addCustomer(customer):
    repo.addCustomer(customer)

def deleteCustomer(customerId: int):
    return repo.delete_customer(customerId)


def updateCustomer(customerId: int, customerUpdate):
    return repo.update_customer(customerId, customerUpdate)


def deleteAccount(customerId: int, accountId: int):
    return repo.delete_account(customerId, accountId)


def updateAccount(customerId: int, accountId: int, accountUpdate):
    return repo.update_account(customerId, accountId, accountUpdate)