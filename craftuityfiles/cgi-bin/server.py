#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
import sys
import json
from flask import Flask, redirect, request, jsonify

import stripe

sys.path.insert(0, os.path.dirname(__file__))

# This is your test secret API key.
stripe.api_key = "SECRETKEY"

app = Flask(__name__, static_url_path="", static_folder="../")

YOUR_DOMAIN = "http://craftuity.com"


# createing sessions
@app.route("/", methods=["POST", "GET"])
def create_session():
    description = request.form.get("allitems")
    prices = request.form.get('allPrices')
    itemlist = description.split(',')
    pricelist = prices.split(',')
    print(itemlist)
    print(pricelist)
    finallist = []
    customfield=[{
        "key": "Variation",
        "label": {"type": "custom", "custom": "Color"},
        "type": "text",
        "optional": True,
        },]
        
    if 'Drink Tac Toe' in itemlist or ' Drink Tac Toe' in itemlist:
        customfield=[{
            "key": "Xcolors",
            "label": {"type": "custom", "custom": "X Color"},
            "optional": False,
            "type": "dropdown",
            "dropdown": {
                "options": [
                    {"label": "Pastel Orange", "value": "beige"},
                    {"label": "Mint Green", "value": "mint"},
                    {"label": "Translucent Red", "value": "tred"},
                    {"label": "Translucent Blue", "value": "tblue"},
                    {"label": "Aqua Blue", "value": "aqua"},
                    {"label": "White", "value": "white"},
                    {"label": "Black", "value": "black"},
                    {"label": "Translucent Green", "value": "tgreen"},
                    {"label": "Clear", "value": "clear"},
                ],
            }
            },
            {
            "key": "Ocolors",
            "label": {"type": "custom", "custom": "O Color"},
            "optional": False,
            "type": "dropdown",
            "dropdown": {
                "options": [
                    {"label": "Pastel Orange", "value": "beige"},
                    {"label": "Mint Green", "value": "mint"},
                    {"label": "Translucent Red", "value": "tred"},
                    {"label": "Translucent Blue", "value": "tblue"},
                    {"label": "Aqua Blue", "value": "aqua"},
                    {"label": "White", "value": "white"},
                    {"label": "Black", "value": "black"},
                    {"label": "Translucent Green", "value": "tgreen"},
                    {"label": "Clear", "value": "clear"},
                ],
            },
        },]
    index=0
    for p in pricelist:
        finallist.append({
            "price_data": {
                "currency": "usd",
                "tax_behavior":"exclusive",
                "unit_amount": int(p) * 100,
                "product_data": {
                    "name": itemlist[index],
                },
            },
            "quantity": 1,})
        index = index + 1
            
    print(finallist)
    session = stripe.checkout.Session.create(
        success_url=YOUR_DOMAIN + "/success.html",
        cancel_url=YOUR_DOMAIN + "/cart.html",
        mode="payment",
        shipping_address_collection={"allowed_countries": ["US"]},
        automatic_tax={
            "enabled": True,
        },
        allow_promotion_codes= True,
        shipping_options=[
            {
                "shipping_rate_data": {
                "type": "fixed_amount",
                "tax_behavior": "exclusive",
                "fixed_amount": {"amount": 1000, "currency": "usd"},
                "display_name": "Standard shipping",
                },
            },
        ],
        submit_type="pay",
        custom_fields=customfield,
        payment_method_types=["card"],
        line_items=finallist,
    )
    return redirect(session.url, code=303)

if __name__ == "__main__":
    app.run()


