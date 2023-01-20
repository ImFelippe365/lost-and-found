const cpfInput = document.getElementById('id_cpf')

cpfInput.addEventListener('keypress', () => {
    let inputLength = cpfInput.value.length

    if (inputLength === 3 || inputLength === 7){
        cpfInput.value += '.'
    }else if (inputLength === 11){
        cpfInput.value += '-'
    }
})