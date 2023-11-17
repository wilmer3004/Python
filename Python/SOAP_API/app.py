# Este proyecto sirve desde google colab

import requests
import xml.etree.ElementTree as ET



url = "https://www.w3schools.com/xml/tempconvert.asmx"

SOAPEnvelope = """
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CelsiusToFahrenheit xmlns="https://www.w3schools.com/xml/">
      <Celsius>string</Celsius>
    </CelsiusToFahrenheit>
  </soap:Body>
</soap:Envelope>
"""

headers = {
    "Content-Type": "text/xml; charset=utf-8",
}
response = requests.post(url, data=SOAPEnvelope, headers=headers)
root = ET.fromstring(response.text)

# Corrected the tag name in the following line
for child in root.iter("*"):
    print(child.tag, child.text )
