import requests
from flask import Flask, render_template, redirect, url_for, request

#  This is for later use while I play around
# with location pins flags


class FlagFetch:
    def __init__(self, requested_country):
        self.requested_country = requested_country
        self.endpoint = f"https://restcountries.com/v3.1/name/{self.requested_country}"
        self.response = requests.get(self.endpoint)
        self.data = self.response.json()

    def get_cca3(self):

        self.cca3 = self.data[0]['cca3']
        return (self.cca3)

    def get_flag_png(self):

        self.flag_png = self.data[0]['flags']['png']
        return (self.flag_png)

    def get_name(self):
        self.name = self.data[0]['name']['common']
        return self.name


app = Flask(__name__)
app.config["SECRET_KEY"] = "fbhsikufgkbwigfuidekd7i6i"
