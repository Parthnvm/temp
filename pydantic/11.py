# Simple class inheritance example
# class calc:
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
# class adavanced(calc):
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a/b

# obj=adavanced()
# print(obj.add(10,5))

#First example using pydantic

from pydantic import BaseModel,ValidationError

class User(BaseModel):
    id : int
    name : str
    age : int
    
    
# user = User(id=1,name="Parth",age=19)
# user1= User(id="2",name="Parth",age="21")
# # print(user)
# print(user1)

# try:
#     user = User(id=".1",name="Parth",age=19)
# except ValidationError as e:
#     print(e)

#Errors are structed Readable, API-Friendly

from typing import Optional
from pydantic import BaseModel, ValidationError,Field,field_validator

class Employee(BaseModel):
    id: int
    name: str
    department: Optional[str] = "AIML"
    salary: Optional[float] = 100000.0

emp = Employee(id='1', name='Parth', department="AIML", salary=100000.0)
# print(emp)    
# try:
    
# except ValidationError as e:
#     print(e)

class Product(BaseModel):
    name : str=Field(..., title="Product Name", max_length=50)
    price: float=Field(...,gt=0)
    quantity : int= Field(...,ge=0)
    
product = Product(name="Laptop", price=1500.0, quantity=10)
# print(product)

class Student(BaseModel):
    name :str
    marks: int
    
    @field_validator('marks')
    def check_marks(cls,value):
        if value < 0 or value > 100:
            raise ValueError('Marks must be between 0 and 100')
        return value
    
student = Student(name="Parth", marks=101)
    
print(student)

class Address(BaseModel):
    city : str
    pincode: int
class Customer(BaseModel):
    id: int
    name: str
    address: Address
    
customer = Customer(id=1, name="Parth", address=Address(city="Mumbai", pincode=400001))

# real time - order product,prices

from typing import List
from pydantic import BaseModel

class Order(BaseModel):
    order_id: int
    items: List[str]
    prices: List[float]
# class CustomerOrder(BaseModel):
#     customer_id: int
#     customer_name: str    
#     orders: List[Order]

order = Order(order_id=101, items=["Laptop", "Mouse"], prices=[1500.0, 25.0])

    