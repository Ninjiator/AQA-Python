from pydantic import BaseModel, HttpUrl


class ProductModel(BaseModel):
    id : int
    title : str
    price : float
    description : str
    category : str
    image: HttpUrl