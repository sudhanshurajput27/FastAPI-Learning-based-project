from pydantic import BaseModel

class IrisData(BaseModel):
    feature1 : float
    feature2 : float
    feature3 : float    
    feature4 : float