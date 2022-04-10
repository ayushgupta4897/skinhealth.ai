VALUE = "value"
CONFIDENCE = "confidence"
POSITIVE = 1
NEGATIVE = 0
SKIN_TYPE = "skin_type"
BUDGET = "budget"

SKIN_TYPE_MAPPING = {
    0 : "oily",
    1 : "dry",
    2 : "normal",
    3 : "mixed"
}

EXCEPTION_KEYS = [SKIN_TYPE, BUDGET]

PORES_LEFT_CHEEK = "pores_left_cheek"
NASOLABIAL_FOLD = "nasolabial_fold"
EYE_POUCH = "eye_pouch"
FOREHEAD_WRINKLE = "forehead_wrinkle"
SKIN_SPOT = "skin_spot"
ACNE = "acne"
PORES_FOREHEAD = "pores_forehead"
PORES_JAW = "pores_jaw"
LEFT_EYELIDS = "left_eyelids"
EYE_FINELINES = "eye_finelines"
DARK_CIRCLE = "dark_circle"
CROWS_FEET = "crows_feet"
PORES_RIGHT_CHEEK = "pores_right_cheek"
BLACKHEAD = "blackhead"
GLABELLA_WRINKLE = "glabella_wrinkle"
MOLE = "mole"
RIGHT_EYELIDS = "right_eyelids"

PROBLEMS_CODE_FROM_NAME_MAP = {

     ACNE : "PR1",
     SKIN_SPOT : "PR2",
     PORES_LEFT_CHEEK : "PR3",
     PORES_RIGHT_CHEEK : "PR4",
     PORES_FOREHEAD : "PR5",
     PORES_JAW : "PR6",
     BLACKHEAD : "PR7",
     EYE_POUCH : "PR8",
     FOREHEAD_WRINKLE : "PR9" ,
     LEFT_EYELIDS : "PR10",
     EYE_FINELINES : "PR11",
     DARK_CIRCLE : "PR12",
     CROWS_FEET : " PR13",
     GLABELLA_WRINKLE : "PR14",
     MOLE : "PR15",
     RIGHT_EYELIDS : "PR16",
     NASOLABIAL_FOLD : "PR17"

}








# {
#   "sku_code": "SKH00001",
#   "brand": "The Derma co",
#   "name": "10% niacinamide serum",
#   "volumes": [30],
#   "range": "mid",
#   "description": "Niacinamide is an anti-inflammatory that works to regulate the amount of acne-causing oil being produced by the glands in your skin. In addition, it regulates skin tone and helps fade the red, purple and brown marks that acne can leave on the skin.",
#   "niche": "premium",
#   "popularity": 87,
#   "category": "serum",
#   "solves": ["PR1"]
# }