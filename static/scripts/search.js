const search = document.getElementById('searchBar')
let url = window.location;

search.addEventListener('change', ({ target }) => {
    const searchText = target.value;

    const params = new Proxy(new URLSearchParams(window.location.search), {
        get: (searchParams, prop) => searchParams.get(prop),
    });
    console.log(params.keyword)
    console.log(decodeURI(url.href))
    console.log(decodeURI(url.href).replace("keyword=" + params.keyword, "keyword=" + searchText))

    if (url.href.includes('keyword')) {
        if (params?.keyword) {
            const defaultUrl = params?.order ? url.href.replace('&order', '?order') : url.href;
            window.location.href = decodeURI(defaultUrl).replace("/search?keyword=" + params.keyword, "")
        } else {
            window.location.href = decodeURI(url.href).replace("keyword=" + params.keyword, "keyword=" + searchText)
        }
    } else {
        const prefix = url.origin + url.pathname
        window.location.href = url.href.includes('order') ?
            prefix + '/search?keyword=' + searchText + url.search.replace('?', '&') :
            prefix + '/search?keyword=' + searchText
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

    hasOrder = url.href.includes('order');

    if (hasOrder) {
        if (url.href.includes('keyword')) {
            url.href.replace('?order', '&order')
        }

        const hrefOrdering =
            url.href.includes('asc') ?
                url.href.replace('asc', searchText) :
                url.href.replace('desc', searchText)

        window.location.href = hrefOrdering
    } else {
        window.location.href = url.href.includes('keyword') || url.href.includes('page') ? url.href + '&order=' + searchText : url.href + '?order=' + searchText
    }
})
