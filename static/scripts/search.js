console.log("teste")
const search = document.getElementById('searchBar')
const items = document.getElementsByClassName('item')
const container = document.getElementById('itemsContainer')



console.log(search)
search.addEventListener('change', ({ target }) => {
    const searchText = target.value;
    const fullUrl = window.location.href
    const link = fullUrl.includes('#') ? fullUrl.split('#')[0] + '#' + url : fullUrl + '#' + url
    console.log(searchText)
    console.log(window.location)
})