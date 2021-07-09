import {BASE_URL,USER_SERVICE,SLASH} from './constants.js'
import customFetch  from './network.js'


const authService  = {
    signUpUser  : (data) => customFetch(BASE_URL + USER_SERVICE + 'signup/','POST',data)
}


export {authService}