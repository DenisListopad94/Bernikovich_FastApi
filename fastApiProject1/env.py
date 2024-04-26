import os
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

config = context.config


section = config.config_ini_section
config.set_section_option(section, "DB_HOST", settings.DB_HOST)
config.set_section_option(section, "DB_PORT", settings.DB_PORT)
config.set_section_option(section, "DB_USER", settings.DB_USER)
config.set_section_option(section, "DB_NAME", settings.DB_NAME)
config.set_section_option(section, "DB_PASS", settings.DB_PASS)


from src.core.model.base import Base
target_metadata = Base.metadata
