function onChangeSearch(inputSearch) {
    let searchText = inputSearch.value.normalize('NFD').replace(/[\u0300-\u036f]/g, "").toUpperCase();
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
        let itemName = item.getAttribute('data-name').normalize('NFD').replace(/[\u0300-\u036f]/g, "").toUpperCase();
        let isRegister = item.getAttribute('data-page') === 'register';

        if (itemName.includes(searchText)) {
            item.style.display = isRegister ? 'table-row' : afterDisplay
        } else {
            item.style.display = 'none'
        }
    }
}



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

    itemsList.sort((a, b) => {
        let a_date = new Date(a.getAttribute('data-date'));
        let b_date = new Date(b.getAttribute('data-date'));

        if (a_date < b_date) {
            return selectText == 'desc' ? 1 : -1
        }
        if (b_date < a_date) {
            return selectText == 'desc' ? -1 : 1
        }

        return 0
    })
    var isRegisterPage = items[0].getAttribute('data-page') == 'register'
    var itemsContainer = document.querySelector(isRegisterPage ? '#itemsContainer' : platform);
    itemsList.forEach((item, index) => {
        if (isRegisterPage) {
            if (index % 2 == 0) {
                item.className = item.className.replace('bg-background-color', 'bg-primary-hover')
            } else {
                item.className = item.className.replace('bg-primary-hover', 'bg-background-color')
            }
        }
        itemsContainer.appendChild(item);
    });
})
