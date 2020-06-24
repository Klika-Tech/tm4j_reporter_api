from typing import List, Dict

import requests

from configuration.configuration import CONFIG
from tm4j_exceptions import tm4j_response_exceptions

TM4J_API_URL = CONFIG.tm4j_api_url
PROJECT_KEY = CONFIG.project_key
AUTH_HEADER = {"Authorization": f"Bearer {CONFIG.api_access_key}"}


def create_test_cycle(
    test_cycle_name: str,
    *,
    description: str = None,
    planned_start_date: str = None,
    planned_end_date: str = None,
    jira_project_version: int = None,
    status_name: str = None,
    folder_id: int = None,
    owner_id: str = None,
) -> str:
    """
    Creates TM4J test cycle from name

    :param test_cycle_name: Name of test run
    :type test_cycle_name: str

    :param description: Description of the test cycle outlining the scope
    :type description: str

    :param planned_start_date: Planned start date of the test cycle. Format: yyyy-MM-dd'T'HH:mm:ss'Z'
    :type planned_start_date: str

    :param planned_end_date: Planned end date for the test cycle. Format: yyyy-MM-dd'T'HH:mm:ss'Z'
    :type planned_end_date: str

    :param jira_project_version: ID of the version from Jira
    :type jira_project_version: int
    
    :param status_name: Name of a status configured for the project
    :type status_name: int
    
    :param folder_id: ID of a folder to place the test cycle within
    :type folder_id: int
    
    :param owner_id: Atlassian Account ID of the owner of the test cycle
    :type owner_id: str

    :return: TM4J test cycle key
    :rtype str
    """
    payload = {
        "projectKey": PROJECT_KEY,
        "name": test_cycle_name,
        "description": description,
        "plannedStartDate": planned_start_date,
        "plannedEndDate": planned_end_date,
        "jiraProjectVersion": jira_project_version,
        "statusName": status_name,
        "folderId": folder_id,
        "ownerId": owner_id,
    }

    response = requests.post(
        url=f"{TM4J_API_URL}/testcycles", json=payload, headers=AUTH_HEADER
    )

    tm4j_response_exceptions.check_tm4j_api_response(response=response)

    return response.json()["key"]


def create_test_execution_result(
    test_cycle_key: str,
    test_case_key: str,
    execution_status: str,
    *,
    test_script_results: List[Dict[str, str]] = None,
    actual_end_date: str = None,
    environment_name: str = None,
    execution_time: int = None,
    executed_by_id: str = None,
    assigned_to_id: str = None,
    comment: str = None,
) -> None:
    """
    Creates test result for particular test case in test run

    :param test_cycle_key: Key of TM4J test cycle to put test execution to
    :type test_cycle_key: str

    :param test_case_key: Key of test case the execution applies to
    :type test_case_key: str

    :param execution_status: Name of the Test Execution Status
    :type execution_status: str
    
    :param test_script_results: List of objects with test steps results: 
        statusName (str), actualEndDate (str, yyyy-MM-dd'T'HH:mm:ss'Z'), actualResult (str)
    :type test_script_results: List[Dict[str, str]]
    
    :param actual_end_date: Date test was executed. Format: yyyy-MM-dd'T'HH:mm:ss'Z'
    :type actual_end_date: str
    
    :param environment_name: Environment assigned to the test case
    :type environment_name: str
    
    :param execution_time: Actual execution time in milliseconds
    :type execution_time: int
    
    :param executed_by_id: Atlassian Account ID of the user who executes the test
    :type executed_by_id: str
    
    :param assigned_to_id: Atlassian Account ID of the user assigned to the test
    :type assigned_to_id: str

    :param comment: Comment against the overall test execution
    :type comment: str

    :return: None
    :rtype: None
    """
    payload = {
        "projectKey": PROJECT_KEY,
        "testCaseKey": test_case_key,
        "testCycleKey": test_cycle_key,
        "statusName": execution_status,
        "testScriptResults": test_script_results,
        "environmentName": environment_name,
        "actualEndDate": actual_end_date,
        "executionTime": execution_time,
        "executedById": executed_by_id,
        "assignedToId": assigned_to_id,
        "comment": comment,
    }

    response = requests.post(
        url=f"{TM4J_API_URL}/testexecutions", json=payload, headers=AUTH_HEADER
    )

    tm4j_response_exceptions.check_tm4j_api_response(response=response)

    return None
