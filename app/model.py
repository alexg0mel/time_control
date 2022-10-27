from typing import Optional
from datetime import date, datetime

from sqlmodel import Field, SQLModel, Relationship


# -- many-to-many links -- #

class TagTaskLink(SQLModel, table=True):
    tag_id: int = Field(foreign_key="tag.id", primary_key=True)
    task_id: int = Field(foreign_key="task.id", primary_key=True)


class TagTaskGroup(SQLModel, table=True):
    group_id: int = Field(foreign_key="group.id", primary_key=True)
    task_id: int = Field(foreign_key="task.id", primary_key=True)


# -- TimestampModel -- #

class TimestampModel(SQLModel):
    created_at: datetime = Field(default=datetime.utcnow())
    updated_at: datetime = Field(default_factory=datetime.utcnow)

# -- Project -- #

class ProjectPost(SQLModel):
    name: str
    active: bool = True


class Project(ProjectPost, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tasks: list['Task'] = Relationship(back_populates='project')


class ProjectOut(ProjectPost):
    id: int
    tasks: list['Task'] = Relationship(back_populates='project')


# -- Tag -- #

class Tag(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    tasks: list["Task"] = Relationship(back_populates="tags", link_model=TagTaskLink)


# -- Task -- #

class Task(TimestampModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    project_id: int = Field(foreign_key='project.id')
    project: Optional[Project] = Relationship(back_populates='tasks')
    tags: list["Tag"] = Relationship(back_populates="tasks", link_model=TagTaskLink)
    plan_time: int = 0
    groups: list["Group"] = Relationship(back_populates="tasks", link_model=TagTaskGroup)
    times: list["Time"] = Relationship(back_populates="task")


# -- Timeline-- #

class TimelinePost(SQLModel):
    name: str
    start_time: date | None = None
    end_time: date | None = None
    status: str = ""


class Timeline(TimestampModel, TimelinePost, table=True):
    id: int | None = Field(default=None, primary_key=True)
    groups: list['Group'] = Relationship(back_populates='timeline')


class TimelineOut(TimestampModel, TimelinePost):
    id: int
    groups: list['Group'] = Relationship(back_populates='timeline')


# -- Group -- #

class Group(TimestampModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    tasks: list["Task"] = Relationship(back_populates="groups", link_model=TagTaskGroup)
    timeline_id: int = Field(foreign_key='timeline.id')
    timeline: Optional[Timeline] = Relationship(back_populates='groups')
    times: list["Time"] = Relationship(back_populates="group")


# -- Time -- #

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


