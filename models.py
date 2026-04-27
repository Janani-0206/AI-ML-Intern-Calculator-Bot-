from pydantic import BaseModel, Field

class HypotenuseArgs(BaseModel):
    a: float = Field(description="Length of side a")
    b: float = Field(description="Length of side b")

class QuadraticArgs(BaseModel):
    a: float = Field(description="Coefficient a")
    b: float = Field(description="Coefficient b")
    c: float = Field(description="Coefficient c")

class CompoundInterestArgs(BaseModel):
    p: float = Field(description="Principal amount")
    r: float = Field(description="Annual interest rate")
    t: float = Field(description="Time in years")
    n: float = Field(default=12)

class SimpleInterestArgs(BaseModel):
    p: float = Field(description="Principal amount")
    r: float = Field(description="Annual interest rate")
    t: float = Field(description="Time in years")

class GeneralMathArgs(BaseModel):
    expression: str = Field(description="Math expression")