from quart import Blueprint


auth_bl = Blueprint('auth', 'auth')


@auth_bl.post('/sing-up')
async def sing_up():
    return { 'result': 'sing-up' }


@auth_bl.post('/login')
async def login():
    return { 'result': 'login' }


@auth_bl.get('/check-login')
async def check_login():
    return { 'result': 'check-login' }


@auth_bl.post('/logout')
async def logout():
    return { 'result': 'logout' }
