from typing import Optional
from datetime import date, datetime

from sqlmodel import Field, SQLModel, Relationship


class TagTaskLink(SQLModel, table=True):
    tag_id: int = Field(foreign_key="tag.id", primary_key=True)
    task_id: int = Field(foreign_key="task.id", primary_key=True)


class TagTaskGroup(SQLModel, table=True):
    group_id: int = Field(foreign_key="group.id", primary_key=True)
    task_id: int = Field(foreign_key="task.id", primary_key=True)


class Project(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    active: bool = True

    tasks: list['Task'] = Relationship(back_populates='project')


class Tag(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    tasks: list["Task"] = Relationship(back_populates="tags", link_model=TagTaskLink)


class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    project_id: int = Field(foreign_key='project.id')
    project: Optional[Project] = Relationship(back_populates='tasks')
    tags: list["Tag"] = Relationship(back_populates="tasks", link_model=TagTaskLink)
    plan_time: int = 0
    groups: list["Group"] = Relationship(back_populates="tasks", link_model=TagTaskGroup)
    times: list["Time"] = Relationship(back_populates="tasks")


class Timeline(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    name: str
    start_time: date | None = None
    end_time: date | None = None
    status: str = ""
    groups: list['Group'] = Relationship(back_populates='timeline')


class Group(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    tasks: list["Task"] = Relationship(back_populates="groups", link_model=TagTaskGroup)
    timeline_id: int = Field(foreign_key='timeline.id')
    timeline: Optional[Timeline] = Relationship(back_populates='groups')
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    times: list["Time"] = Relationship(back_populates="groups")


class Time(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    task_id: int = Field(foreign_key='task.id')
    task: Optional[Task] = Relationship(back_populates='times')

    group_id: int = Field(foreign_key='group.id')
    group: Optional[Group] = Relationship(back_populates='times')

    start_time: datetime = Field(nullable=False)
    end_time: datetime | None = None

    fact_time: int = 0


def create_all():
    pass
