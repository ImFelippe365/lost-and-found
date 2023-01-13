const search = document.getElementById('searchBar')
let url = window.location;

console.log(window.location.pathname)
search.addEventListener('change', ({ target }) => {
    const searchText = target.value;

    const params = new Proxy(new URLSearchParams(window.location.search), {
        get: (searchParams, prop) => searchParams.get(prop),
    });

    if (params?.keyword) {
        if (href.includes('keyword')) {
            href.replace('?keyword', '&keyword')
        }

        window.location.href = url.replace(params.keyword, searchText)
    } else {
        console.log('SIMMMMMMM', url.href, url.pathname)
        url.pathname = url.pathname + '/search'
        console.log("NOVO -> ", url.href)

        window.location.href = url.href.includes('order') ? url.href + '&keyword=' + searchText : url.href + '?keyword=' + searchText

    }

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
