from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as _schemas

if TYPE_CHECKING:
	from sqlalchemy.orm import Session


def _add_tables():
	return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
	db = _database.SessionLocal()
	try:
		yield db
	finally:
		db.close()


async def create_menu(
	menu: _schemas.CreateMenu, db: "Session"
) -> _schemas.Menu:
	menu = _models.Menu(**menu.dict())
	db.add(menu)
	db.commit()
	db.refresh(menu)
	return _schemas.Menu.from_orm(menu)


async def get_all_menus(db: "Session") -> List[_schemas.Menu]:
	menus = db.query(_models.Menu).all()
	return list(map(_schemas.Menu.from_orm, menus))


async def get_menu(menu_id: str, db: "Session"):
	menu = db.query(_models.Menu).filter(_models.Menu.id == menu_id).first()
	return menu


async def delete_menu(menu: _models.Menu, db: "Session"):
	db.delete(menu)
	db.commit()


async def update_menu(
	menu_data: _schemas.CreateMenu, menu: _models.Menu, db: "Session"
) -> _schemas.Menu:
	menu.title = menu_data.title
	menu.description = menu_data.description

	db.commit()
	db.refresh(menu)

	return _schemas.Menu.from_orm(menu)