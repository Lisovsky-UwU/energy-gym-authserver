from .ext.parametrica import Field
from .ext.parametrica import Fieldset
from .ext.parametrica import Metaconfig
from .ext.parametrica.io import YAMLFileConfigIO


class CommonSettings(Fieldset):

    use_dev         = Field[bool](True).label('Использовать ли окружение разработки')


class LocalServerSettings(Fieldset):

    host = Field[str]('0.0.0.0').label('Адрес')
    port = Field[int](5020).label('Порт')

    @property
    def address(self):
        return f'{self.host}:{self.port}'


class MainServerConnectionSettings(Fieldset):

    token = Field[str]('').label('Токен доступа')
    base_url = Field[str]('127.0.0.1:5010/api/v1').label('Адрес для API главного сервера')

    @property
    def formated_base_url(self) -> str:
        return f'{self.base_url}{"" if self.base_url[-1] == "/" else "/"}'


class DataBaseSettings(Fieldset):

    host      = Field[str]('127.0.0.1').label('Адрес')
    port      = Field[int](5432).label('Порт')
    user      = Field[str]('').label('Логин для доступа')
    password  = Field[str]('').label('Пароль для доступа')
    base_name = Field[str]('energy-gym').label('Название БД')

    @property
    def connection_string(self) -> str:
        return f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.base_name}'


class Config(Metaconfig):

    common          = Field[CommonSettings]().label('Общие настройки')
    local_server    = Field[LocalServerSettings]().label('Настройки локального сервера')
    main_server     = Field[MainServerConnectionSettings]().label('Настройки подключения к главному серверу')
    database        = Field[DataBaseSettings]().label('Настройки базы данных')


config = Config(YAMLFileConfigIO('config.yaml'))
