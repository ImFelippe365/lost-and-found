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

})


const order = document.getElementById('orderId')

order.addEventListener('change', ({ target }) => {
    const selectText = target.value;
    const items = document.getElementsByClassName('itemsContainer');
    let itemsList = [...items[0].children]
    let platform = '#desktopItemsList'
    if (items.length > 1 && getComputedStyle(items[0], null).display == 'none') {
        itemsList = [...items[1].children];
        platform = '#mobileItemsList'
    }
    console.log(itemsList)

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

    var itemsContainer = document.querySelector(platform);
    itemsList.forEach(item => {
        itemsContainer.appendChild(item);
    });
})
