
from logging.config import fileConfig
from alembic import context
from core_models import Base
from src import settings


target_metadata = Base.metadata
fileConfig(context.config.config_file_name)
config = context.config

config.set_main_option(
    "sqlalchemy.url",
    f"postgresql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
)


section = config.config_ini_section
config.set_section_option(section, "DB_HOST", settings.DB_HOST)
config.set_section_option(section, "DB_PORT", settings.DB_PORT)
config.set_section_option(section, "DB_NAME", settings.DB_NAME)
config.set_section_option(section, "DB_USER", settings.DB_USER)
config.set_section_option(section, "DB_PASS", settings.DB_PASS)




