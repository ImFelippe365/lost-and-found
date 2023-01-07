const buttons = [...document.getElementsByClassName('shareButton')]

buttons.forEach(element => {
    element.addEventListener('click', () => {
        const url = element.getAttribute('data-url')
        const link = 'http://localhost:8000' + window.location.pathname + '#' + url
        const dataToShare = {
            url: link,
            text: 'Venha conferir esse item no Achados & Perdidos',
            title: 'Achados & Perdidos'
        }

        navigator.share(dataToShare)
            .then(() => console.log("deu certo"))
            .catch((error) => alert("Não foi possível compartilhar este item"))

        navigator.clipboard.writeText(url)
        alert("O link para redirecionar diretamente para este item foi copiado para sua área de transferência")
    })
});