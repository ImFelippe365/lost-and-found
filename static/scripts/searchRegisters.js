$(() => {
    const table = $("#desktopItemsList").html();
    const searchBar = $('#registerSearchBar');
    const [headerTagOpen, headerTagClose] = ['<span class="table-footer-group" id="desktopItemsList">', '</span>']

    $(searchBar).keyup(() => {
        const searchText = searchBar.val();
        if (searchText.length === 0) {
            $('#desktopItemsList').replaceWith(headerTagOpen + table + headerTagClose)
        } else {
            $.get(`search/${searchText}`, (response) => {
                $('#desktopItemsList').replaceWith(headerTagOpen + response + headerTagClose)
            })
        }
    })
})

