from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://bibtranscolbpes.es.gov.br/mobile/'
RESULT_URL = f'{BASE_URL}resultado.asp'