*** Settings ***
Library	RequestsLibrary


*** Keywords ***
SendGetRequest
    [Arguments]    ${url}  ${endpoint}  ${params}=${None}  ${expected_json}=${None}
    Create Session    mysession   ${url}
    ${response} =  GET On Session	mysession	${endpoint}/${params}
	[Return]  ${response.json()}
