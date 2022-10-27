from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.db import get_session
from app.model import Timeline, TimelineOut, TimelinePost

router = APIRouter()


@router.get('/timelines', response_model=list[TimelineOut])
def get_timelines_view(session: Session = Depends(get_session)):
    timelines = session.exec(select(Timeline)).all()
    return timelines


@router.post('/timelines', response_model=TimelineOut)
def post_timeline_view(data: TimelinePost, session: Session = Depends(get_session)):
    instance = Timeline(**data.dict())
    session.add(instance)
    session.commit()
    session.refresh(instance)
    return instance


@router.get('/timelines/{timeline_id}', response_model=TimelineOut)
def get_timeline_view(timeline_id: int, session: Session = Depends(get_session)):
    timeline = session.get(Timeline, timeline_id)
    if not timeline:
        raise HTTPException(status_code=404, detail="Item not found")
    return timeline


@router.put('/timelines/{timeline_id}', response_model=TimelineOut)
def put_timeline_view(timeline_id: int, data: TimelinePost, session: Session = Depends(get_session)):
    timeline = session.get(Timeline, timeline_id)
    if not timeline:
        raise HTTPException(status_code=404, detail="Item not found")
    data = data.dict()

    for key in data:
        setattr(timeline, key, data[key])
    # autoupdate does not work if field not included to input data :(
    timeline.updated_at = datetime.utcnow()

    session.add(timeline)
    session.commit()
    session.refresh(timeline)
    return timeline


@router.delete('/timelines/{timeline_id}')
def delete_timeline_view(timeline_id: int, session: Session = Depends(get_session)):
    timeline = session.get(Timeline, timeline_id)
    if not timeline:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(timeline)
    session.commit()

    return None
