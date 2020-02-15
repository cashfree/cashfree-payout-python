from cashfree_sdk.payouts import Payouts
from cashfree_sdk.payouts.beneficiary import Beneficiary
from cashfree_sdk.payouts.transfers import Transfers

clientId = "clientId"
clientSecret = "clientSecret"

beneId =  "JOHN1801290915"
transferId = "tranfer001232347"

bene = {
    "beneId": beneId, 
    "name": "john doe",
    "email": "johndoe@cashfree.com", 
    "phone": "9876543213",
    "bankAccount": "00011020001772",
    "ifsc": "HDFC0000001",  
    "address1" : "ABC Street", 
    "city": "Bangalore", 
    "state":"Karnataka", 
    "pincode": "560001"
}

transfer = {
    "beneId": beneId,
    "transferId": transferId,
    "amount": "1.00",
}


try:
    Payouts.init(clientId, clientSecret, "TEST")
    bene_add_response = Beneficiary.add(**bene)
    print("beneficiary addition response")
    print(bene_add_response.content)

    bene_details_response = Beneficiary.get_bene_details(bene["beneId"])
    print("get beneficary details")
    print(bene_details_response.content)

    request_transfer_response = Transfers.request_transfer(**transfer)
    print("request transfer response")
    print(request_transfer_response.content)

    get_transfer_status_response =  Transfers.get_transfer_status(**{"transferId": transferId})
    print("get transfer status response")
    print(get_transfer_status_response.content)

except Exception as err: 
    print("err occurred")
    print(err)