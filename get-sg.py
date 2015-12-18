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

def get_info():
    # Create tenant (POST http://10.49.238.40/api/node/mo/uni/tn-helloworld_REST.json)
    global login_cookies
    global apic_url
    global subject
    try:
		r = requests.get(
                        url = apic_url + "api/node/mo/uni/tn-SiriusCyber/brc-" + contract + "/subj-" + subject + ".json",
                        params = {
                              "rsp-prop-include": "config-only",
                              "rsp-subtree": "full",
                        },
			cookies = login_cookies
		)
		json_obj = json.loads (r.text)
                # Get the subject 
                subject = json_obj ['imdata'][0]['vzSubj']['children']
		numchildren = len (subject)
		for i in range (0, numchildren):
                        SG = ""
                        keys = subject[i].keys ()
                        if (keys[0] == 'vzRsSubjGraphAtt'):
                            SG = subject[i]['vzRsSubjGraphAtt']['attributes']['tnVnsAbsGraphName']

		print SG 
    except requests.exceptions.RequestException as e:
        print('REST API Request failed')
# Create cookie variable
login_cookies = ""

# Get CLI arguments
if (len(sys.argv) != 6):
	print "I need 5 arguments: url, user, password, contract and subject name"
else:
	# Get arguments
	apic_url = sys.argv[1]
	apic_usr = sys.argv[2]
	apic_pwd = sys.argv[3]
	contract = sys.argv[4]
	subject  = sys.argv[5]
	# Add trailing slash to url if not there
	if apic_url [len (apic_url) - 1] != "/":
		apic_url += "/"
	# Do what you need to do
	login ()
	get_info ()

