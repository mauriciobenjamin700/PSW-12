from ninja import Router


router = Router()


@router.get("/create")
def create(request):
    return {"detail": "Create"}