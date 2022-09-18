# Global imports 
from dataclasses import dataclass
import pandas as pd
import json
# Local imports
from project.data.classes import MyInput

# Input/Output pipe to process data from input source
class Pipe(object):
    def __init__(self):
        # Set Output Format (JSON vs MyOuputObject)
        # NOTE Workers may break if setting changes
        self.output_type = "JSON"
    
    def output(self, input_obj: dataclass):
        if self.output_type is "JSON":
            return self.out_json(input_obj)
        return input_obj
    
    # TODO add read_csv

    def read_json(self, json_string: str) -> MyInput:
        if not type(json_string) is str:
            raise TypeError("Input must be JSON data as a string")
        json_obj = json.loads(json_string)
        # Check Types of Input
        if not self.correct_type(json_obj, int):
            raise TypeError("Input(s) must be an int")
        try:
            result = MyInput(num_intervals=json_obj["num_intervals"], 
                            interval_start=json_obj["interval_start"],
                            interval_end=json_obj["interval_end"],
                            percision=json_obj["percision"])
        except:
            raise Exception("Unable to create MyInput Object")
        return result
        

    @staticmethod
    def correct_type(input: dict, in_type: type) -> bool:
        for value in input.values(): 
            if(type(value) is not in_type): 
                return False
        return True

    # Wrapper in case custom to_json is needed
    @staticmethod
    def out_json(in_dataclass: dataclass) -> str:
        return in_dataclass.to_json()
