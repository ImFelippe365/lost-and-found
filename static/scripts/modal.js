const buttonShowModal = document.querySelector('.openDialog');
const buttonCloseDialog = document.querySelector("closeModal");
const modal = document.querySelector('.modal');
console.log(buttonShowModal)
console.log(modal)

var total_items = buttonShowModal.length; 

function showDialog(){
    modal.showModal();
}

function closeDialog(){
    modal.close()
}

//buttonShowModal.addEventListener('click', showDialog)
//buttonCloseDialog.addEventListener('click', closeDialog)