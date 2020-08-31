# Copyright (C) 2020 Klika Tech, Inc. or its affiliates.  All Rights Reserved.
# Use of this source code is governed by an MIT-style license that can be found in the LICENSE file
# or at https://opensource.org/licenses/MIT.

class TM4JConfiguration(object):
    """
    Main TM4J reporter API configuration object.
    """

    def __init__(self, api_access_key, project_key):
        self.api_access_key = api_access_key
        self.project_key = project_key
