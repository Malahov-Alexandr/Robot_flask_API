*** Settings ***
Library	RequestsLibrary
Library  Process
Library    Telnet
Variables	../endpoints/URL_and_endpoints.py
Resource    ../Templates/GET_tamplates.robot
Variables	../../flask/data/data_for_response.py
Library    perfomance.py
#create a set up method to start the flas app



*** Variables ***
${endpointForPerdomance} = 	people
${output} = 	${EMPTY}


*** Keywords ***
Validation Of Json
#This keyword is used to validate the response of the GET request
	[Arguments]   ${endpoint}  ${expected_json}	 ${id}  ${code}
	${validResponse} =    SendGetRequest    ${URL}	${endpoint}   ${id}
	Log To Console     Status code is ${validResponse.status_code}
	${status_for_response} =    Evaluate    int(${code})
	Should Be Equal As Integers    ${validResponse.status_code}    ${status_for_response}
	Should Be Equal    ${validResponse.json()} 	${expected_json}
	Log To Console    Test with ${endpoint} and id ${id} passed

StartApplication
	Run Process    python3    ../../flask/start.py   shell=True   cwd=../../flask


StopApplication
	Run Process    python3    ../../flask/stop.py  shell=True   cwd=../../flask


*** Test Cases ***
Start Server
	StartApplication
	Sleep    3s

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



*** Test Cases ***
Perfomace test
	perfomance.Run Performance Test		${endpointForPerdomance}	10

*** Test Cases ***
Stop Server
	StopApplication
















