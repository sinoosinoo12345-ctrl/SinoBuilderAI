from concurrent.futures import ThreadPoolExecutor, as_completed


class ParallelExecution:

    def __init__(self):
        self.results = []

    def _run_task(self, task):

        agent = task["agent"]

        return {
            "agent": agent,
            "target": task["target"],
            "status": "completed"
        }

    def execute(self, tasks):

        self.results = []

        with ThreadPoolExecutor(max_workers=8) as executor:

            futures = [
                executor.submit(
                    self._run_task,
                    task
                )
                for task in tasks
            ]

            for future in as_completed(futures):
                self.results.append(
                    future.result()
                )

        return self.results
