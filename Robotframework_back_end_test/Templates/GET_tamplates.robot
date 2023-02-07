*** Settings ***
Library	RequestsLibrary
Library    requests


*** Keywords ***
SendGetRequest
# this keyword is used to send a GET request to the specified endpoint
# it returns the response object
    [Arguments]    ${url}  ${endpoint}  ${id}
    Create Session    mysession  ${url}
    ${response} =  GET On Session  mysession	${endpoint}/${id}/   expected_status=any
    ${status_code} =  Convert To String    ${response.status_code}
	Log To Console    ${status_code}
   	[Return]  ${response}


