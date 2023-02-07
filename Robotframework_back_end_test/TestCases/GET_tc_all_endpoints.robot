*** Settings ***
Library	RequestsLibrary
Variables	../endpoints/URL_and_endpoints.py
Resource    ../Templates/GET_tamplates.robot
Variables	../../data/data_for_response.py




*** Variables ***





*** Keywords ***
Validation Of Json
	[Arguments]   ${endpoint}  ${expected_json}	 ${id}  ${code}
	${validResponse} =    SendGetRequest    ${URL}	${endpoint}   ${id}
	Log To Console     Status code is ${validResponse.status_code}
	${status_for_response} =    Evaluate    int(${code})
	Should Be Equal As Integers    ${validResponse.status_code}    ${status_for_response}
	Should Be Equal    ${validResponse.json()} 	${expected_json}
	Log To Console    Test with ${endpoint} and id ${id} passed
	




*** Test Cases ***
GetRequestForUsersValidID
	Validation Of Json    ${people}  ${person}    		1	200
	Validation Of Json    ${planets}    ${planet}    	50	200
	Validation Of Json    ${starships}    ${cosmo_boat}	100	200

GetRequestForUsersInvalidID
	Validation Of Json    ${people}    ${more_than_100}    101	404
	Validation Of Json    ${planets}    ${less_than_0}    	0	404
	Validation Of Json    ${starships}    ${less_than_0}    -1	404
	Validation Of Json    ${planets}    ${error_500}    letter	500











