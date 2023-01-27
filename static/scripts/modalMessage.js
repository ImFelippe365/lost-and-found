const buttonCloseDialog = document.getElementById("closeModalMessage");
const modal = document.getElementById('modalMessage');

function closeMessage(){
    modal.close()
}

modal.showModal()

setTimeout(() => {
    closeMessage()
}, 5000);

buttonCloseDialog.addEventListener('click', closeMessage)