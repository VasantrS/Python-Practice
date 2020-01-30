
# Python mail script with smtplib, email.utils and email.mime.text.

# --- imports ---

import smtplib
import email.utils
from email.mime.text import MIMEText
import os
import subprocess
import socket
Service="jbossjdv" # Change service name as per 
Threshold=20   # Threshold values as per your requirement

No_disk_issue=''
Disk_Bool=False
Service_Bool=False
p=subprocess.Popen("df -P | awk '0+$5 >= "+str(Threshold)+" {print}'| awk '{print $NF}'", stdout=subprocess.PIPE, shell=True);
(output, err) = p.communicate();
p_status = p.wait();
p_status;
print(output)
type(output.split("\n"))
output_list=(output.split("\n"))
output_list=list(filter(None,output_list))
if len(output_list) ==0:
	No_disk_issue=''+"No Diskspace issue"
else:
	No_disk_issue=''+"Diskspace issue"
	Disk_Bool=True

if os.system("service "+ Service + " status")>0:
	Service_Bool=True	
else:
	pass	


def Main(Disk_Bool,Service_Bool,No_disk_issue,Service,output_list):
	ServerName=socket.gethostname()
	server = smtplib.SMTP()
	server.connect ('smtpServerName',port) # Give SMTP server name and port 
	if Disk_Bool==True:
		if Service_Bool==True:
			Test_Subject = '   ' + No_disk_issue +"   On   "+ str(output_list) +   "  \n   " +Service+"  \n  Service is DOWN   "
			msg = MIMEText(str(len(output_list))+"  Disk_issues Those are ------->  " +str(output_list)+" \n \t\t " + Service +  "   Service is not running   "+" \n\t\t\t\t "+ServerName)
		else :
		 	Test_Subject = '   ' + No_disk_issue +"   On   "+ str(output_list) +   "  \n   " +Service+"  \n  Service is Running   "
			msg = MIMEText(str(len(output_list))+"  Disk_issues Those are ------->  " +str(output_list)+" \n \t\t " + Service +  "   Service is Running   "+" \n \t\t\t\t "+ServerName)
	else:
		if Service_Bool==True:
			Test_Subject ='   '+ No_disk_issue + "\n "+ Service+" \n  Service is Down   "
			msg = MIMEText(str(len(output_list))+"  Disk_issues   \n   \t\t "   + Service +  "   Service is not running  \n\t\t\t\t "+ServerName)
		else:	
			Test_Subject="   " +No_disk_issue+ " \n    "+ str(Service) + "  \n  "+"    Service is Running "
			msg = MIMEText(str(len(output_list))+"  Disk_issues  \n \t\t " + Service +  " Service is running   "+" \n\t\t\t\t "+ServerName)
	To_address='Your team mail id or yours mail id' # Give receiver mail id 
	From_address='Sender mail id' # GIve sender mail id
	msg['To'] = email.utils.formataddr(('Adminteam', To_address))
	msg['From'] = email.utils.formataddr(('Reporting', From_address))
	msg['Subject']=Test_Subject+""+ServerName
	try:
		server.sendmail(From_address, [To_address], msg.as_string())
	finally:
		server.quit()
	return


Main(Disk_Bool,Service_Bool,No_disk_issue,Service,output_list)
