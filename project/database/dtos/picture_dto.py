from project.database.dtos.base_dto import BaseDTO
from project.database.gateways.category_gateway import CategoryGateway


class PictureDTO(BaseDTO):
    def __init__(self, title, description, category_id, image, created_at=None, updated_at=None):
        self.title = title
        self.description = description
        self.category_id = category_id
        self.image = image
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_row(cls, rows):
        if not rows:
            return None
        else:
            row_dict = dict(rows[0])

        return cls.from_dict(row_dict)

    @staticmethod
    def from_dict(picture_dict):
        return PictureDTO(
            title=picture_dict.get('title'),
            description=picture_dict.get('description'),
            category_id=picture_dict.get('category_id'),
            image=picture_dict.get('image'),
            created_at=picture_dict.get('created_at'),
            updated_at=picture_dict.get('updated_at'),
        )

    def as_frontend_object(self):
        self.category = CategoryGateway().get_by_id(self.category_id).name
        return self
