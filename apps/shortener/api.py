from ninja import Router


router = Router()


@router
def create(request):
    return {"detail": "Create"}