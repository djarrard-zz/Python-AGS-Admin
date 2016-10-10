import adminfunctions

#Parameters - use portal credentials for federated setup
AGSRestEndpoint = "http://myserver.mysite.com/arcgis/rest"
username = "siteadmin"
password = "siteadmin"
referer = "http://referer.mysite.com/arcgis/rest"

###Script execution - Where functions are executed.
endpoints = adminfunctions.defineEndpoints(AGSRestEndpoint)
token = adminfunctions.getToken(endpoints["TokenUrl"],username,password, referer)["token"]

backup = adminfunctions.backupSite(endpoints["Admin"],token,r"C:\temp")

if backup['outcome'] != "success":
    print backup['messages']
else:
    print "Backup Created: " + backup['messages']

