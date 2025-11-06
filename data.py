class Url:
    MAIN_URL = 'https://stellarburgers.education-services.ru'
    CREATE_USER = '/api/auth/register'
    LOGIN_USER = '/api/auth/login'
    USER = '/api/auth/user'
    ORDER_CREATION = '/api/orders'

class ResponseMessages:
    USER_CREATED_SUCCESS = True
    USER_LOGIN_ALREADY = "User already exists"
    USER_NOT_ENOUGH_DATA = "Email, password and name are required fields"
    USER_LOGIN_SUCCESS = True
    USER_DATA_INCORRECT = "email or password are incorrect"