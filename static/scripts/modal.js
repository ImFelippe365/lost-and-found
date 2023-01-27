const buttonShowModal = document.querySelector('.openDialog');
const buttonCloseDialog = document.querySelector('.closeModal');

const modal = document.querySelector('.modal');

var total_items = buttonShowModal.length;

function showDialog() {
    modal.showModal();
}

function closeDialog() {
    modal.close()
}