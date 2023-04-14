from datetime import datetime

from dateutil import parser

from pytz import timezone
from langchain.tools import BaseTool

class RenewLicense(BaseTool):
    name = "Renew License"
    description = "Use this tool to renew a license"

    def _run(self, query: str) -> str:
        print(query)
        return "FAKE API: License renew"

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("RenewLicense does not support async")

class CancelLicense(BaseTool):
    name = "Cancel License"
    description = "Use this tool to cancel a license"

    def _run(self, query: str) -> str:
        print(query)
        return "FAKE API: License cancel"

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("CancelLicense does not support async")
    