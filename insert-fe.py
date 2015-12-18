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
    # Insert FE SG
    global login_cookies
    try:
        r = requests.post(
            url="http://192.168.0.50/api/node/mo/uni/tn-SiriusCyber/brc-out-to-app1/subj-Subject/rsSubjGraphAtt.json",
            data="{\"vzRsSubjGraphAtt\":{\"attributes\":{\"tnVnsAbsGraphName\":\"Sirius-FE-SGT\",\"status\":\"created,modified\"},\"children\":[]}}",
            cookies = login_cookies
        )
    except requests.exceptions.RequestException as e:
        print('Remove FE SG HTTP Request failed')

    # Move the ISR L3out to the external VRF
    try:
        r = requests.post(
            url="http://192.168.0.50/api/node/mo/uni/tn-SiriusCyber/out-ToISR/rsectx.json",
            data="{\"l3extRsEctx\":{\"attributes\":{\"tnFvCtxName\":\"Sirius-external\"},\"children\":[]}}",
            cookies = login_cookies
        )
    except requests.exceptions.RequestException as e:
        print('Move ISR L3out to the external VRF HTTP Request failed')

login()
main()

