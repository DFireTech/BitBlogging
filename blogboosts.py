#Open the DB Floodgates
import sqlite3
import json
from btcpay import BTCPayClient

connection = sqlite3.connect("boosts.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS payments (
    id INTEGER PRIMARY KEY,
    sats_amount INTEGER,
    user_comment TEXT
)''')
connection.commit()

try:
    #Get Sats Amount
    sats_input = input("How many sats would you like to send: ")
    if not sats_input.isdigit():
        raise ValueError("Nice try!")
    
    sats_amount = int(sats_input)

    #Get comment
    user_comment = input("Leave a comment: ")
    if not user_comment:
        raise ValueError("Gotta send sats and a message!")

    #Confirm stuff
    confirm_send = input("Send ", sats_amount, " satoshis with ", user_comment, " ? y/n").lower()


    if confirm_send != "y":
        print("Op aborted")
    else:
        #JSON Dictionary
        payment_data = {
            "sats_amount": sats_amount,
            "user_comment": user_comment
        }

        #Convert payment to JSON
        payment_json = json.dumps(payment_data)

        #Init BTCPay
        btcpay_url = "boost.goldenblogathon.com"
        api_key = "359d5e5d42f7116750698d3f780a1a7bdf7752ce"
        client = BTCPayClient(btcpay_url, api_key)

        #Invoicing
        invoice_data = {
            "price": sats_amount,
            "currency": SATS,
            "orderId": BoostOnEm,
            "itemDesc": user_comment
        }
        invoice = client.create_invoice(invoice_data)

        print("Invoice created. Send ", invoice['cryptoInfo'][0]['cryptoPaid'], " sats to ", invoice['cryptoInfo'][0]['paymentUrls']['BIP21'])

        #Needs to have an invoiceSettled deal...

        #store that beautiful bean footage
        cursor.execute("INSERT INTO payments (sats_amount, user_comment) VALUES (?,?)", (sats_amount, user_comment))
        connection.commit()
        print("Comment saved.")
    
except KeyboardInterrupt:
    print("\nProcess Interrupted.")
    
finally:
    #close up shop
    connection.close()