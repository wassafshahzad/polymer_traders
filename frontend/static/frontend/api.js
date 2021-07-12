import {BASE_URL,USER_SERVICE,SLASH, LOGIN_URL} from './constants.js'
import customFetch  from './network.js'


window.authService  = {
    signUpUser  : (data) => customFetch(BASE_URL + USER_SERVICE + SLASH + 'signup/','POST',data,false),
    loginUser : (data) => customFetch(BASE_URL  + LOGIN_URL + SLASH,'POST',data,false)
}


