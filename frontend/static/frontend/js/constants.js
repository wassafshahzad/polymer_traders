const BASE_URL = '/trader/api/v1/'
const USER_SERVICE = 'user_service'
const SLASH = '/'
const LOGIN_URL = 'api-auth/login'
const ERROR_CODES = {
    404: 'Content not available: Sorry, this content must have been changed or deleted.',
    403: 'Unauthorized: Sorry, You do not have permission to access this content',
    400: 'Bad request: Sorry the request must be malformed',
    409: 'Sorry, this action is not possible at the moment.',
    405: 'Sorry, this action is not possible at the moment.',
};


export {BASE_URL,USER_SERVICE,SLASH,ERROR_CODES,LOGIN_URL}