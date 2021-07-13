from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from stock import HandleStock

class StockItem(BaseModel):
    name: str
    shares: int
    price: Optional[float] = 100


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello data-scientists"}


@app.post("/{name}")
def hello(name):
    return f"Hello {name}"


@app.get("/power/{x}")
def power(x: int):
    return x ** x


##get post put delete

## path parameters
@app.get("/stock/{id}")
def get_stock_detail(id: int):
    hs = HandleStock(id=id)
    res = hs.get_analysis()
    return res


##query parameters
@app.get("/stock")
def get_stock_with_query_params(stock_industry: int = None):
    if not stock_industry:
        return [{"stock_id": i} for i in range(10)]
    elif stock_industry in [1, 2, 3, 4]:
        return [{"stock_id": i} for i in range(4)]
    else:
        return []


## Request Body
@app.post("/stock/buy")
def buy_stock(item: StockItem):

    return {
        "stock_name": item.name,
        "shares": item.shares,
        "price": item.price,
        "total_price": item.shares * item.price,
    }
