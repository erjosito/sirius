import requests

login_cookies = 0

def login():
    # Login (POST http://192.168.0.50/api/aaaLogin.xml)
    global login_cookies
    try:
        r = requests.post(
            url="http://192.168.0.50/api/aaaLogin.xml",
            data = "<aaaUser name=\"admin\" pwd=\"C15co123\" />"
        )
        login_cookies = r.cookies
    except requests.exceptions.RequestException as e:
        print('Login HTTP Request failed')

def main():
    # Add BE SG
    global login_cookies
    try:
        r = requests.post(
            url="http://192.168.0.50/api/node/mo/uni/tn-SiriusCyber/brc-App1-T2-Services/subj-App1-T2-Svc/rsSubjGraphAtt.json",
            data="{\"vzRsSubjGraphAtt\":{\"attributes\":{\"tnVnsAbsGraphName\":\"Sirius-BE-SGT\",\"status\":\"created,modified\"},\"children\":[]}}",
            cookies = login_cookies
        )
    except requests.exceptions.RequestException as e:
        print('Add BE SG HTTP Request failed')

    # Replace the IP addresses in the fabric with the FW's IP addresses
    # That is, remove the .1 addresses (the .254 had been left)
    try:
        r = requests.post(
            url="http://192.168.0.50/api/node/mo/uni/tn-SiriusCyber/BD-Sirius-BD1.json",
            data="{\"fvBD\":{\"attributes\":{\"dn\":\"uni/tn-SiriusCyber/BD-Sirius-BD1\",\"status\":\"modified\"},\"children\":[{\"fvSubnet\":{\"attributes\":{\"dn\":\"uni/tn-SiriusCyber/BD-Sirius-BD1/subnet-[172.18.1.1/24]\",\"status\":\"deleted\"},\"children\":[]}}]}}",
            cookies = login_cookies
        )
    except requests.exceptions.RequestException as e:
        print('Delete 172.18.1.1 HTTP Request failed')
    '''
    try:
        r = requests.post(
            url="http://192.168.0.50/api/node/mo/uni/tn-SiriusCyber/BD-Sirius-BD1/subnet-%5B172.18.1.254/24%5D.json",
            data="{\"fvSubnet\":{\"attributes\":{\"dn\":\"uni/tn-SiriusCyber/BD-Sirius-BD1/subnet-[172.18.1.254/24]\",\"ip\":\"172.18.1.254/24\",\"scope\":\"public\",\"rn\":\"subnet-[172.18.1.254/24]\",\"status\":\"created\"},\"children\":[]}}",
            cookies = login_cookies
        )
    except requests.exceptions.RequestException as e:
        print('Add 172.18.1.254 HTTP Request failed')
    '''
    try:
        r = requests.post(
            url="http://192.168.0.50/api/node/mo/uni/tn-SiriusCyber/BD-Sirius-BD2.json",
            data="{\"fvBD\":{\"attributes\":{\"dn\":\"uni/tn-SiriusCyber/BD-Sirius-BD2\",\"status\":\"modified\"},\"children\":[{\"fvSubnet\":{\"attributes\":{\"dn\":\"uni/tn-SiriusCyber/BD-Sirius-BD2/subnet-[172.18.2.1/24]\",\"status\":\"deleted\"},\"children\":[]}}]}}",
            cookies = login_cookies
        )
    except requests.exceptions.RequestException as e:
        print('Delete 172.18.2.1 HTTP Request failed')
    '''
    try:
        r = requests.post(
            url="http://192.168.0.50/api/node/mo/uni/tn-SiriusCyber/BD-Sirius-BD2/subnet-%5B172.18.2.254/24%5D.json",
            data="{\"fvSubnet\":{\"attributes\":{\"dn\":\"uni/tn-SiriusCyber/BD-Sirius-BD2/subnet-[172.18.2.254/24]\",\"ip\":\"172.18.2.254/24\",\"scope\":\"public\",\"rn\":\"subnet-[172.18.2.254/24]\",\"status\":\"created\"},\"children\":[]}}",
            cookies = login_cookies
        )
    except requests.exceptions.RequestException as e:
        print('Add 172.18.2.254 HTTP Request failed')
    '''

login()
main()

