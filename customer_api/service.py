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
    return repo.addCustomer(customer)

def addAccount(customerId: int, accountCreate):
    return repo.addAccount(customerId, accountCreate)

def deleteCustomer(customerId: int):
    return repo.deleteCustomer(customerId)


def updateCustomer(customerId: int, customerUpdate):
    return repo.updateCustomer(customerId, customerUpdate)


def deleteAccount(customerId: int, accountId: int):
    return repo.deleteAccount(customerId, accountId)


def updateAccount(customerId: int, accountId: int, accountUpdate):
    return repo.updateAccount(customerId, accountId, accountUpdate)

def registerUser(user):
    return repo.registerUser(user)

def loginUser(username: str):
    return repo.loginUser(username)

def getCustomerByUsername(username: str):
    return repo.getCustomerByUsername(username)