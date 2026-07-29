from __future__ import annotations

from system_check import SystemCheck


class FinalTest:
    """
    Sino Builder AI
    Final Integration Test
    Release V1
    """

    def run(self):

        result = SystemCheck().run()

        return {

            "final_status":
                result["status"],

            "errors":
                result["errors"],

            "system":
                result["application"],

        }


if __name__ == "__main__":

    output = FinalTest().run()

    print(output)
