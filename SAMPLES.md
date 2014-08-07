#Samples
This document provides practical samples on how the functions included with this package can be used to administrate ArcGIS for Server services. For more information about the individual functions, please see the Functions Documentation page.

##Batch Adjust Minimum/Maximum Instances

This sample demonstrates how the minimum and maximum instances for a service can be edited through scripted calls to the Admin API. Using the input ArcGIS Server REST endpoint along with an administrative username/password combination, the script executes the *defineEndpoints* function to retrieve the REST, Token, and Admin URLs. It then gets a token from the token URL using the *getToken* function.  The script then uses this newly acquired token to get a list of all of the administrative service endpoints that the token has access to. An administrative service URL is the Admin API’s endpoint for that service (e.g. http://localhost:6080/arcgis/admin/services/SampleWorldCities.MapServer). The script then loops though this list using the* updateMinMaxInstance* function to iteratively updated the Minimum and Maximum instances per service. This function was intentionally designed for one service at a time so that it could be used outside the context of a loop if desired. Please see the respective function documentations for more information on expected parameters and syntax.

```python
import adminfunctions

# Parameters
AGSRestEndpoint = "http://myserver.mysite.com/arcgis/rest"
username = "admin"
password = "admin"

### Script execution - Where functions are executed.
endpoints = adminfunctions.defineEndpoints(AGSRestEndpoint)
token = adminfunctions.getToken(endpoints["TokenUrl"],username,password)["token"]

services = adminfunctions.getServiceAdminEndpoints(endpoints["Admin"], token)
for service in services:
    print "Editing " + service + "..."
    result = adminfunctions.updateMinMaxInstance(service,token,0,2)
    print result
    print ""
    
```

##Batch Start, Stop, or Delete Services

This sample demonstrates how to use the *StartStopDelete* function to either start, stop, or delete a service. Using the input ArcGIS Server REST endpoint along with an administrative username/password combination, the script executes the *defineEndpoints* function to retrieve the REST, Token, and Admin URLs. It then gets a token from the token URL using the getToken function.  The script then uses this newly acquired token to get a list of all of the administrative service endpoints that the token has access to. An administrative service URL is the Admin API’s endpoint for that service (http://localhost:6080/arcgis/admin/services/SampleWorldCities.MapServer). The script then loops though this list using the* StartStopDelete* function to iteratively perform the desired effect on the each service in the list. This function was intentionally designed for one service at a time so that it could be used outside the context of a loop if desired. Please see the respective function documentations for more information on expected parameters and syntax.

```python
import adminfunctions

#Parameters
AGSRestEndpoint = "http://myserver.mysite.com/arcgis/rest"
username = "admin"
password = "admin"

###Script execution - Where functions are executed.
endpoints = adminfunctions.defineEndpoints(AGSRestEndpoint)
token = adminfunctions.getToken(endpoints["TokenUrl"],username,password)["token"]

services = adminfunctions.getServiceAdminEndpoints(endpoints["Admin"], token)

for service in services:
    print "Administrating " + service + "..."
    result = adminfunctions.StartStopDelete(service,token,"stop")
    print result
    print ""
```

##Update Service Timeouts

This sample demonstrates how to use the *updateTimeouts* function to modify the service timeout values for the input service. Using the input ArcGIS Server REST endpoint along with an administrative username/password combination, the script executes the *defineEndpoints* function to retrieve the REST, Token, and Admin URLs. It then gets a token from the token URL using the* getToken* function.  The script then uses this newly acquired token to get a list of all of the administrative service endpoints that the token has access to. An administrative service URL is the Admin API’s endpoint for that service (http://localhost:6080/arcgis/admin/services/SampleWorldCities.MapServer). The script then loops though this list using the* updateTimeouts* function to iteratively update the values for each service. This function was intentionally designed for one service at a time so that it could be used outside the context of a loop if desired. Please see the respective function documentations for more information on expected parameters and syntax.

```python
import adminfunctions

#Parameters
AGSRestEndpoint = "http://myserver.mysite.com/arcgis/rest"
username = "admin"
password = "admin"

###Script execution - Where functions are executed.
endpoints = adminfunctions.defineEndpoints(AGSRestEndpoint)
token = adminfunctions.getToken(endpoints["TokenUrl"],username,password)["token"]

services = adminfunctions.getServiceAdminEndpoints(endpoints["Admin"], token)
for service in services:
    print "Editing " + service + "..."
    result = adminfunctions.updateTimeouts(service,token,60,300,1800,600)
    print result
    print ""
```

##Backup Site

This sample demonstrates how to use the *backupSite* function to backup an ArcGIS Server site through the Admin API (requires ArcGIS for Server 10.2 or higher). Using the input ArcGIS Server REST endpoint along with an administrative username/password combination, the script executes the *defineEndpoints* function to retrieve the REST, Token, and Admin URLs. It then gets a token from the token URL using the *getToken* function. The script then sends an ExportSite request to the Admin API to create a backup at the specified path. The function output is a dictionary with the keys “outcome” and “message”. This is done so that the script executing the function can be responsive to the outcome of the backup. For example, if the function is part of a larger script, and the backup is a precursor to sweeping changes made by that script, you could easily program the script to not proceed if the backup fails as a safety precausion. If the “outcome” is successful, the “messages” key will contain the path to the backup file. Else, the messages regarding the error are returned. This responsive nature is demonstrated in the sample by proceeding based on the value of the “outcome” key. Please see the respective function documentations for more information on expected parameters and syntax.

```python
import adminfunctions

#Parameters
AGSRestEndpoint = "http://myserver.mysite.com/arcgis/rest"
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
    
```
