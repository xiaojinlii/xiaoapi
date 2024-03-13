from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.model_base import BaseModel


class Department(BaseModel):
    __tablename__ = "department"
    __table_args__ = ({'comment': '部门表'})

    name: Mapped[str] = mapped_column(String(50), index=True, nullable=False, comment="部门名称")

    employees: Mapped[List["Employee"]] = relationship(back_populates="department")

    def __repr__(self):
        return f"id: {self.id}, name:{self.name}"
