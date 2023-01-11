console.log("teste")
const search = document.getElementById('searchBar')
const items = document.getElementsByClassName('item')
const container = document.getElementById('itemsContainer')

search.addEventListener('change', ({ target }) => {
    const searchText = target.value;
    const fullUrl = window.location.href
    const link = fullUrl.includes('#') ? fullUrl.split('#')[0] + '#' + url : fullUrl + '#' + url
    console.log(searchText)
    console.log(window.location)
})


const order = document.getElementById('orderId')
console.log(order)
order.addEventListener('change', ({ target }) => {
    const searchText = target.value;
    const fullUrl = window.location.href
    // const link = fullUrl.includes('#') ? fullUrl.split('#')[0] + '#' + url : fullUrl + '#' + url

    if (window.location.href.includes('order')) {
        const hrefOrdering =
            window.location.href.includes('asc') ?
                window.location.href.replace('asc', searchText) :
                window.location.href.replace('desc', searchText)

        window.location.href = hrefOrdering
    } else {
        window.location.href = window.location.href + '?order=' + searchText
    }
    console.log(searchText)
    console.log(window.location)
})
