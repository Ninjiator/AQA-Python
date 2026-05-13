from dynaconf import Dynaconf

from utils.definitions import BASE_PATH

d_settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[BASE_PATH / ".settings.toml", BASE_PATH / ".secrets.toml"],
    environments=True,
    load_dotenv=True,
)