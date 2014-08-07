# Function Documentation

This is a documentation list of all of the functions defined within the administrateservices.py file included within this package. Please see the samples documentation for practical examples on how these functions can be used.


## Define Endpoints

####Purpose
Takes a defined REST endpoint as input and returns the standardized base REST URL, Token URL, and Admin API URL. 

####Output
Returns dictionary with keys “REST, “TokenUrl”, and “Admin”.

####Call
adminfunctions.defineEndpoints(agsURL)

#### Parameters
Parameter		|	Description
-------------	|	------------
agsUrl    		|  *String* – An ArcGIS Server REST URL.



## Get Token

####Purpose

Retrieves a short-lived token from the specified AGS Token URL, username, and password.

####Output

Returns dictionary with keys “token” and “expires”.

####Call

adminfunctions.getToken(tokenURL, username, password)

#### Parameters

Parameter		|	Description
-------------	|	------------
tokenURL		|	*String* - The ArcGIS Server Token URL from which the token is retrieved (e.g https://sampleserver6.arcgisonline.com/arcgis/tokens/)
username		|	*String* – String value representing the username.
password		|	*String* – String value representing theusername.



## Get Service Administrative Endpoints

####Purpose

Crawls the Admin API’s Services directory for all services that can be administrated by the user associated with the token. Recursively loops through all non-default directories (System and Utilities are excluded).

####Output

A list of all of the administrative service URLs returned by the function. (e.g. http://arcgisserver.com/arcgis/admin/SampleWorldCities.MapServer)

####Call

adminfunctions.getServiceAdminEndpoints (adminUrl, token)

#### Parameters

Parameter		|	Description
-------------	|	------------
adminUrl		|	*String* – The ArcGIS Server Admin API URL. This value can be returned using the defineEndpoints function by retrieving the resulting “Admin” key value.
token			|	*String* – A token allowing the user to access the REST endpoint. A token can be automatically generated using the getToken function and retrieving the resulting “token” key value.



##	Update Minimum and Maximum Instances Per Node

####Purpose

Sends an edit request to the specified administrative service URL to update the minimum and maximum number of instance per node values.

####Output

Returns a message specifying whether the edit request was successful or not.

####Call

adminfunctions.updateMinMaxInstance(serviceAdminURL, token, minInstances, maxInstances)

#### Parameters

Parameter		|	Description
-------------	|	------------
serviceAdminURL	|	*String* – A specific administrative URL for an ArcGIS Server Service (e.g. http://arcgisserver.com/arcgis/admin/SampleWorldCities.MapServer). Administrative URLs can be collected using the getServiceAdminEndpoints
token			|	*String* – A token allowing the user to access the REST endpoint. A token can be automatically generated using the getToken function and retrieving the resulting “token” key value.
minInstances	|	*Integer* – The minimum number of instances desired.
maxInstances	|	*Integer* – The maximum number of instances desired.



## Start, Stop, and Delete Services

####Purpose

Sends a request to either start, stop, or delete a service via an administrative service URl and token passed to the function. 

####Output

Returns a message specifying whether the request was successful or not.

####Call

adminfunctions.StartStopDelete(serviceAdminUrl, token, operation)

#### Parameters

Parameter		|	Description
-------------	|	------------
serviceAdminURL	|	*String* – A specific administrative URL for an ArcGIS Server Service (e.g. http://arcgisserver.com/arcgis/admin/SampleWorldCities.MapServer). Administrative URLs can be collected using the getServiceAdminEndpoints
token			|	*String* – A token allowing the user to access the REST endpoint. A token can be automatically generated using the getToken function and retrieving the resulting “token” key value.
operation		|	*String* – Must be “stop”, “start”, or “delete”.



## Update Timeouts

#### Purpose

Sends an edit request to the specified administrative URL to update the service timeout parameters. 

#### Output

Returns a message specifying whether the request was successful or not.

#### Call

updateTimeouts(serviceAdminUrl, token, maxWaitTime, maxStartupTime, maxIdleTime)

#### Parameters

Parameter		|	Description
-------------	|	------------
serviceAdminURL	|	*String* – A specific administrative URL for an ArcGIS Server Service (e.g. http://arcgisserver.com/arcgis/admin/SampleWorldCities.MapServer). Administrative URLs can be collected using the getServiceAdminEndpoints
token			|	*String* – A token allowing the user to access the Admin endpoint. A token can be automatically generated using the getToken function and retrieving the resulting “token” key value.
maxWaitTime		|	*Integer* – The maximum number of seconds a client will wait for an instance. To use default value (60), specify “” as the parameter value.
maxStartupTime	|	*Integer* – The maximum number of seconds the GIS Server will wait for an instance to start before assuming the startup is hanging. To use default value (300), specify “” as the parameter value.
maxIdleTime		|	*Integer* – The maximum number of seconds that an instance can remain Idle before it is destroyed by the GIS Server. To use default value (1800), specify “” as the parameter value.
maxUsageTime	|	*Integer* – The maximum number of seconds a client can use a service. To use default value (600), specify “” as the parameter value.



## Backup Site (Requires ArcGIS for Server 10.2 and higher)

#### Purpose

Performs a backup of the ArcGIS Server Site. This task can be automated to run on a schedule, or to preclude any full-scale scripted changes.

#### Output

Returns a dictionary that includes the keys “outcome” and “messages”. This is done so that the script can be responsive to the outcome of the backup. For example, if this function is part of a larger script, and the backup is a precursor to sweeping changes made by this script, you could easily program the script to not proceed if the backup fails. If the “outcome” is successful, the “messages” key will contain the path to the backup file. Else, the messages regarding the error are returned.

#### Call

backupSite(adminUrl, token, outputDirectory)

#### Parameters

Parameter		|	Description
-------------	|	------------
adminUrl		|	*String* – The ArcGIS Server Admin API URL. This value can be returned using the defineEndpoints function by retrieving the resulting “Admin” key value.
token			|	*String* – A token allowing the user to access the Admin endpoint. A token can be automatically generated using the getToken function and retrieving the resulting “token” key value.
outputDirectory	|	*String* – The output locator to which the backup will be written. If successful, the message will include path and file-name of the output backup file. NOTE: specifying a local directory will output a file that is local to the Server, not the client. 
