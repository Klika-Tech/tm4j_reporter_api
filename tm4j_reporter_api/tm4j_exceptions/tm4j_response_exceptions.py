# Copyright (C) 2020 Klika Tech, Inc. or its affiliates.  All Rights Reserved.
# Use of this source code is governed by an MIT-style license that can be found in the LICENSE file
# or at https://opensource.org/licenses/MIT.

import requests


class TM4JResponseException(Exception):
    """
    Class to represent unsuccessful TM4J API operations
    """

    def __init__(self, message):
        self.message = message


def check_tm4j_api_response(response: requests.models.Response, expected_status_code: int = 201) -> None:
    """
    Checking response from TM4J API

    :param response: requests response object
    :type response: requests.models.Response

    :param expected_status_code: expected response status code, 201 by default
    :type expected_status_code: int

    :raise TM4JResponseException: raised if actual response status code doesn't match to expected

    :return: None
    :rtype: None
    """
    try:
        assert response.status_code == expected_status_code
    except AssertionError:
        raise TM4JResponseException(f"Response status code: {response.status_code}, response message: {response.text}")

    return None
