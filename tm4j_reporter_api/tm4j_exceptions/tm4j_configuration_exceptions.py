# Copyright (C) 2020 Klika Tech, Inc. or its affiliates.  All Rights Reserved.
# Use of this source code is governed by an MIT-style license that can be found in the LICENSE file
# or at https://opensource.org/licenses/MIT.

class TM4JConfigurationException(Exception):
    """
    Class to represent TM4J configuration exceptions
    """

    def __init__(self, message):
        self.message = message
