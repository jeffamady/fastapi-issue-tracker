from fastapi import FastAPI

app = FastAPI()

items = [
    {
        "id": 1,
        "name": "Item 1",
        "description": "This is item 1",
    },
    {
        "id": 2,
        "name": "Item 2",
        "description": "This is item 2",
    },
    {
        "id": 3,
        "name": "Item 3",
        "description": "This is item 3",
    },
]


@app.get("/check")
def quick_check():
    return {"message": "Quick check passed!"}


@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"message": "Item not found"}


@app.post("/items")
def create_item(item: dict):
    new_id = max(item["id"] for item in items) + 1
    item["id"] = new_id
    items.append(item)
    return item
