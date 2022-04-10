
@property
class Product:

    def __init__(self,
                 brand : str,
                 name : str,
                 volumes : list,
                 range : str,
                 description : str,
                 niche : str,
                 popularity : int,
                 category : str,
                 solves : list,
                 image_urls : list):

        self.brand = brand
        self.name = name
        self.volumes = volumes
        self.range = range
        self.description = description
        self.niche = niche
        self.popularity = popularity
        self.category = category
        self.solves = solves
        self.image_urls = image_urls
