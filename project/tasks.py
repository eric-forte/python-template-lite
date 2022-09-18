# Global imports
from mpmath import mp
from timeit import default_timer as timer
# Local imports
from project.celery import app
from project.data.io import Pipe
from project.data.classes import MyOutput

@app.task
def calc_pi(input_json: str) -> str:
    my_pipe = Pipe()
    # Cast to dataclass 
    my_input = my_pipe.read_json(input_json)
    mp.dps = my_input.percision
    # Gaussian integral method 
    return str(mp.quad(lambda x: mp.exp(-x**2), [-mp.inf, mp.inf]) ** 2)

@app.task
def my_fxn(input_json: str) -> MyOutput:
    my_pipe = Pipe()
    # Cast to dataclass 
    my_input = my_pipe.read_json(input_json)
    # Timer is not concerned with IO 
    start = timer()
    mp.dps = my_input.percision
    # Integrate sin(x) with supplied parameters
    result = str(mp.quad(mp.sin, mp.linspace(my_input.interval_start, my_input.interval_end, my_input.num_intervals)))
    end = timer()
    cmp_time = str(end - start)
    
    return my_pipe.output(MyOutput(result=result,compute_time=cmp_time,percision=my_input.percision))
