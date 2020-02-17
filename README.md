# Cashfree Payout Integration Kit for Python

Below is an integration flow on how to use Cashfree's payouts sdk.
Please go through the payout docs [here](https://dev.cashfree.com/payouts)
<br/>
This kit is linked to the standard transfer flow. Go [here](https://dev.cashfree.com/payouts/integrations/standard-transfer) to get a better understanding.
<br/>

## Functionalities

The following kit contains the following functionalities:
    <ol>
    <li> init: to initialize the sdk.
    <li> Benefeciary.get_bene_details: to get beneficiary details/check if a beneficiary exists.
    <li> Benefeciary.add: to create beneficiaries.
    <li> Transfers.request_transf: to create a payout transfer.
    <li> getTransferStatus: to get payout transfer status.
    </ol>
<br/>
You can get more information on the python sdk [here](https://github.com/cashfree/cashfree-sdk-python).

## Build Steps

follow the following build steps to compile the Integration kit:
  1. Download the code and cd into the directory containing the code.
  2. install the following dependency: Cashfree's python sdk
  ```
  pip3 install git+https://github.com/cashfree/cashfree-sdk-python.git
  ```
  
## Set Up

### Pre Requisites:
The following kit uses information stored in a app.py file. Before running the code for the first time open the app.py file
and add the relevant details:
  1. ClientId: This is a unique Identifier that identifies the merchant. For more information please go [here](https://dev.cashfree.com/payouts/integrations/pre-requisites#credentials).
  2. ClientSecret: Corresponding secret key for the given ClientId that helps Cashfree indentify the merchant. For more information please go [here](https://dev.cashfree.com/payouts/integrations/pre-requisites#credentials).
  3. Environment: Environment to be hit. The following values are accepted prod: for production, test: for test environment. Pass this parameter to the init function

### IP Whitelisting:

Your IP has to be whitelisted to hit Cashfree's server. For more information please go [here](https://dev.cashfree.com/payouts/integrations/pre-requisites#ip).

### Beneficiary:
The following kit needs beneficiary details in order to create a beneficiary and fetch its details. For more information on Beneficiaries please go [here](https://dev.cashfree.com/payouts/integrations/standard-transfer#beneficiary)

The kit reads beneficiary details from the app.py file. Under the bene object. For a list of required fields go [here](https://dev.cashfree.com/api-reference/payouts-api#create-beneficiary).
Sample Fields to add a beneficiary using bankAccount and ifsc:
  1. beneId: uniqueId of the created beneficiary.
  2. name: beneficiary name.
  3. email: beneficiary email.
  4. phone: beneficiary phone.
  5. bankAccount: beneficiary's bank account.
  6. ifsc: corresponding ifsc.
  7. address1: beneficiary address.
  8. city: beneficiary city.
  9. state: beneficiary state.
  10. pincode: beneficiary pincode.
  
### transferDetails:
To request a payout transfer certain information is needed. To get a better understanding on requesting a transfer go [here](https://dev.cashfree.com/api-reference/payouts-api#transfers).
the request transfer object is read from the app.py file under the transfer object.

Required Fields are:
  1. beneId: beneficiaryId to whom the transfer must be made to.
  2. amount: amount to be transferred.
  3. trasnferId: unique transfer id to identify the transfer.


## Usage

Once the app.py file is setup you can run the executable, to run the entire flow. Authorise, check and add beneficiary, 
request for a payout transfer and get the transfer status.

run the following command in the terminal to run the script:
```
  python app.py
```

You can change the necessary values in the app.py file as per your requirements and re run the script whenever needed.

## Doubts

Reach out to techsupport@cashfree.com in case of doubts.
 


