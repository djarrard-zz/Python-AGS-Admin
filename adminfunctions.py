import requests, json

#### PLEASE SEE FUNCTION DOCUMENTATION FOR MORE INFORMATION ABOUT THESE FUNCTIONS ##

###Script Functions - These should not need to be modified OOTB.
def defineEndpoints(agsURL):
    base = agsURL.split(r"/rest")[0]
    REST = base + "/rest/services"
    adminAPI = base + "/admin"
    info = base + "/rest/info" 
    response = requests.get(info + "?f=json")
    jsonresponse = json.loads(response.text)
    tokenURL = jsonresponse["authInfo"]["tokenServicesUrl"]
    output = {"REST":REST,"TokenUrl":tokenURL,"Admin":adminAPI}
    return output

def getToken(tokenURL, username, password):
    token_POSTdata = {'username':username,'password':password,'f':"json"}
    token_request = requests.post(tokenURL, token_POSTdata, verify=False)
    token_response = json.loads(token_request.text)
    return token_response

def getServiceAdminEndpoints(adminURL, token):
    serviceList = []
    if token != "":
        tokenstring = "&token="+token
    else:
        tokenstring = ""
    crawl_URL = adminURL + "/services/?f=json" + tokenstring
    folders = []
    services = []
    serviceURLs = []
    request = requests.get(crawl_URL)
    response = json.loads(request.text)
    for item in response["services"]:
        serviceInfo = []
        serviceInfo.append(item["folderName"])
        serviceInfo.append(item["serviceName"])
        serviceInfo.append(item["type"])
        serviceList.append(serviceInfo)
    for folder in response["foldersDetail"]:
        if folder["isDefault"] == False:
            folders.append(folder["folderName"])
    for item in folders:
        url = adminURL +"/services/" + item + "/" + "?f=json" + tokenstring
        request = requests.get(url)
        response = json.loads(request.text)
        for item in response["services"]:
            serviceInfo = []
            serviceInfo.append(item["folderName"])
            serviceInfo.append("/" + item["serviceName"])
            serviceInfo.append(item["type"])
            serviceList.append(serviceInfo)
    urlList = []
    for item in serviceList:
        url = adminURL + "/services/" + item[0] + item[1] + "." + item[2]
        urlList.append(url)
    return urlList

def updateMinMaxInstance(serviceAdminUrl, token, minInstances, maxInstances):
    if token != "":
        tokenstring = "&token="+token
    else:
        tokenstring = ""
    requestURL = serviceAdminUrl + "?f=json" + tokenstring
    request = requests.get(requestURL)
    response = json.loads(request.text)
    response["minInstancesPerNode"] = minInstances
    response["maxInstancesPerNode"] = maxInstances
    newjson = json.dumps(response)
    editURL = serviceAdminUrl + "/edit" + "?f=json" + tokenstring
    postData = {"service":newjson}
    request = requests.post(editURL, postData)
    response = json.loads(request.text)["status"]
    return "Serviced update result: " + response
    
def StartStopDelete(serviceAdminUrl, token, operation):
    if token != "":
        tokenstring = "&token="+token
    else:
        tokenstring = ""
    if operation.upper() == "START":
        requestUrl = serviceAdminUrl + "/start" + "?f=json" + tokenstring
    elif operation.upper() == "STOP":
        requestUrl = serviceAdminUrl + "/stop" + "?f=json" + tokenstring
    elif operation.upper() == "DELETE":
        requestUrl = serviceAdminUrl + "/stop" + "?f=json" +tokenstring
    request = requests.post(requestUrl)
    response = json.loads(request.text)["status"]
    return "Result: " + response

def updateTimeouts(serviceAdminUrl, token, maxWaitTime, maxStartupTime, maxIdleTime, maxUsageTime):
    if token != "":
        tokenstring = "&token="+token
    else:
        tokenstring = ""
    defaultmaxWaitTime = 60
    defaultmaxStartupTime = 300
    defaultmaxIdleTime = 1800
    defaultmaxUsageTime = 600
    requestURL = serviceAdminUrl + "?f=json" + tokenstring
    request = requests.get(requestURL)
    response = json.loads(request.text)
    if maxWaitTime != "":
        newWaitTime = maxWaitTime
    else:
        newWaitTime = defaultmaxWaitTime 
    if maxStartupTime != "":
        newStartupTime = maxStartupTime
    else:
        newStartupTime = defaultmaxStartupTime 
    if maxIdleTime != "":
        newIdleTime = maxIdleTime
    else:
        newIdleTime = defaultmaxIdleTime
    if maxUsageTime != "":
        newUsageTime = maxUsageTime
    else:
        newUsageTime = defaultmaxUsageTime
    response["maxWaitTime"] = newWaitTime
    response["maxStartupTime"] = newStartupTime
    response["maxIdleTime"] = newIdleTime
    response["maxUsageTime"] = newUsageTime
    newjson = json.dumps(response)
    editURL = serviceAdminUrl + "/edit" + "?f=json" + tokenstring
    postData = {"service":newjson}
    request = requests.post(editURL, postData)
    response = json.loads(request.text)["status"]
    return "Serviced update result: " + response

def backupSite(adminUrl, token, outputDirectory):
    if token != "":
        tokenstring = "&token="+token
    else:
        tokenstring = ""
    compCheckUrl = adminUrl + "?f=json" + tokenstring
    compCheckRequest = requests.get(compCheckUrl)
    response = json.loads(compCheckRequest.text)
    if response["currentVersion"] >= 10.2:
        bkpUrl = adminUrl + "/exportSite"
        bkpPostData = {"f":"json","location":outputDirectory,"token":token}
        request = requests.post(bkpUrl, bkpPostData)
        response = json.loads(request.text)
        if response["status"] == "success":
            return {'outcome':"success",'messages':response["location"]}
        else:
            return {'outcome':"error",'messages':response["messages"]}
        return response
    else:
        return "This ArcGIS Server does not support the exportSite operation. 10.2 and higher is required."
