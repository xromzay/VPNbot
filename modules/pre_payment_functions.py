# import the Payment provider token from config.py
from config import PAYMENT_PROVIDER_TOKEN

# import the required Telegram modules
from telegram import Update, LabeledPrice
from telegram.ext import ContextTypes


# define a function that handles user's callback query when a product is selected
async def select_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # extract the callback query and chat id from the update object
    query = update.callback_query
    chat_id = query.message.chat_id

    # extract the selected product from the callback query data
    product = query.data

    # check which product is selected and set the corresponding price, title, payload and description
    if product == "product_35":
        price = [LabeledPrice("1 Week", 35)]
        title = "VPN Access Pass - 1 Month"
        description = "Get one week of access to hawktuahVPN"
        payload = "1 Month"
    elif product == "product_52":
        price = [LabeledPrice("1 Month", 52)]
        title = "VPN Access Pass - 1 Month Premium"
        description = "Get one month of premium access to hawktuahVPN"
        payload = "1 Month"
    elif product == "product_70":
        price = [LabeledPrice("1 Month SIGMIUM", 70)]
        title = "VPN Access Pass - 1 Month SIGMIUM"
        description = "Get one month of unlimited access to hawktuahVPN"
        payload = "1 Month"
    else:
        # handle invalid product selection by returning
        return

    # set the payment currency
    currency = "RUB"

    # send the invoice to the user with the selected product price
    await context.bot.send_invoice(
        chat_id, title, description, payload, PAYMENT_PROVIDER_TOKEN, currency, price
    )
