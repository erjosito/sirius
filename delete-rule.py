import requests
import json
import sys

login_cookies = 0

def login():
    # Login (POST http://muc-apic.cisco.com/api/aaaLogin.xml)
    global login_cookies
    global apic_url
    global apic_usr
    global apic_pwd
    try:
        r = requests.post(
            url = apic_url + "api/aaaLogin.xml",
            data = "<aaaUser name=\"" + apic_usr + "\" pwd=\"" + apic_pwd + "\" />"
        )
        login_cookies = r.cookies
    except requests.exceptions.RequestException as e:
        print('Login HTTP Request failed')

def main():
    global login_cookies
    global apic_url

    try:
        response = requests.post(
            cookies = login_cookies,
            url=apic_url+"api/node/mo/uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-access-list-inbound/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-" + rulename + ".json",
            data="{\"vnsFolderInst\": {\"attributes\": {" + \
                 "\"dn\":\"uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-access-list-inbound/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-" + rulename + "\"," + \
                 "\"status\": \"deleted\"}, \"children\": [] }}"
        )
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Create cookie variable
login_cookies = ""

# Get CLI arguments
if (len(sys.argv) != 5):
	print "I need 4 arguments: url, user, password and rulename"
else:
	# Get arguments
	apic_url = sys.argv[1]
	apic_usr = sys.argv[2]
	apic_pwd = sys.argv[3]
        rulename = sys.argv[4]
	# Add trailing slash to url if not there
	if apic_url [len (apic_url) - 1] != "/":
		apic_url += "/"
	# Do what you need to do
	login ()
	main ()

