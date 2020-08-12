import webbrowser
import time

def search_amazon_basic(what):
    webbrowser.open_new(f"https://www.amazon.ca/s?k={what}")

search_amazon_basic("milk")
