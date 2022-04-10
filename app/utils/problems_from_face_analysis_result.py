from enitities.RequestFaceToProducts import RequestFaceToProducts
from collections import namedtuple
from CONSTANTS import SECRETS, CONSTANTS
import json


class ProblemsFromFaceAnalysisResult():

    def __init__(self, face_analysis_result):
        self.face_analysis_result = face_analysis_result

    def get_problems_from_face_analysis_result(self):
        problems = []
        for key,value in self.face_analysis_result.items():
            if( key not in CONSTANTS.EXCEPTION_KEYS and value[CONSTANTS.VALUE] == CONSTANTS.POSITIVE):
                problems.append(key)
        return problems

    def get_skin_type(self):
        if(CONSTANTS.SKIN_TYPE not in self.face_analysis_result.keys()):
            return -1
        skin_type =  self.face_analysis_result[CONSTANTS.SKIN_TYPE][CONSTANTS.SKIN_TYPE]
        return skin_type
