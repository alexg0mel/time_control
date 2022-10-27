from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.db import get_session
from app.model import Project, ProjectOut, ProjectPost

router = APIRouter()


@router.get('/projects', response_model=list[ProjectOut])
def get_projects_view(session: Session = Depends(get_session)):
    projects = session.exec(select(Project)).all()
    return projects


@router.post('/projects', response_model=ProjectOut)
def post_project_view(data: ProjectPost, session: Session = Depends(get_session)):
    instance = Project(**data.dict())
    session.add(instance)
    session.commit()
    session.refresh(instance)
    return instance


@router.get('/projects/{project_id}', response_model=ProjectOut)
def get_project_view(project_id: int, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Item not found")
    return project


@router.put('/projects/{project_id}', response_model=ProjectOut)
def put_project_view(project_id: int, data: ProjectPost, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Item not found")
    data = data.dict()

    for key in data:
        setattr(project, key, data[key])
    session.add(project)
    session.commit()
    session.refresh(project)
    return project


@router.delete('/projects/{project_id}')
def delete_project_view(project_id: int, session: Session = Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(project)
    session.commit()

    return None
