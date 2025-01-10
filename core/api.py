from ninja import NinjaAPI


from apps.shortener.api import router as shortener_router


api = NinjaAPI(
    title="API com Django Ninja",
    description="API para gerar URLs curtas",
    version="1.0.0"
)

api.add_router('', shortener_router)