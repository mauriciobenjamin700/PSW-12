from datetime import timedelta
from ninja import (
    ModelSchema,
    Schema
)


from apps.shortener.models import Links


class LinkSchema(ModelSchema):
    expiration_time: int
   
    class Meta:
        model = Links
        fields = [
        "redirect_link",
        "token",
        "expiration_time",
        "max_uniques_cliques"
        ]


    def to_model_data(self) -> dict:
        return {
            "redirect_link": self.redirect_link,
            "token": self.token,
            "expiration_time": timedelta(minutes=self.expiration_time),
            "max_uniques_cliques": self.max_uniques_cliques
        }
    

    @classmethod
    def from_model(cls, link: Links):
        return cls(
            redirect_link=link.redirect_link,
            token=link.token,
            expiration_time=int(link.expiration_time.total_seconds() / 60),
            max_uniques_cliques=link.max_uniques_cliques
        )
    

class UpdateLinkSchema(Schema):
    redirect_link: str = None
    expiration_time: int = None
    max_uniques_cliques: int = None
    token: str = None
    active: bool = None