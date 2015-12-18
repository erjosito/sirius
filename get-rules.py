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
    try:
		r = requests.get(
                        url = apic_url + "api/node/mo/uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1.json",
                        params = {
                              "rsp-prop-include": "config-only",
                              "rsp-subtree": "full",
                        },
			cookies = login_cookies
		)
		json_obj = json.loads (r.text)
                # Get the ACL "access-list-inbound"
                acl = json_obj ['imdata'][0]['fvAEPg']['children'][6]['vnsFolderInst']['children']
		numACEs = len (acl)
                # Browse the ACL
		print "<table width='100%%' id='acltable'>"
		print "  <thead><tr><th align='left'>Delete?</th><th>Order</th><th>Name</th><th>Protocol</th><th>Port</th></tr></thead>"
		for i in range (0, numACEs):
			name   = acl[i]['vnsFolderInst']['attributes']['name']
                        prot = ""
                        port = ""
                        order = ""
                        acl_children = acl[i]['vnsFolderInst']['children']
                        for j in range (0, len(acl_children)):
                            keys = acl_children[j].keys ()
                            if (keys[0] == 'vnsFolderInst'):
                                if (acl_children[j]['vnsFolderInst']['attributes']['key'] == 'protocol'): 
                                    acl_children_2 = acl_children[j]['vnsFolderInst']['children']
                                    acl_children_2_len = len (acl_children_2)
                                    for k in range (0, acl_children_2_len):
                                        keys_2 = acl_children_2[k].keys ()
                                        if (keys_2[0] == 'vnsParamInst'):
			                    prot   = acl_children_2[k]['vnsParamInst']['attributes']['name']
                                elif (acl_children[j]['vnsFolderInst']['attributes']['key'] == 'destination_service'):
                                    acl_children_2 = acl_children[j]['vnsFolderInst']['children']
                                    acl_children_2_len = len (acl_children_2)
                                    for k in range (0, acl_children_2_len):
                                        keys_2 = acl_children_2[k].keys ()
                                        if (keys_2[0] == 'vnsParamInst'):
                                            if (acl_children_2[k]['vnsParamInst']['attributes']['key'] == "low_port"):
                                                port   = acl_children_2[k]['vnsParamInst']['attributes']['value']
                            elif (keys[0] == 'vnsParamInst'):
                                if (acl_children[j]['vnsParamInst']['attributes']['key'] == 'order'):
                                   order = acl_children[j]['vnsParamInst']['attributes']['value']

			print "  <tr><td><input type='radio' name='rules' value='%s'></td><td align='center'>%s</td><td align='center'>%s</td><td align='center'>%s</td><td align='center'>%s</td></tr>" % (name, order, name, prot, port)
		print "</table>"
    except requests.exceptions.RequestException as e:
        print('REST API Request failed')
# Create cookie variable
login_cookies = ""

# Get CLI arguments
if (len(sys.argv) != 4):
	print "I need 3 arguments: url, user and password"
else:
	# Get arguments
	apic_url = sys.argv[1]
	apic_usr = sys.argv[2]
	apic_pwd = sys.argv[3]
	# Add trailing slash to url if not there
	if apic_url [len (apic_url) - 1] != "/":
		apic_url += "/"
	# Do what you need to do
	login ()
	get_info ()

