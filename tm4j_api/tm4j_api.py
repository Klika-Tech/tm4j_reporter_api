import requests

from configuration.configuration import CONFIG


TM4J_API_URL = CONFIG.tm4j_api_url
PROJECT_KEY = CONFIG.project_key
AUTH_HEADER = {"Authorization": f"Bearer {CONFIG.api_access_key}"}


def create_test_cycle(test_cycle_name: str, **kwargs) -> str:
    """
    Creates TM4J test cycle from name

    :param test_cycle_name: Name of test run
    :type test_cycle_name: str

    :param kwargs: Arbitrary keyword arguments
        :Keyword Arguments:
        :keyword description (str): Description of the test cycle outlining the scope.
        :keyword plannedStartDate (str): Planned start date of the test cycle. Format: yyyy-MM-dd'T'HH:mm:ss'Z'
        :keyword plannedEndDate (str): Planned end date for the test cycle. Format: yyyy-MM-dd'T'HH:mm:ss'Z'
        :keyword jiraProjectVersion (int): ID of the version from Jira.
        :keyword statusName (str): Name of a status configured for the project.
        :keyword folderId (int): ID of a folder to place the test cycle within.
        :keyword ownerId (str): Atlassian Account ID of the owner of the test cycle.

    :return: TM4J test cycle key
    :rtype str
    """
    payload = {"projectKey": PROJECT_KEY, "name": test_cycle_name}

    # TODO: key/type checks?
    if kwargs:
        payload.update(kwargs)

    # TODO: think about exceptions
    response = requests.post(
        url=f"{TM4J_API_URL}/testcycles", json=payload, headers=AUTH_HEADER
    )

    return response.json()["key"]


def create_test_execution_result(
    test_cycle_key: str, test_case_key: str, execution_status: str, **kwargs
) -> None:
    """
    Creates test result for particular test case in test run

    :param test_cycle_key: Key of TM4J test cycle to put test execution to
    :type test_cycle_key: str

    :param test_case_key: Key of test case the execution applies to
    :type test_case_key: str

    :param execution_status: Name of the Test Execution Status
    :type execution_status: str

    :param kwargs: Arbitrary keyword arguments
        :Keyword Arguments:
        :keyword testScriptResults (List[Dict[str, str]]): List of objects with test steps results:
                    statusName (str), actualEndDate (str, yyyy-MM-dd'T'HH:mm:ss'Z'), actualResult (str).
        :keyword actualEndDate (str): Date test was executed. Format: yyyy-MM-dd'T'HH:mm:ss'Z'
        :keyword environmentName (str): Environment assigned to the test case.
        :keyword executionTime (int): Actual execution time in milliseconds.
        :keyword executedById (str): Atlassian Account ID of the user who executes the test.
        :keyword assignedToId (str): Atlassian Account ID of the user assigned to the test.
        :keyword comment (str): Comment against the overall test execution.

    :return: None
    :rtype: None
    """
    payload = {
        "projectKey": PROJECT_KEY,
        "testCycleKey": test_cycle_key,
        "testCaseKey": test_case_key,
        "statusName": execution_status,
    }

    # TODO: key/type checks?
    if kwargs:
        payload.update(kwargs)

    # TODO: think about exceptions
    requests.post(
        url=f"{TM4J_API_URL}/testexecutions", json=payload, headers=AUTH_HEADER
    )

    return None
