## What is pydantic?

- automatic data validation
- data seralization (when user sends JSON, Pydantic converts that to a python object against a defined model)

How to make a pydantic model:

```python
class Item(BaseModel):
    name: str
    description: str | None = None  # Optional string, defaults to None
    price: float
    tax: float | None = None
```

## How to use a pydantic model in FastAPI (or someplace else in normal python files):

- auto conversion to python object from dict
- conversion of data types within the object (like if user gives string "10", which is usually the case with JSON, pydantic will convert it to int in the object's property)
- if validation fails in a way it can't be corrected, auto raise a 422 Unprocessable Entity http error
- Just by using the pydantic model as type, you get autocomplete and type check by IDE

```python
@app.post("/items/")
async def create_item(item: Item):
    # 'item' is now a fully validated Python object, not just a raw dictionary

    # You can access attributes directly using dot notation
    total_price = item.price
    if item.tax:
        total_price += item.tax

    # Convert the Pydantic model back to a dictionary if needed
    item_dict = item.model_dump()
    item_dict["total_price"] = total_price

    return item_dict
```

## Pydantic Models with Extra Constraints:

```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    price: float = Field(..., gt=0) # gt = greater than 0
```

## Creating Objects based on Pydantic Models:

```python
from pydantic import BaseModel

# 1. Define the structure and types clearly
class UserProfile(BaseModel):
    user_id: int
    username: str
    email: str
    is_premium: bool = False
    age: int | None = None

# 2. When creating an instance, your IDE will prompt you for these exact fields
new_user = UserProfile(
    user_id=101,
    username="alice_dev",
    email="alice@example.com"
)

# 3. This is where autocomplete saves you from typos:
# If you type `new_user.` your editor instantly suggests:
# -> user_id (int)
# -> username (str)
# -> email (str)
# -> is_premium (bool)
# -> age (int | None)

print(new_user.username)  # Safely autocompleted!
# print(new_user.usrname)  # Your IDE will immediately flag this with a red squiggly line (type error)
```

## When to use Pydantic vs Python Dictionaries:

- Rule of thumb: Pydantic for data at boundaries (entering or exiting backend)
  - eg: sending and receiving JSON responses from an API
  - validating data as it comes out of a database
  - for env variables and config files (check the section in [FastAPI documentation about convention](fastapi-project-conventions.md))
