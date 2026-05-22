from database import customer_collection, user_collection
from pymongo.errors import DuplicateKeyError

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
    customer_dict["id"] = getNextCustomerId()
    result = customer_collection.insert_one(customer_dict)
    customer_dict["_id"] = str(result.inserted_id)
    return customer_dict

def getNextAccountId():
    highest_id = 0

    for customer in customer_collection.find():
        for account in customer.get("accounts", []):
            if account["id"] > highest_id:
                highest_id = account["id"]

    return highest_id + 1


def addAccount(customerId: int, accountCreate):
    new_account = {
        "id": getNextAccountId(),
        "type": accountCreate.type,
        "balance": accountCreate.balance
    }

    result = customer_collection.update_one(
        {"id": customerId},
        {"$push": {"accounts": new_account}}
    )

    if result.modified_count == 0:
        return None

    return new_account

def deleteCustomer(customerId: int):
    result = customer_collection.delete_one({"id", customerId})
    return result.deleted_count > 0
    
def deleteAccount(customerId: int, accountId: int):
    customer = customer_collection.find_one({"id": customerId})

    if customer is None:
        return False

    result = customer_collection.update_one(
        {"id": customerId},
        {"$pull": {"accounts": {"id": accountId}}}
    )

    return result.modified_count > 0

def updateCustomer(customerId: int, customerUpdate):
    result = customer_collection.update_one(
        {"id": customerId},
        {"$set": {"name": customerUpdate.name}}
    )

    # Consider this successful if the customer exists, even when the name is unchanged.
    return result.matched_count > 0
    

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

    # Treat no-op updates as success when the target account exists.
    return result.matched_count > 0

def registerUser(user):
    user_dict = user.model_dump()
    try:
        user_collection.insert_one(user_dict)
    except DuplicateKeyError:
        raise ValueError(f"Username '{user.username}' is already taken")
    user_dict["_id"] = str(user_dict["_id"])
    return user_dict

def loginUser(username: str):
    user = user_collection.find_one({"username": username})
    if user:
        user["_id"] = str(user["_id"])
    return user

def getNextCustomerId():
    last_customer = customer_collection.find_one(
        sort=[("id", -1)]
    )
    if last_customer is None:
        return 1
    return last_customer["id"] + 1

def getCustomerByUsername(username: str):

    customer = customer_collection.find_one(
        {"username": username}
    )

    if customer:
        customer["_id"] = str(customer["_id"])

    return customer



