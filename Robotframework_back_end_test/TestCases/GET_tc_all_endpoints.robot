*** Settings ***
Variables	../endpoints/URL_and_endpoints.py


*** Keywords ***
GET request
	[Arguments]    ${URL}   ${endpoint}
	cr   ${URL}    ${endpoint}


*** Test Cases ***
test
	crea sessione