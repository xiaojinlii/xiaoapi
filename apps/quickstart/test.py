import asyncio

from sqlalchemy import select

from db.database import session_factory
from apps.quickstart.models import *


async def insert_records(session):
    d1 = Department(name="hr")
    e1 = Employee(name="Jack", nickname="Jack", department=d1)
    e2 = Employee(name="Tom", nickname="Tom", department=d1)
    session.add(e1)
    session.add(e2)

    d2 = Department(name="it")
    e3 = Employee(name="Amy", nickname="Amy", department=d2)
    e4 = Employee(name="Smith", nickname="Smith", department=d2)
    session.add(e3)
    session.add(e4)

    await session.commit()


async def select_records(session):
    queryset = await session.execute(select(Employee).where(Employee.id == 1))
    print(queryset.first())
    queryset = await session.scalars(select(Employee).where(Employee.id == 1))
    e = queryset.first()
    print(e)
    d = await e.awaitable_attrs.department
    print(d)
    employees = await d.awaitable_attrs.employees
    print(employees)


async def main():
    async with session_factory() as session:
        async with session.begin():
            await insert_records(session)
            # await select_records(session)


if __name__ == "__main__":
    asyncio.run(main())
