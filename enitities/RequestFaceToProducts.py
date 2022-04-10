from .ResultProblem import ResultProblem

@property
class RequestFaceToProducts:

    def __init__(self,
                 budget : str,
                 pores_left_cheek : ResultProblem,
                 nasolabial_fold : ResultProblem,
                 eye_pouch : ResultProblem,
                 forehead_wrinkle : ResultProblem,
                 skin_spot : ResultProblem,
                 acne : ResultProblem,
                 pores_forehead : ResultProblem,
                 pores_jaw : ResultProblem,
                 left_eyelids : ResultProblem,
                 eye_finelines : ResultProblem,
                 dark_circle : ResultProblem,
                 crows_feet : ResultProblem,
                 pores_right_cheek : ResultProblem,
                 blackhead : ResultProblem,
                 glabella_wrinkle : ResultProblem,
                 mole : ResultProblem,
                 skin_type : ResultProblem,
                 right_eyelids
                 ):
        self.budget = budget
        self.pores_left_cheek = pores_left_cheek
        self.nasolabial_fold = nasolabial_fold
        self.eye_pouch = eye_pouch
        self.forehead_wrinkle = forehead_wrinkle
        self.skin_spot = skin_spot
        self.acne = acne
        self.pores_forehead = pores_forehead
        self.pores_jaw = pores_jaw
        self.left_eyelids = left_eyelids
        self.eye_finelines = eye_finelines
        self.dark_circle = dark_circle
        self.crows_feet = crows_feet
        self.pores_right_cheek =  pores_right_cheek
        self.blackhead = blackhead
        self.glabella_wrinkle = glabella_wrinkle
        self.mole = mole
        self.skin_type = skin_type
        self.right_eyelids = right_eyelids
        
    