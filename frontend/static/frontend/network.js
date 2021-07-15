import { ERROR_CODES } from "./constants.js";
class CustomError extends Error{
  constructor(status,message){
      super(message)
      this.status = status
  }
} 

function _handleErrors({ status, data, message }) {
  if (
    message === 'Network Error' ||
    message === 'Failed to fetch'
  ) {
    alert(
      'Request could not be completed, please check your internet connection.'
    );
  }
  if (status) {
    alert(ERROR_CODES[status]);
  } else {
    alert("Sorry, something went wrong.");
  }
}


function customFetch(
  url,
  method,
  data = undefined,
  is_auth = true,
  content = "application/json"
) {
  return fetch(url, {
    method: method,
    headers: {
      Authorization: is_auth ? `Token ${localStorage.getItem("key")}` : null,
      "Content-Type": content,
    },
    body: data,
  })
    .then((response) => {
      if (!response.ok) {
        throw new CustomError(response.status,response.statusText);
      }
      return response.json();
    })
    .catch((error) => {
      _handleErrors(error);
    });
}

export default customFetch;
