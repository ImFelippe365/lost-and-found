const buttonCloseMessage = document.getElementById("closeModalMessage");
const modalMessage = document.getElementById('modalMessage');

function closeMessage(){
    modalMessage.close()
}

modalMessage.showModal()

setTimeout(() => {
    closeMessage()
}, 3000);

buttonCloseMessage.addEventListener('click', closeMessage)