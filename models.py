# from sqlalchemy.dialects.postgresql import UUID
import uuid
import sqlalchemy as _sql

import database as _database


class Menu(_database.Base):
	__tablename__ = "menus"
	id = _sql.Column(_sql.String, primary_key=True, index=True, default=str(uuid.uuid4()))
	title = _sql.Column(_sql.String, index=True)
	description = _sql.Column(_sql.String, index=True)


# class SubMenu(_database.Base):
# 	__tablename__ = "submenu"
# 	id = _sql.Column(_sql.Integer, primary_key=True, index=True)
# 	title = _sql.Column(_sql.String, index=True)
# 	description = _sql.Column(_sql.String, index=True)
# 	relative_menu_id = _sql.Column(_sql.Integer, _sql.ForeignKey("menu.id"), index=True)
