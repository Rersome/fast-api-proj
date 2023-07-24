# import datetime as _dt
# from sqlalchemy.dialects.postgresql import UUID
import pydantic as _pydantic


class _BaseMenu(_pydantic.BaseModel):
	title: str
	description: str
	# email: str
	# phone_number: str


class Menu(_BaseMenu):
	id: str
	# date_created: _dt.datetime
	class Config:
		orm_mode = True


class CreateMenu(_BaseMenu):
	...