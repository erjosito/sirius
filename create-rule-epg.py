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
            data="\
{ \
  \"vnsFolderInst\": { \
    \"attributes\": { \
      \"childAction\": \"deleteNonPresent\", \
      \"ctrctNameOrLbl\": \"out-to-app1\",  \
      \"dn\": \"uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-access-list-inbound/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-" + rulename + "\",  \
      \"graphNameOrLbl\": \"Sirius-FE-SGT\", \
      \"key\": \"AccessControlEntry\", \
      \"name\": \"" + rulename + "\", \
      \"nodeNameOrLbl\": \"N1\", \
      \"status\": \"created,modified\" \
    }, \
    \"children\": [ \
      { \
        \"vnsFolderInst\": { \
          \"attributes\": { \
            \"childAction\": \"deleteNonPresent\",  \
            \"ctrctNameOrLbl\": \"out-to-app1\", \
            \"dn\": \"uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-access-list-inbound/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-" + rulename + "/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-destination_address\", \
            \"graphNameOrLbl\": \"Sirius-FE-SGT\", \
            \"key\": \"destination_address\", \
            \"name\": \"destination_address\", \
            \"nodeNameOrLbl\": \"N1\", \
            \"status\": \"created,modified\" \
          }, \
          \"children\": [ \
            { \
              \"vnsParamInst\": { \
                \"attributes\": { \
                  \"dn\": \"uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-access-list-inbound/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-" + rulename + "/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-destination_address/ParamInst-epg_name\", \
                  \"key\": \"epg_name\", \
                  \"name\": \"epg_name\", \
                  \"status\": \"created,modified\", \
                  \"value\": \"SiriusCyber-Sirius-App1-Tier1\" \
                }, \
                \"children\": [] \
              } \
            } \
          ] \
        } \
      }, \
      { \
        \"vnsFolderInst\": { \
          \"attributes\": { \
            \"childAction\": \"deleteNonPresent\", \
            \"ctrctNameOrLbl\": \"out-to-app1\", \
            \"dn\": \"uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-access-list-inbound/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-" + rulename + "/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-destination_service\", \
            \"graphNameOrLbl\": \"Sirius-FE-SGT\", \
            \"key\": \"destination_service\", \
            \"name\": \"destination_service\", \
            \"nodeNameOrLbl\": \"N1\", \
            \"status\": \"created,modified\" \
          }, \
          \"children\": [ \
            { \
              \"vnsParamInst\": { \
                \"attributes\": { \
                  \"dn\": \"uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-access-list-inbound/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-" + rulename + "/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-destination_service/ParamInst-low_port\", \
                  \"key\": \"low_port\", \
                  \"name\": \"low_port\", \
                  \"status\": \"created,modified\", \
                  \"value\": \"" + port + "\" \
                }, \
                \"children\": [] \
              } \
            }, \
            { \
              \"vnsParamInst\": { \
                \"attributes\": { \
                  \"dn\": \"uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-access-list-inbound/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-" + rulename + "/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-destination_service/ParamInst-operator\", \
                  \"key\": \"operator\", \
                  \"name\": \"operator\", \
                  \"status\": \"created,modified\", \
                  \"value\": \"eq\" \
                }, \
                \"children\": [] \
              }}]}}, \
      { \
        \"vnsFolderInst\": { \
          \"attributes\": { \
            \"childAction\": \"deleteNonPresent\", \
            \"ctrctNameOrLbl\": \"out-to-app1\", \
            \"dn\": \"uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-access-list-inbound/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-" + rulename + "/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-source_address\", \
            \"graphNameOrLbl\": \"Sirius-FE-SGT\",  \
            \"key\": \"source_address\", \
            \"name\": \"source_address\",  \
            \"nodeNameOrLbl\": \"N1\", \
            \"status\": \"created,modified\" \
          }, \
          \"children\": [ \
            { \
              \"vnsParamInst\": { \
                \"attributes\": { \
                  \"dn\": \"uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-access-list-inbound/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-" + rulename + "/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-source_address/ParamInst-any\",  \
                  \"key\": \"any\", \
                  \"name\": \"any\", \
                  \"status\": \"created,modified\",  \
                  \"value\": \"any\" \
                }, \
                \"children\": [] \
              } \
            } \
          ] \
        } \
      }, \
      { \
        \"vnsFolderInst\": { \
          \"attributes\": { \
            \"childAction\": \"deleteNonPresent\", \
            \"ctrctNameOrLbl\": \"out-to-app1\", \
            \"dn\": \"uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-access-list-inbound/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-" + rulename + "/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-tcp\",  \
            \"graphNameOrLbl\": \"Sirius-FE-SGT\",  \
            \"key\": \"protocol\", \
            \"name\": \"" + prot + "\", \
            \"nodeNameOrLbl\": \"N1\", \
            \"status\": \"created,modified\" \
          }, \
          \"children\": [ \
            { \
              \"vnsParamInst\": { \
                \"attributes\": { \
                  \"dn\": \"uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-access-list-inbound/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-" + rulename + "/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-tcp/ParamInst-tcp\",  \
                  \"key\": \"name_number\", \
                  \"name\": \"" + prot + "\", \
                  \"status\": \"created,modified\",  \
                  \"value\": \"" + prot + "\" \
                }, \
                \"children\": [] \
              } \
            } \
          ] \
        } \
      },  \
      { \
        \"vnsParamInst\": { \
          \"attributes\": { \
            \"dn\": \"uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-access-list-inbound/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-" + rulename + "/ParamInst-action\", \
            \"key\": \"action\", \
            \"name\": \"action\", \
            \"status\": \"created,modified\", \
            \"value\": \"permit\" \
          }, \
          \"children\": [] \
        } \
      }, \
      { \
        \"vnsParamInst\": { \
          \"attributes\": { \
            \"dn\": \"uni/tn-SiriusCyber/ap-Sirius-App1/epg-Tier1/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-access-list-inbound/FI_C-out-to-app1-G-Sirius-FE-SGT-F-N1-N-" + rulename + "/ParamInst-order\", \
            \"key\": \"order\", \
            \"name\": \"order\", \
            \"status\": \"created,modified\",  \
            \"value\": \"" + order + "\" \
          }, \
          \"children\": [] \
        } \
      } \
    ] \
  } \
} \
                 "
        )
    except requests.exceptions.RequestException:
        print('HTTP Request failed')


# Create cookie variable
login_cookies = ""

# Get CLI arguments
if (len(sys.argv) != 8):
	print "I need 7 arguments: url, user, password, rulename, protocol, port number and ACE order"
else:
	# Get arguments
	apic_url = sys.argv[1]
	apic_usr = sys.argv[2]
	apic_pwd = sys.argv[3]
        rulename = sys.argv[4]
        prot     = sys.argv[5]
        port     = sys.argv[6]
        order    = sys.argv[7]
	# Add trailing slash to url if not there
	if apic_url [len (apic_url) - 1] != "/":
		apic_url += "/"
	# Do what you need to do
	login ()
	main ()

