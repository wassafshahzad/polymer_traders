const ERROR_CODES = {
    404: 'Content not available: Sorry, this content must have been changed or deleted.',
    403: 'Unauthorized: Sorry, You do not have permission to access this content',
    400: 'Bad request: Sorry the request must be malformed',
    409: 'Sorry, this action is not possible at the moment.',
    405: 'Sorry, this action is not possible at the moment.',
};


  function handleErrors(error) {
    if (
      error.message === 'Network Error' ||
      error.message === 'Failed to fetch'
    ) {
      alert(
        'Request could not be completed, please check your internet connection.'
      );
    } else if (error.response && error.response.data.error) {
      alert(error.response.data.error);
    } else if (error.response && error.response.data.message) {
      alert(error.response.data.message);
    } else if (error.response && error.response.status === 400) {
      alert(error.response.data);
    } else if (error.response && error.response.status) {
      alert(ERROR_CODES[error.response.status]);
    } else {
      alert('Sorry, something went wrong.');
    }
  }


function customFetch(url,method, data=undefined, is_auth = true){
    return fetch(url, {
        method: method,
        headers: {
            Authorization: is_auth ? `Token ${localStorage.getItem('key')}` : null 
        },
        body: data
    }).then(response =>{
        if (!response.ok) {
            throw new Error(response)
        }
        return  response.json()
    }).catch(error => {
        handleErrors(error)
    })
}

export default customFetch