from adaptavist import Adaptavist

# TODO: configuration of JIRA credentials
TM4J = Adaptavist(jira_server, jira_username, jira_password)


def create_test_run(test_run_name: str, test_cases: list) -> str:
    """
    Creates TM4J test run from name and list of test cases

    :param test_run_name: name of test run
    :type test_run_name: str

    :param test_cases: list of TM4J test case keys
    :type test_cases: list

    :return: TM4J test run key
    :rtype str
    """
    # TODO: need to understand how to configure project key - static or dynamic
    return TM4J.create_test_run(
        project_key, test_run_name, test_cases=test_cases
    )


def create_test_execution_result(
    test_run_key: str, test_case_key: str, status: str, **kwargs
) -> None:
    """
    Creates test result for particular test case in test run

    :param test_run_key: TM4J key of test run
    :type test_run_key: str

    :param test_case_key: TM4K key of test case
    :type test_case_key: str

    :param status: test execution result, e.g. "Fail"
    :type status: str

    :param kwargs: Arbitrary list of keyword arguments
                comment: comment to add
                execute_time: execution time in seconds. ex. "5"
                environment: environment to distinguish multiple executions (call get_environments() to get a list of available ones)
                issue_links: list of issue keys to link the test result to

    :return: None
    :rtype: None
    """
    # TODO: think about exceptions
    TM4J.create_test_result(test_run_key, test_case_key, status, **kwargs)
    # TODO: should we consider to return ID of test execution result?
    return None


def create_test_execution_results(
    test_run_key: str,
    results: list,
    exclude_existing_test_cases: bool,
    **kwargs
) -> None:
    """
    Creates test execution results for multiple test cases in test run

    :param test_run_key: TM4J key of test run
    :type test_run_key: str

    :param results: list of key-value pairs of TM4J test case keys and its execution results
    :type results: list of {"testCaseKey": str, "result": str} objects

    :param exclude_existing_test_cases: if true, creates test results only for new test cases (can be used to add test cases to existing test runs)
                                        if false, creates new test results for existing test cases as well
    :type exclude_existing_test_cases: bool

    :param kwargs: Arbitrary list of keyword arguments
                environment: environment to distinguish multiple executions (call get_environments() to get a list of available ones)
                             sets environment field for all test cases
    :return: None
    :rtype: None
    """
    # TODO: think about exceptions
    TM4J.create_test_results(
        test_run_key, results, exclude_existing_test_cases, **kwargs
    )
    # TODO: should we consider to return list of test execution results IDs?
    return None
