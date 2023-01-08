console.log("teste")
const search = document.getElementById('searchBar')
const items = document.getElementsByClassName('item')
const container = document.getElementById('itemsContainer')



console.log(search)
search.addEventListener('change', ({ target }) => console.log({ target }))