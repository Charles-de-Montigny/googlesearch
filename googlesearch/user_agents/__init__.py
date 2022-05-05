import pandas as pd

USER_AGENTS_DF = pd.read_json("user_agents")

class UserAgents:

    def __init__(self, json_path: str = None) -> None:
        self.df: pd.DataFrame = pd.read_json(json_path) if json_path else USER_AGENTS_DF

    @staticmethod
    def _get(df, random_state: int = None) -> str:
        user_agents = df.sample(
            1, random_state=random_state
            )['user_agents'].values[0]
        return user_agents

    def get(self, random_state: int = None) -> str:
        """
        Get a random user agents.
        """
        return self._get(self.df, random_state)

    def get_by_device_or_os(self, device_or_os: str, random_state: int = None) -> str:
        """
        Get a random user agents for a given device.
        """
        df = self.df.query(f"{device_or_os} == 1")
        return self._get(df, random_state)