from CONSTANTS import SECRETS, CONSTANTS
from clients.mongo_utils import MongoUtils
from enitities.RequestFaceToProducts import RequestFaceToProducts
from utils.problems_from_face_analysis_result import ProblemsFromFaceAnalysisResult


class ProblemToProducts:

    def __init__(self, face_analysis_result : RequestFaceToProducts):
        self.face_analysis_result = face_analysis_result

        self.mong_util_obj =  MongoUtils()
        self.ProblemsFromFaceAnalysisResultObj = ProblemsFromFaceAnalysisResult(self.face_analysis_result)

    def query_builder_for_problem_and_niche(self, problems, niche):
        problems_json = {"$in" : problems}
        query = {"solves" : problems_json, "niche" : niche}
        return query

    def get_products_from_problem_and_niche(self, problem, niche):

        query = self.query_builder_for_problem_and_niche(problem, niche)
        result = self.mong_util_obj.get_document(query, SECRETS.COLLECTION_PRODUCTS)

        return result

    def get_problem_map_from_problem_names(self, problem_names):
        problems_map = {}
        for key in problem_names:
            problems_map[key] = CONSTANTS.PROBLEMS_CODE_FROM_NAME_MAP[key]


    def get_response(self):
        budget = self.face_analysis_result[CONSTANTS.BUDGET]
        problem_names = self.ProblemsFromFaceAnalysisResultObj.get_problems_from_face_analysis_result()
        problem_codes = [value for key, value in CONSTANTS.PROBLEMS_CODE_FROM_NAME_MAP.items() if key in problem_names]

        products = self.get_products_from_problem_and_niche(problem_codes,budget)
        return products

if __name__ == '__main__':

    ## Need to Whitelist IP first in MongoDB
    ## Example :
    request = { 'budget' : "premium",
          'pores_left_cheek': {'confidence': 0.84026295, 'value': 1},
          'nasolabial_fold': {'confidence': 0.33373865, 'value': 0},
          'eye_pouch': {'confidence': 0.9996973, 'value': 0},
          'forehead_wrinkle': {'confidence': 0.0090346215, 'value': 0},
          'skin_spot': {'confidence': 0.9966935, 'value': 1},
          'acne': {'confidence': 0.99947804, 'value': 1},
          'pores_forehead': {'confidence': 0.99127394, 'value': 0},
          'pores_jaw': {'confidence': 0.9071017, 'value': 0},
          'left_eyelids': {'confidence': 0.9283517, 'value': 1},
          'eye_finelines': {'confidence': 0.10976741, 'value': 0},
          'dark_circle': {'confidence': 0.99998, 'value': 0},
          'crows_feet': {'confidence': 0.00074191764, 'value': 0},
          'pores_right_cheek': {'confidence': 0.52230364, 'value': 0},
          'blackhead': {'confidence': 0.0057849204, 'value': 0},
          'glabella_wrinkle': {'confidence': 0.014744136, 'value': 0},
          'mole': {'confidence': 0.9990219, 'value': 1},
          'skin_type': {'details': {'0': {'confidence': 0.20793314, 'value': 0},
            '1': {'confidence': 4.9446102e-05, 'value': 0},
            '2': {'confidence': 0.7656414, 'value': 1},
            '3': {'confidence': 0.026376005, 'value': 0}},
           'skin_type': 2}
                }

    obj = ProblemToProducts(request)
    products  = obj.get_response()
    print( products )