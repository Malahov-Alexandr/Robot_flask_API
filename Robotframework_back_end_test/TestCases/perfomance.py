import random
import time
import statistics
import requests


def run_performance_test(endpoint, id=1):
    """This function perfomance test of the API.
    It takes the endpoint and id as parameters.
    The default id is 1.
    The function returns the results of perfomance test into the file results_of_perfomance.txt
    """
    start_time = time.time()
    response_times = []
    # the time of perfomance test has been increased to 10 seconds to do not overload the RAM
    while time.time() - start_time < 30:
        response = requests.get(f"http://127.0.0.1:5000/{endpoint}/{id}/")
        response_time = response.elapsed.total_seconds()
        response_times.append(response_time)
        print(f"Response time: {response_time}")
        # the time sleep has been increased to 4 seconds to do not overload the RAM
        time.sleep(random.uniform(0, 4))
        print('Tic-Tock')
    with open("results_of_perfomance.txt", "w") as file:
            file.write(f"Number of requests: {len(response_times)}\n")
            file.write(f"Average response time: {statistics.mean(response_times)}\n")
            file.write(f"Median response time: {statistics.median(response_times)}\n")
            file.write(f"Max response time: {max(response_times)}\n")
            file.write(f"Min response time: {min(response_times)}\n")
    return "results were saved into results_of_perfomance.txt"



