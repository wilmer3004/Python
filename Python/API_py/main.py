from flask import Flask

import requests
if __name__  == '__main__':
    url = 'https://www.google.com.mx/'
    response = requests.get(url)
    
    print(response)
    
    print(dir(requests))    