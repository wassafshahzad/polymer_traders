window.setItemToLocalStorage = (key,item)=>{
    localStorage.setItem(key,item)
}

window.getItemFromLocalStorage = (key)=>{
    return JSON.parse(localStorage.getItem(key))
}
