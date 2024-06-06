from PIL import Image
from quart import Blueprint, send_from_directory, abort, request
from werkzeug.exceptions import NotFound
from loguru import logger

from ..controllers import ImgController, AuthController
from ..orm import SessionCtx
from ..services.database import UserDBService


media = Blueprint('media', __name__)


@media.get('/<filename>')
async def get_image(filename: str):
    try:
        return await send_from_directory(
            ImgController().retreive_path(),
            filename
        )
    except NotFound:
        abort(404)


@media.post('/update-my-picture')
async def update_image():
    token = request.headers.get('Authorization')
    if token is None:
        return { 'error': 'Отсутствует токен в заголовке' }
    
    with SessionCtx() as session:
        user = AuthController(
            UserDBService(session)
        ).get_user(token)

        user.image = ImgController().save(
            Image.open(
                (await request.files)['image']
            )
        )
        session.commit()
        logger.success(f'Обновлена картинка для пользователя id={user.id}, новый файл называется {user.image}')

        return {'imgName': user.image}
