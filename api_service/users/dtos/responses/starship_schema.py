from marshmallow import Schema, fields, post_load, validate

from dataclasses import dataclass


@dataclass
class PilotDTO:
    name: str
    id: str


@dataclass
class StarShipDTO:
    name: str
    id: str
    pilots: list[PilotDTO]
    pilot: PilotDTO


class PilotSchema(Schema):
    name = fields.Str(validate=validate.Length(min=3, max=25))
    id = fields.Int(strict=True)

    @post_load
    def serialize(self, data, **kwarg):
        return PilotDTO(**data)


class StarShipSchema(Schema):
    name = fields.Str()
    id = fields.Integer()
    pilots = fields.List(fields.Nested(PilotSchema))
    pilot = fields.Nested(PilotSchema)

    @post_load
    def serialize(self, data, **kwarg):
        return StarShipDTO(**data)


if __name__ == '__main__':
    data = [{
        'name': 'spaceship Milenium',
        'id': 10,
        'pilots': [
            {
                'id': 1,
                'name': 'Den',
            },
            {
                'id': 2,
                'name': 'Arthur',
            },
        ],
        'pilot':
            {
                'id': 1,
                'name': 'Den',
            }

    }
    ]

    starships = StarShipSchema(many=True).load(data)

    for starship in starships:
        assert starship.id < 11
        assert starship.pilot.id == 2
