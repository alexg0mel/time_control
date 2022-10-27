from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def get_main_view():
    return {'hello': 'dude!'}
