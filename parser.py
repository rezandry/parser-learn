class Parser:

    def parse_xml(self, input):
        pass

    def parse_json(self, input):
        pass

    def parse_sms(self, input):
        pass


xml = """<payload>
    <action>TOPUP</action>
    <denom>XL100</denom>
    <phonenumber>085642405493</phonenumber>
</payload>"""

sms = "TOPUP XL100 085642405493"

json = """{
    "transaction_type":"TOPUP",
    "denom":"XL100",
    "phone_number":"085642405493"
}"""


parser = Parser()
output_xml = parser.parse_xml(xml)
print(xml)
print(output_xml)


output_sms = parser.parse_sms(sms)
print(sms)
print(output_sms)


output_json = parser.parse_json(json)
print(json)
print(output_json)