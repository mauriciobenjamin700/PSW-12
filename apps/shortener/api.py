from django.shortcuts import (
    get_object_or_404, 
    redirect
)
from ninja import Router


from apps.shortener.schemas import (
    LinkSchema, 
    UpdateLinkSchema
)
from apps.shortener.models import (
    Clicks,
    Links
)


router = Router()


def validate_token(token: str):
    if token:
        if Links.objects.filter(token=token).exists():
            return False
        
    return True


@router.post("/create", response={201: LinkSchema, 409: dict})
def create(request, schema: LinkSchema):
    data =  schema.to_model_data()
    token = data["token"]

    if not validate_token(token):
        return 409, {"detail": "Token already exists"}


    link = Links(**data)

    link.save()

    return 201, LinkSchema.from_model(link)


@router.get("/{token}", response={200:str,410: dict})
def redirect_to(request, token: str):
    link = get_object_or_404(Links, token=token, active=True)

    if link.expired():
        link.active = False
        link.save()
        return 410, {"detail": "Link expired"}
    

    click = Clicks(link=link, ip=request.META["REMOTE_ADDR"])
    click.save()

    unique_clicks = Clicks.objects.filter(link=link).values("ip").distinct().count()

    if link.max_uniques_cliques:
        if unique_clicks >= link.max_uniques_cliques:
            link.active = False
            link.save()
            return 410, {"detail": "Max unique clicks reached"}

    return redirect(link.redirect_link)


@router.put("/{link_id}", response={200: LinkSchema, 409: dict})
def update_link(request, link_id: int, link_schema: UpdateLinkSchema):
    link = get_object_or_404(Links, pk=link_id)

    data = link_schema.dict(exclude_unset=True)
    token = data["token"]

    if token:
        if Links.objects.filter(token=token).exclude(id=link_id).exists():
            return False
        return 409, {"detail": "Token already exists"}

    for key, value in data.items():
        if value is not None:
            setattr(link, key, value)

    link.save()

    return 200, LinkSchema.from_model(link)