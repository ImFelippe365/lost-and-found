const buttonShowModal = document.querySelector('.openDialog');
const buttonCloseDialog = document.querySelector('.closeModal');

const modal = document.querySelector('.modal');

var total_items = buttonShowModal.length;

function showDialog(id, name) {
    const itemName = document.querySelector('#modalItemName');
    const deleteForm = document.querySelector('#deleteForm');

    itemName.innerText = name
    deleteForm.setAttribute('action', `items/${id}/delete/`)
    
    modal.showModal();
}

function closeDialog() {
    modal.close()
}