import requests
import json

def paypal_generate_invoice_id(authorization: str):
    url = "https://api.sandbox.paypal.com/v2/invoicing/generate-next-invoice-number"

    headers = {"Authorization": f"Bearer {authorization}",
               "Content-Type": "application/json"}

    r = requests.post(url, headers=headers)

    return r.json()["invoice_number"]
    
def paypal_create_invoice(email: str, authorization: str):
    url = "https://api.sandbox.paypal.com/v2/invoicing/invoices"

    headers = {"Authorization": f"Bearer {authorization}",
               "Content-Type": "application/json"}

    data = """{
    
          } 
           """

    x = json.loads(data)

    x["detail"]["invoice_number"] = paypal_generate_invoice_id(authorization)
    x["primary_recipients"][0]["billing_info"]["email_address"] = email

    data = json.dumps(x)

    r = requests.post(url, data=data, headers=headers)

    return r.json()["href"]
    
    
def paypal_get_invoice_status(id: str, authorization: str):

    headers = {"Authorization": f"Bearer {authorization}",
               "Content-Type": "application/json"}

    r = requests.get(
        f"https://api.sandbox.paypal.com/v2/invoicing/invoices/{id}", headers=headers)

    return r.json()["status"]
    
    
def paypal_send_invoice(url: str, authorization: str):

    headers = {"Authorization": f"Bearer {authorization}",
               "Content-Type": "application/json"}

    data = """
        {
            "send_to_invoicer": true
        }   
          """

    r = requests.post(url + "/send", data=data, headers=headers)
    return r.json()["href"]
    
    
