from pydantic import BaseModel, ConfigDict, Field


# from .department import DepartmentSimpleOut


class Employee(BaseModel):
    name: str
    nickname: str | None = None


class EmployeeSimpleOut(Employee):
    model_config = ConfigDict(from_attributes=True)

    id: int


class EmployeeOut(EmployeeSimpleOut):
    model_config = ConfigDict(from_attributes=True)

    # department: DepartmentSimpleOut  # error: circular import


class EmployeeIn(Employee):
    """
    创建员工
    """
    dep_id: int


class EmployeeUpdate(BaseModel):
    """
    更新用户详细信息
    """
    name: str | None = None
    nickname: str | None = None
