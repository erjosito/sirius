from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, vmodl
import ssl, atexit
import argparse


def getParameters():
	# Global variables defined
	global vCenterSvr
	global vCenterUsr
	global vCenterPwd
	global vmIP
	global vmAttKey
	global vmAttVal
	global debug
	# Find arguments and flags
	try:
		parser = argparse.ArgumentParser (description = 'Set custom attributes on VMs')
		parser.add_argument('-s', '--server', type=str,
						   help='vCenter server (IP or hostname)')
		parser.add_argument('-u', '--username', type=str,
						   help='vCenter username')
		parser.add_argument('-p', '--password', type=str,
						   help='vCenter password')
		parser.add_argument('-i', '--ip', type=str,
						   help='IP address of the VM whose attribute is to be set')
		parser.add_argument('-k', '--attributekey', type=str,
						   help='Custom attribute key to be set')
		parser.add_argument('-v', '--attributevalue', type=str,
						   help='Custom attribute key to be set')
		parser.add_argument('--verbose', action="store_true",
						   help='if additional verbose output should be shown (aka debug)')
		args = parser.parse_args()
		vCenterSvr = args.server
		vCenterUsr = args.username
		vCenterPwd = args.password
		vmIP = args.ip
		vmAttKey = args.attributekey
		vmAttVal = args.attributevalue
		debug = args.verbose
	except Exception as e:
		print str (e)
		parser.print_help ()
		sys.exit (0)

def main():

	# Global variables defined
	global vCenterSvr
	global vCenterUsr
	global vCenterPwd
	global vmIP
	global vmAttKey
	global vmAttVal
	global debug

	context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
	context.verify_mode = ssl.CERT_NONE

	si = SmartConnect(host = vCenterSvr, user = vCenterUsr, pwd = vCenterPwd, port='443', sslContext=context)
	atexit.register(Disconnect, si)
	content = si.content
	mykey = [k.key for k in content.customFieldsManager.field if k.name == vmAttKey]

	if not mykey:
	    content.customFieldsManager.AddCustomFieldDef(name = vmAttKey, moType = vim.VirtualMachine)
	    mykey = [k.key for k in content.customFieldsManager.field if k.name == vmAttKey]

	vmView = content.viewManager.CreateContainerView(content.rootFolder,[vim.VirtualMachine],True)
	vmList = vmView.view
	vmView.Destroy()

	for vm in vmList:
		try:
			if vm.summary.guest.ipAddress == vmIP:
				content.customFieldsManager.SetField(entity=vm, key=mykey[0], value=vmAttVal)
		except Exception as e:
			pass
	#content.customFieldsManager.SetField(entity=vmFound[0], key=mykey[0], value=vmAttVal)

vCenterSvr = ''
vCenterUsr = ''
vCenterPwd = ''
vmIP       = ''
vmAttKey   = ''
vmAttVal   = ''
debug      = False


if __name__ == '__main__':
	getParameters ()
	main()
