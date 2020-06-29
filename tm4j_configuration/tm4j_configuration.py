import os


class TM4JConfiguration(object):
    """
    Main configuration object.
    Requires API_ACCESS_KEY, TM4J_API_URL, PROJECT_KEY to be defined in environment.
    """

    def __init__(self):
        self._check_required_keys_exist()
        self.api_access_key = os.environ["API_ACCESS_KEY"]
        self.tm4j_api_url = os.environ["TM4J_API_URL"]
        self.project_key = os.environ["PROJECT_KEY"]

    @staticmethod
    def _check_required_keys_exist():
        """
        Checks if required API_ACCESS_KEY, TM4J_API_URL, PROJECT_KEY exist in environment variables.

        :raise NameError: raised if any of required keys is missing

        :return: None
        :rtype: None
        """
        missing_keys = []
        for key in ["API_ACCESS_KEY", "TM4J_API_URL", "PROJECT_KEY"]:
            try:
                os.environ[key]
            except KeyError as e:
                missing_keys.append(e.args[0])
        if missing_keys:
            raise NameError(f"Environment variables missing: {' ,'.join(missing_keys)}")

        return None


CONFIG = TM4JConfiguration()
