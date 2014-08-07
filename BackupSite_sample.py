import adminfunctions

#Parameters
AGSRestEndpoint = "http://localhost:6080/arcgis/rest"
username = "admin"
password = "admin"

###Script execution - Where functions are executed.
endpoints = adminfunctions.defineEndpoints(AGSRestEndpoint)
token = adminfunctions.getToken(endpoints["TokenUrl"],username,password)["token"]

backup = adminfunctions.backupSite(endpoints["Admin"],token,r"C:\temp")

if backup['outcome'] != "success":
    print backup['messages']
else:
    print "Backup Created: " + backup['messages']
    
