'''
Below is an integration flow on how to use Cashfree's payouts.
Please go through the payout docs here: https://docs.cashfree.com/docs/payout/guide/

The following script contains the following functionalities :
    1.getToken() -> to get auth token to be used in all following calls.
    2.getBeneficiary() -> to get beneficiary details/check if a beneficiary exists
    3.createBeneficiaryEntity() -> to create beneficiaries
    4.requestTransfer() -> to create a payout transfer
    5.getTransferStatus() -> to get payout transfer status.


All the data used by the script can be found in the config.ini file. This includes the clientId, clientSecret, Beneficiary object, Transaction Object.
You can change keep changing the values in the config file and running the script.
Please enter your clientId and clientSecret, along with the appropriate enviornment, beneficiary details and request details
'''

#warning the following code is written for python2 and tested using python2.7
#warning the following code has a dependency on the request, configparser library

import configparser
import requests
import json

#read the config file
config = configparser.ConfigParser()
config.optionxform = str
if config.read('config.ini') == []:
    print 'unable to read config'
    exit()

#default
default = config._sections['default']
clientId, clientSecret, env = default['clientId'], default['clientSecret'], default['env']
baseurl = config._sections['baseUrl'][env]
url = config._sections['url']

#get auth token
def getToken():
    try:
        finalUrl = baseurl + url['auth']
        r =  requests.post(finalUrl, headers={ "X-Client-Id":clientId, "X-Client-Secret":clientSecret})

        if (not r):
            raise Exception("response err: response is null")

        content = json.loads(r.content)


        if (content['status'] != "SUCCESS") or (content['subCode'] != "200"):
            raise Exception("response err: response is incorrect \n" + content["message"])
        return content["data"]["token"]
    except Exception as err:
        print 'err in getting token'
        raise Exception(err)

#get beneficiary details
def getBeneficiary(token):
    try:
        beneId = config._sections['beneficiary']['beneId']
        finalUrl = baseurl + url['getBene'] + beneId
        r = requests.get(finalUrl, headers={"X-Client-Id":clientId, "X-Client-Secret":clientSecret, 'Content-Type': 'application/json','Authorization': 'Bearer ' + token})
        
        if (not r):
            raise Exception("response err: response is null")
        content = json.loads(r.content)

        if (content['status'] != "SUCCESS") or (content['subCode'] != "200"):
            return False
        return True
    except Exception as err:
        print 'err in getting beneficiary'
        raise Exception(err)

#create beneficiary
def createBeneficiary(token):
    try:
        finalUrl = baseurl + url['addBene']
        bene = json.loads(json.dumps(config._sections['beneficiary']))
        #bene = config._sections['beneficiary']
        r = requests.post(finalUrl, json=bene, headers={"X-Client-Id":clientId, "X-Client-Secret":clientSecret, 'Content-Type': 'application/json','Authorization': 'Bearer ' + token})
        content = json.loads(r.content)

        if (content['status'] != "SUCCESS") or (content['subCode'] != "200"):
            raise Exception("response err: response is incorrect \n" + content["message"])
    except Exception as err:
        print 'err in creating beneficary'
        raise Exception(err)

#request transfer
def requestTransfer(token):
    try:
        finalUrl = baseurl + url['requestTransfer']
        trasfer = json.loads(json.dumps(config._sections['transferDetails']))

        r = requests.post(finalUrl, json=trasfer, headers={"X-Client-Id":clientId, "X-Client-Secret":clientSecret, 'Content-Type': 'application/json','Authorization': 'Bearer ' + token})
        content = json.loads(r.content)
        
        if (content['status'] != "SUCCESS") or (content['subCode'] != "200"):
            raise Exception("response err: response is incorrect \n" + content["message"])
        print 'transfer successfully created'
    except Exception as err:
        print 'err in requesting transfer'
        raise Exception(err)

#get transfer status
def getTransferStatus(token):
    try:
        transferId = config._sections['transferDetails']['transferId']
        finalUrl = baseurl + url['getTransferStatus'] + transferId

        r = requests.get(finalUrl, headers={"X-Client-Id":clientId, "X-Client-Secret":clientSecret, 'Content-Type': 'application/json','Authorization': 'Bearer ' + token})
        content = json.loads(r.content)
        
        if (content['status'] != "SUCCESS") or (content['subCode'] != "200"):
            raise Exception("response err: response is incorrect \n" + content["message"])
        
        print('transfer details')
        print json.dumps(content)
    except Exception as err:
        print 'err in getting transfer status'
        raise Exception(err)


#main function
if __name__ =="__main__":
    token = getToken()
    if (not getBeneficiary(token)):
        createBeneficiary(token)
    requestTransfer(token)
    getTransferStatus(token)
