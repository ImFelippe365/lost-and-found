const search = document.getElementById('searchBar')
let url = window.location;

search.addEventListener('input', ({ target }) => {
    let searchText = target.value.normalize('NFC').toUpperCase();
    const itemsContainer = document.getElementsByClassName('itemsContainer');
    let afterDisplay = ''

    let items = itemsContainer[0].children
    if (itemsContainer.length > 1) {
        if (getComputedStyle(itemsContainer[0], null).display == 'none') {
            items = itemsContainer[1].children;
            afterDisplay = 'block';
        } else {
            items = itemsContainer[0].children;
            afterDisplay = 'flex';
        }
    }

    for (let index = 0; index < items.length; index++) {
        const item = items[index];
        let itemName = item.getAttribute('data-name');
        let isRegister = item.getAttribute('data-page') === 'register';
        itemName = itemName.normalize('NFC').toUpperCase();
        console.log(itemName.normalize('NFD').toUpperCase())
        if (itemName.includes(searchText)) {
            item.style.display = isRegister ? 'table-row' : afterDisplay
        } else {
            item.style.display = 'none'
        }
    }

    // const params = new Proxy(new URLSearchParams(window.location.search), {
    //     get: (searchParams, prop) => searchParams.get(prop),
    // });
    // console.log(params.keyword)
    // console.log(decodeURI(url.href))
    // console.log(decodeURI(url.href).replace("keyword=" + params.keyword, "keyword=" + searchText))

    // if (url.href.includes('keyword')) {
    //     if (params?.keyword) {
    //         const defaultUrl = params?.order ? url.href.replace('&order', '?order') : url.href;
    //         window.location.href = decodeURI(defaultUrl).replace("/search?keyword=" + params.keyword, "")
    //     } else {
    //         window.location.href = decodeURI(url.href).replace("keyword=" + params.keyword, "keyword=" + searchText)
    //     }
    // } else {
    //     const prefix = url.origin + url.pathname
    //     window.location.href = url.href.includes('order') ?
    //         prefix + '/search?keyword=' + searchText + url.search.replace('?', '&') :
    //         prefix + '/search?keyword=' + searchText
    // }

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
    const selectText = target.value;
    const items = document.getElementById('itemsContainer');

    const itemsList = [...items.children]

    itemsList.sort((a, b) => {
        let a_date = new Date(a.getAttribute('data-date'));
        let b_date = new Date(b.getAttribute('data-date'));

        console.log(a_date, b_date)
        if (a_date < b_date) {
            return selectText == 'desc' ? 1 : -1
        }
        if (b_date < a_date) {
            return selectText == 'desc' ? -1 : 1
        }

        return 0
    })

    var itemsContainer = document.querySelector('#itemsContainer');
    itemsList.forEach(item => {
        itemsContainer.appendChild(item);
    });
    // console.log(selectText)
    // for (let index = 0; index < items.length; index++) {
    //     const item = items[index];
    //     let itemName = item.getAttribute('data-date');
    //     itemName = itemName.normalize('NFC').toUpperCase();

    //     if (itemName.includes(selectText)) {
    //         item.style.display = 'flex'
    //     } else {
    //         item.style.display = 'none'
    //     }
    // }
    // const searchText = target.value;

    // hasOrder = url.href.includes('order');

    // if (hasOrder) {
    //     if (url.href.includes('keyword')) {
    //         url.href.replace('?order', '&order')
    //     }

    //     const hrefOrdering =
    //         url.href.includes('asc') ?
    //             url.href.replace('asc', searchText) :
    //             url.href.replace('desc', searchText)

    //     window.location.href = hrefOrdering
    // } else {
    //     window.location.href = url.href.includes('keyword') || url.href.includes('page') ? url.href + '&order=' + searchText : url.href + '?order=' + searchText
    // }
})
