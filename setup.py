# Copyright (C) 2020 Klika Tech, Inc. or its affiliates.  All Rights Reserved.
# Use of this source code is governed by an MIT-style license that can be found in the LICENSE file
# or at https://opensource.org/licenses/MIT.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tm4j-reporter-api",
    description="python package providing functionality for Jira Test Management (tm4j) Cloud through REST API calls",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="v0.1.2",
    url="https://github.com/Klika-Tech/tm4j_reporter_api",
    author="Klika-Tech, Inc",
    author_email="contact@klika-tech.com",
    license="MIT",
    packages=[
        "tm4j_reporter_api.tm4j_api", "tm4j_reporter_api.tm4j_configuration", "tm4j_reporter_api.tm4j_exceptions"
    ],
    platforms="any",
    python_requires=">=3.6",
    install_requires=["requests"],
    keywords="python tm4j jira test testmanagement report",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
