import datetime
import random


def find_workers_available_for_time(open_time:datetime.datetime) -> list[str]:
    workers = worker_database.get_all_workers()
    available_workers = [worker for worker in workers
                            if is_available(worker)]
    if available_workers:
        return available_workers

    # fall back to emergency workers
    # who listed they are available
    # in an emergency
    emergency_workers = [worker for worker in get_emergency_workers()
                            if is_available(worker)]
    if emergency_workers:
        return emergency_workers

    # Schedule the owner to open, they will find someone else
    return [OWNER]
    pass

def schedule_restaurant_open(open_time: datetime.datetime,
                            workers_needed: int):

    workers = find_workers_available_for_time(open_time)
    # use random.sample to pick X available workers
    # where X is the number of workers needed
    for worker in random.sample(workers, workers_needed):
        worker.schedule(open_time)



# Annotating Variables
workers: list[str] = find_workers_available_for_time(open_time)
numbers: list[int] = []
ratio: float = get_ratio(5,3)
number: int = 0
text: str = "useless"
values: list[float] = [1.2, 3.4, 6.0]
worker: Worker = Worker()
