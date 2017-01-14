from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin_content_error import DustbinContentError


class Dustbin:
    def __init__(self, color, plastic_content=None, paper_content=None, house_waste_content=None):
        self.color = color
        self.plastic_content = plastic_content or []
        self.paper_content = paper_content or []
        self.house_waste_content = house_waste_content or []

    def throw_out_garbage(self, garbage):
        if isinstance(garbage, Garbage):
            if isinstance(garbage, PlasticGarbage):
                if garbage.is_clean:
                    self.plastic_content.append(garbage)
                else:
                    raise DustbinContentError
            elif isinstance(garbage, PaperGarbage):
                if garbage.is_squeezed:
                    self.paper_content.append(garbage)
                else:
                    raise DustbinContentError
            else:
                self.house_waste_content.append(garbage)
        else:
            raise DustbinContentError

    def empty_contents(self):
        self.plastic_content = []
        self.paper_content = []
        self.house_waste_content = []
