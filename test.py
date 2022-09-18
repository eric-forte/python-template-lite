# Global import
import logging
import json
# Local import
from project.tasks import my_fxn
from project.data.io import Pipe

# Setup logger 
logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format=logFormatter, level=logging.INFO)
logger = logging.getLogger(__name__)

# Setup IO Pipe 
my_pipe = Pipe()

# TODO generate multiple JSONs
# TODO Generate random numbers
x = [10,0,100,50]
test_json = "{" + f"\"num_intervals\":{x[0]}, \"interval_start\":{x[1]}, \"interval_end\":{x[2]}, \"percision\":{x[3]}" + "}"

res = my_fxn.delay(test_json)
task_result = res.get(timeout=10)
logger.info(task_result)

# TODO Get worker function results 

logger.info('tests completed')




