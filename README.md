# Scripted Server Administration Framework

## Features

This project is intended to provide a base resource that allows a GIS  server administrator to perform batch tasks using Python and ArcGIS for Server's web-based Admin API. The framework currently includes the following functions. Samples are provided that demonstrate usage of these samples:

* [**defineEndpoints**](https://github.com/djarrard/Python-AGS-Admin/blob/master/FUNCTION%20DOCUMENTATION.md#define-endpoints) - defines ArcGIS Server’s web-based endpoints including REST, Admin API, and Token URL.
* [**getToken**](https://github.com/djarrard/Python-AGS-Admin/blob/master/FUNCTION%20DOCUMENTATION.md#get-token) - retrieves a short-lived token from the Token URL.
* [**getServiceAdminEndpoints**](https://github.com/djarrard/Python-AGS-Admin/blob/master/FUNCTION%20DOCUMENTATION.md#get-service-administrative-endpoints) - Provides a list of administrative service URLs that can be used by other functions in the framework.
* [**updateMinMaxInstance**](https://github.com/djarrard/Python-AGS-Admin/blob/master/FUNCTION%20DOCUMENTATION.md#update-minimum-and-maximum-instances-per-node) - edits input service(s) to modify the Minimum and Maximum number of instances per service parameters.
* [**StartStopDelete**](https://github.com/djarrard/Python-AGS-Admin/blob/master/FUNCTION%20DOCUMENTATION.md#start-stop-and-delete-services) - Starts, Stops, or Deletes service(s).
* [**updateTimouts**](https://github.com/djarrard/Python-AGS-Admin/blob/master/FUNCTION%20DOCUMENTATION.md#update-timeouts) - Updates Maximum Wait Time, Maximum Startup Time, Maximum Idle Time, and Maximum Usage time parameters for service(s).
* [**backupSite**](https://github.com/djarrard/Python-AGS-Admin/blob/master/FUNCTION%20DOCUMENTATION.md#backup-site-requires-arcgis-for-server-102-and-higher) - Performs a backup of the ArcGIS Server site (ArcGIS for Server 10.2 or higher required).

This package ships with the [Requests](http://docs.python-requests.org/en/latest/) module to facilitate the Get and Post requests executed by the functions.



## Instructions and Notes

1. Download the repository ZIP file.
2. Refer to the [Samples](https://github.com/djarrard/Python-AGS-Admin/blob/master/SAMPLES.md) page and [Function Documentation](https://github.com/djarrard/Python-AGS-Admin/blob/master/FUNCTION%20DOCUMENTATION.md) page for guidance
3. Deploy the samples against a development/test server. **Do not execute these scripts against a production server     until they have been fully vetted against atesting-tier server**
4. Keep in mind that the Requests folder and adminfunctions.py file must reside in the same folder as scripts that use them unless they are copied to the python libraries on the machine or the environment variables are set to look for these libraries in their remote location.
5. The [backupSite](https://github.com/djarrard/Python-AGS-Admin/blob/master/FUNCTION%20DOCUMENTATION.md#backup-site-requires-arcgis-for-server-102-and-higher) function or another site backup method should be incorporated into any script that makes sweeping administrative changes so that it can be recovered should something go wrong.

## Requirements

* A network connection between the client machine and the GIS server.
* A named user on the ArcGIS for Server site with Administrative privileges.
* A python editor

## Issues

I'd like to expand upon this framework to include other administrative tasks. If you find or bug or think of a feature you'd like to see, please let me know by submitting an issue.

## Contributing

I follow the Esri Github guidelines for contributing. Please see [guidelines for contributing](https://github.com/esri/contributing).

## Licensing

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at


   http://www.apache.org/licenses/LICENSE-2.0


Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


A copy of the license is available in the repository.
