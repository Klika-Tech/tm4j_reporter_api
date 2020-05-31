import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TM4J Reporter API",
    description="python package providing functionality for Jira Test Management (tm4j) through Adaptavist API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="v0.1.0",
    url="https://gitlab.klika-tech.com/qa/tm4j_reporter_api",
    author="Yury Kuptsou",
    author_email="ykuptsou@klika-tech.com",
    license="MIT",
    packages=setuptools.find_packages(),
    platforms="any",
    python_requires=">=3.7",
    install_requires=["adaptavist"],
    keywords="python adaptavist tm4j jira test testmanagement report",
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
