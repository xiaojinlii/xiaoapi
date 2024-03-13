from pydantic import BaseModel, ConfigDict, Field

from .employee import EmployeeSimpleOut


class Department(BaseModel):
    name: str


class DepartmentSimpleOut(Department):
    model_config = ConfigDict(from_attributes=True)

    id: int


class DepartmentOut(DepartmentSimpleOut):
    model_config = ConfigDict(from_attributes=True)

    employees: list[EmployeeSimpleOut] = []
