$(() => {
    const table = $("#itemsContainer").html();
    const searchBar = $('#registerSearchBar');
    const [headerTagOpen, headerTagClose] = ['<span class="table-footer-group" id="itemsContainer">', '</span>']

    $(searchBar).keyup(() => {
        const searchText = searchBar.val(); 
        if (searchText.length === 0) {
            $('#itemsContainer').replaceWith(headerTagOpen + table + headerTagClose)
        } else {
            $.get(`search/${searchText}`, (response) =>
                $('#itemsContainer').replaceWith(headerTagOpen + response + headerTagClose)
            )

        }
    })
})

