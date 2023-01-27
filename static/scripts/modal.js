const buttonShowModal = document.querySelector('.openDialog');
//const buttonCloseDialog = document.querySelector("closeModal");
const modal = document.querySelectorAll('.modal');
console.log(buttonShowModal)
console.log(modal)

function showDialog(){
    modal.showModal();
}

function closeDialog(){
    modal.close()
}

//buttonShowModal.addEventListener('click', showDialog)
//buttonCloseDialog.addEventListener('click', closeDialog)