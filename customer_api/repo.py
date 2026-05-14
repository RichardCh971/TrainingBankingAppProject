from database import customer_collection

def getAllCustomers():
    customers = []

    for customer in customer_collection.find():
        customer["_id"] = str(customer["_id"])

        customers.append(customer)
    return customers

def getCustomerByID(customerId: int):
    customer = customer_collection.find_one({"id": customerId})

    if customer is None:
        return None
    
    customer["_id"] = str(customer["_id"])

    return customer


def getAllAccounts():
    allAccounts = []

    for customer in customer_collection.find():
        for account in customer["accounts"]:
            allAccounts.append(account)

    return allAccounts


def getAccountsByCustomerId(customerId: int):
    
    customer = customer_collection.find_one({"id": customerId})

    if customer is None:
        return None
    
    return customer["accounts"]

def getPremiumAccounts():

    premiumAccounts = []

    for customer in customer_collection.find():
        for account in customer["accounts"]:
            if account["balance"] > 10000:
                premiumAccounts.append(account)

    return premiumAccounts

def addCustomer(customer):
    customer_dict = customer.model_dump()
    customer_collection.insert_one(customer_dict)
    return customer_dict

def deleteCustomer(customerId: int):
    result = customer_collection.delete_one({"id", customerId})
    return result.deleted_count > 0
    
def deleteAccount(customerId: int, accountId: int):
    result = customer_collection.update_one(
        {"id": customerId},
        {"$pull": {"accounts": {"id":accountId}}})

def updateCustomer(customerId: int, customerUpdate):
    result = customer_collection.update_one(
        {"id": customerId},
        {"$set": {"name": customerUpdate.name}}
    )

    return result.modified_count > 0
    

def updateAccount(customerId: int,accountId: int, accountUpdate):
    result = customer_collection.update_one(
        {
            "id": customerId,
            "accounts.id": accountId
        },
        {
            "$set": {
                "accounts.$.type": accountUpdate.type,
                "accounts.$.balance": accountUpdate.balance
            }
        }
    )

    return result.modified_count > 0




