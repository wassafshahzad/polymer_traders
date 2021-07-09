import {BASE_URL,USER_SERVICE,SLASH} from './constants.js'
import customFetch  from './network.js'


window.authService  = {
    signUpUser  : (data) => customFetch(BASE_URL + USER_SERVICE + 'signup/','POST',data)
}


