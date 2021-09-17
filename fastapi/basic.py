from typing import Optional

from fastapi import FastAPI, Path, Query
import uvicorn

# Uvicorn is a lightning-fast ASGI server implementation
# Starlette is a lightweight asyncio ASGI framework/toolkit
# pydantic enforces type hints at runtime, with friendly errors when data is invalid
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int = Path(None, example="item_id_value"),
              q: str = Query("query")):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    uvicorn.run('basic:app', host='0.0.0.0', reload=True)
