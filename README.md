# Project summary
Package providing TM4J Cloud REST API for test automation integration.

# Install
## How to build
    python setup.py sdist
    
## How to install
    # PyPi
    pip install tm4j-reporter-api
    # Git
    pip install git+https://github.com/Klika-Tech/tm4j_reporter_api.git
    
# Configure
In order to use TM4J Cloud REST API, you need to configure TM4J reporter with `tm4j_api.configure_tm4j_api` function first:
```python
from tm4j_reporter_api import tm4j_api


def my_test_run_setup(my_access_key, my_project_key):

    tm4j_api.configure_tm4j_api(
        api_access_key=my_access_key,
        project_key=my_project_key
    )
```
| Param          | Mandatory | Description                                                                                                                                            | Type | Example |
|----------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|------|---------|
| api_access_key | Yes       | API key to access TM4j. To get it see [Instruction](https://support.smartbear.com/tm4j-cloud/docs/api-and-test-automation/generating-access-keys.html) | str  |         |
| project_key    | Yes       | Jira / TM4J project prefix without trailing dash                                                                                                       | str  | QT      |

# Usage
## Test cycle
You need TM4J test cycle where to submit test execution results.
You could create new TM4J test cycle in your test run setup in order to use its key for test execution results submitting with `tm4_api.create_test_cycle` function:
```python
from tm4j_reporter_api import tm4j_api


def my_test_run_setup():

    tm4j_test_cycle_key = tm4j_api.create_test_cycle(
        test_cycle_name="My TM4J test cycle"    
    )

    return tm4j_test_cycle_key
```
| Param                | Mandatory | Description                                                            | Type | Example                              |
|----------------------|-----------|------------------------------------------------------------------------|------|--------------------------------------|
| test_cycle_name      | Yes       | Name of your test cycle                                                | str  | My TM4J test cycle                   |
| description          | No        | Description of the test cycle outlining the scope                      | str  | Some feature test run                |
| planned_start_date   | No        | Planned start date of the test cycle. Format: yyyy-MM-dd'T'HH:mm:ss'Z' | str  | 2020-07-15'T'12:00:00'Z'             |
| planned_end_date     | No        | Planned end date for the test cycle. Format: yyyy-MM-dd'T'HH:mm:ss'Z'  | str  | 2020-07-15'T'12:30:00'Z'             |
| jira_project_version | No        | ID of the version from Jira                                            | int  | 1000                                 |
| status_name          | No        | Name of a status configured for the project                            | str  | Done                                 |
| folder_id            | No        | ID of a folder to place the test cycle within                          | int  | 10001                                |
| owner_id             | No        | Atlassian Account ID of the owner of the test cycle                    | str  | 377441B7-835D-4B08-B7F4-219E9E62C015 |

## Test execution results
With TM4J test cycle key you can now submit test execution result. You also could use test cycle key of already existing TM4J test cycle if you want.
Pass test cycle key and test execution results to `tm4j_api.create_test_execution_result` function:
```python
from tm4j_reporter_api import tm4j_api

def my_test_teardown(tm4_test_cycle_key, tm4j_test_case_key, execution_status):
    
    tm4j_api.create_test_execution_result(
        test_cycle_key=tm4_test_cycle_key,
        test_case_key=tm4j_test_case_key,
        execution_status=execution_status    
    )
```
| Param               | Mandatory | Description                                                                                                                                                                                        | Type | Example                                                                                                                                                                                                            |
|---------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_cycle_key      | Yes       | Key of TM4J test cycle to put test execution to                                                                                                                                                    | str  | TIS                                                                                                                                                                                                                |
| test_case_key       | Yes       | Key of test case the execution applies to                                                                                                                                                          | str  | SA-T10                                                                                                                                                                                                             |
| execution_status    | Yes       | Name of the Test Execution Status                                                                                                                                                                  | str  | Pass                                                                                                                                                                                                               |
| test_script_results | No        | List of objects with test steps results: statusName (str), actualEndDate (str, yyyy-MM-dd'T'HH:mm:ss'Z'), actualResult (str). Number of objects should match to steps number in TM4J test script.  | list | [{"statusName": "Pass", "actualEndDate": "2020-07-15'T'12:30:00'Z'", "actualResult": "This step passed"}, {"statusName": "Fail", "actualEndDate": "2020-07-15'T'12:30:10'Z'", "actualResult": "This step failed"}] |
| actual_end_date     | No        | Date test was executed. Format: yyyy-MM-dd'T'HH:mm:ss'Z'                                                                                                                                           | str  | 2020-07-15'T'12:30:00'Z'                                                                                                                                                                                           |
| environment_name    | No        | Environment assigned to the test case                                                                                                                                                              | str  | Staging                                                                                                                                                                                                            |
| execution_time      | No        | Actual execution time in milliseconds                                                                                                                                                              | int  | 121000                                                                                                                                                                                                             |
| executed_by_id      | No        | Atlassian Account ID of the user who executes the test                                                                                                                                             | str  | 377441B7-835D-4B08-B7F4-219E9E62C015                                                                                                                                                                               |
| assigned_to_id      | No        | Atlassian Account ID of the user assigned to the test                                                                                                                                              | str  | 377441B7-835D-4B08-B7F4-219E9E62C015                                                                                                                                                                               |
| comment             | No        | Comment against the overall test execution                                                                                                                                                         | str  | Test failed on step 2, check with Dev team                                                                                                                                                                         |

# Exceptions
## TM4JConfigurationException
Raised by `tm4j_api.configure_tm4j_api` and `tm4j_api.create_test_execution_result` functions if `tm4j_api.configure_tm4j_api` function was not called before:
```bash
tm4j_reporter_api.tm4j_exceptions.tm4j_configuration_exceptions.TM4JConfigurationException: You must configure TM4J reporter API before calling TM4J, call tm4j_api.configure_tm4j_api method first
```

## TM4JResponseException
Raised by `tm4j_api.configure_tm4j_api` and `tm4j_api.create_test_execution_result` functions if TM4J Cloud responded with response status code different from `201 Created`:
```bash
tm4j_reporter_api.tm4j_exceptions.tm4j_response_exceptions.TM4JResponseException: Response status code: 400, response message: Bad Request
```