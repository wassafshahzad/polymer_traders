window.setItemToLocalStorage = (key,item)=>{
    debugger
    localStorage.setItem(key,item)
}

window.getItemFromLocalStorage = (key)=>{
    return JSON.parse(localStorage.getItem(key))
}
