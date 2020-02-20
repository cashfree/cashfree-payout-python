'''
Below is an integration flow on how to use Cashfree's payouts SDK. The SDK can be found at: https://github.com/cashfree/cashfree-sdk-python
Please go through the payout docs here: https://dev.cashfree.com/payouts
The following script contains the following functionalities :
    1. Beneficiary.get_bene_details -> get details of a beneficiary
    2. Beneficiary.add -> add a beneficiary
    3. Transfers.request_transfer -> request a transfer
    4. Transfers.get_transfer_status -> get the status of a requested transfer
'''

import json

from cashfree_sdk.payouts import Payouts
from cashfree_sdk.payouts.beneficiary import Beneficiary
from cashfree_sdk.payouts.transfers import Transfers

clientId = "clientId"
clientSecret = "clientSecret"
env = "TEST"

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
    Payouts.init(clientId, clientSecret, env)

    bene_details_response = Beneficiary.get_bene_details(bene["beneId"])
    bene_details_response_content = json.loads(bene_details_response.content)
    print("get beneficiary details")
    print(bene_details_response_content)

    if(bene_details_response_content['status'] == 'ERROR' and bene_details_response_content['subCode'] == '404':
        bene_add_response = Beneficiary.add(beneId=bene['beneId'], name=bene['name'], email=bene['email'], phone=bene['phone'], bankAccount=bene['bankAccount'], ifsc=bene['ifsc'], address1=bene['address1'], city=bene['city'], state=bene['state'], pincode=bene['pincode'])
        print("beneficiary addition response")
        print(bene_add_response.content)


    request_transfer_response = Transfers.request_transfer(beneId=transfer['beneId'], transferId=transfer['transferId'], amount=transfer['amount'])
    print("request transfer response")
    print(request_transfer_response.content)

    get_transfer_status_response =  Transfers.get_transfer_status(transferId=transferId)
    print("get transfer status response")
    print(get_transfer_status_response.content)

except Exception as err: 
    print("err occurred")
    print(err)
