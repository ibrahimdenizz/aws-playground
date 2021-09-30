import json

def lambda_handler(event, context):
    # 1. Parse out query string parameters
    transaction_id = event['queryStringParameters']['transactionId']
    transaction_type = event['queryStringParameters']['type']
    transaction_amount = event['queryStringParameters']['amount']

    print(f"Transaction ID: {transaction_id}")
    print(f"Transaction Type: {transaction_type}")
    print(f"Transaction Amount: {transaction_amount}")

    # 2. Construct the body of the response object
    transaction_response = {}
    transaction_response['transactionId'] = transaction_id
    transaction_response['type'] = transaction_type
    transaction_response['amount'] = transaction_amount
    transaction_response["message"] = "Transaction processed successfully"

    # 3. Construct the response object
    response = {}
    response['statusCode'] = 200
    response['headers'] = {}
    response['headers']['Content-Type'] = 'application/json'
    response['body'] = json.dumps(transaction_response)

    #4. Return the response object
    return response