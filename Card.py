from pydantic import BaseModel

class Card(BaseModel):
    card_id: str | None = None
    print_id: str | None = None
    set_id: str | None = None
    rarity: str | None = None
    type: str | None = None
    name: str | None = None
    cost: str | None = None
    attr: str | None = None
    power: str | None = None
    counter: str | None = None
    color: str | None = None
    feat: str | None = None
    text: str | None = None
    img: str | None = None