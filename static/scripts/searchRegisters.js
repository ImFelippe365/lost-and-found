$(() => {
    const table = $("#itemsContainer").html();
    const searchBar = $('#registerSearchBar');
    const [headerTagOpen, headerTagClose] = ['<span class="table-footer-group" id="itemsContainer">', '</span>']

    $(searchBar).keyup(() => {
        const searchText = searchBar.val();
        if (searchText.length === 0) {
            $('#itemsContainer').replaceWith(headerTagOpen + table + headerTagClose)
        } else {
            $.get(`search/${searchText}`, (response) => {
                // for (let index = 0; index < response.length; index++) {
                //     const element = array[index];
                //     if (index % 2 == 0){
                //         element.className = element.className.replace('bg-background-color', 'bg-primary-hover')
                //     } else {
                //         element.className = element.className.replace('bg-primary-hover', 'bg-background-color')
                //     }
                // }
                $('#itemsContainer').replaceWith(headerTagOpen + response + headerTagClose)
            })
        }
    })
})

