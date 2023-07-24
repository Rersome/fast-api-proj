from typing import TYPE_CHECKING, List
from sqlalchemy.dialects.postgresql import UUID
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
	from sqlalchemy.orm import Session

app = _fastapi.FastAPI()


@app.post("/api/v1/menus/", response_model=_schemas.Menu, status_code=201)
async def create_menu(
	menu: _schemas.CreateMenu,
	db: _orm.Session = _fastapi.Depends(_services.get_db),
):
	return await _services.create_menu(menu=menu, db=db)


@app.get("/api/v1/menus/", response_model=List[_schemas.Menu])
async def get_menus(db: _orm.Session = _fastapi.Depends(_services.get_db)):
	return await _services.get_all_menus(db=db)


@app.get("/api/v1/menus/{menu_id}/", response_model=_schemas.Menu)
async def get_menu(
	menu_id: str,
	db: _orm.Session = _fastapi.Depends(_services.get_db)
):
	menu = await _services.get_menu(db=db, menu_id=menu_id)
	if not menu:
		raise _fastapi.HTTPException(status_code=404, detail="menu not found")

	return menu


@app.delete("/api/v1/menus/{menu_id}/")
async def delete_menu(
	menu_id: str,
	db: _orm.Session = _fastapi.Depends(_services.get_db)
):
	menu = await _services.get_menu(db=db, menu_id=menu_id)
	if not menu:
		raise _fastapi.HTTPException(status_code=404, detail="menu not found")

	await _services.delete_menu(menu, db=db)

	return "successfully deleted the menu"


@app.patch("/api/v1/menus/{menu_id}/", response_model=_schemas.Menu, status_code=200)
async def update_menu(
	menu_id: str,
	menu_data: _schemas.CreateMenu,
	db: _orm.Session = _fastapi.Depends(_services.get_db),
):
	menu = await _services.get_menu(db=db, menu_id=menu_id)
	if not menu:
		raise _fastapi.HTTPException(status_code=404, detail="menu not found")

	return await _services.update_menu(
		menu_data=menu_data, menu=menu, db=db
	)