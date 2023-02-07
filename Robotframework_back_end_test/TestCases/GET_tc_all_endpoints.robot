*** Settings ***
Library	RequestsLibrary
Library    requests
Variables	../endpoints/URL_and_endpoints.py
Resource    ../Templates/GET_tamplates.robot
Variables	../../data/data_for_response.py


*** Keywords ***
JsonValidation
	[Arguments]    ${response}    ${expected_json}
	BuiltIn.Should Be Equal  ${response}    ${expected_json}


*** Test Cases ***
GetRequestForUsers
	${response}=    SendGetRequest    ${URL}	${people}  ${param}
	JsonValidation    ${response}    ${expected_json}

	|  ${param} |  ${expected_json} 	 |
	|  1  		 |  ${person}  	 	 |
	|  50  		 |  ${person}   	 	 |
	|  100  	 |  ${person}  	 	 |
	|  -1  		 |  ${less_than_0}  	 |
	|  0		 |  ${less_than_0}  	 |
	|  101  	 |  ${more_than_100}  	 |
	|  1000  	 |  ${more_than_100}  	 |
	|  test  	 |  ${must_be_int}  		 |
