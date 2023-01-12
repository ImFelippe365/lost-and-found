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
const selects = [...order.children]

if (window.location.href.includes('order')) {
    const orderValue = window.location.href.includes('asc') ? 'asc' : 'desc'
    selects.forEach(select => {
        if (select.value === orderValue) {
            select.selected = true
        } else {
            select.selected = false
        }
    });
}

order.addEventListener('change', ({ target }) => {
    const searchText = target.value;
    const url = window.location.href

    hasOrder = url.includes('order');

    if (hasOrder) {
        if (url.includes('keyword')) {
            url.replace('?order', '&order')
        }

        const hrefOrdering =
            url.includes('asc') ?
                url.replace('asc', searchText) :
                url.replace('desc', searchText)

        window.location.href = hrefOrdering
    } else {
        window.location.href = url.includes('keyword') ? url + '&order=' + searchText : url + '?order=' + searchText
    }
})
