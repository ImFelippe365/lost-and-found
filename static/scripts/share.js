const buttons = [...document.getElementsByClassName('shareButton')]
const fullUrl = window.location.href

if (fullUrl.includes('#')) {
    const [path, cardId] = fullUrl.split('#')
    const cardContainer = document.getElementsByClassName(cardId);

    for (let index = 0; index < cardContainer.length; index++) {
        const element = cardContainer[index];
        element.style.border = '2px solid lightblue'
        element.style.borderRadius = '0.5rem'
        element.style.boxShadow = '-2px 0px 24px 0px rgba(30,129,176,0.34)'
    }
}
buttons.forEach(element => {
    element.addEventListener('click', () => {
        const url = element.getAttribute('data-url')
        const link = fullUrl.includes('#') ? fullUrl.split('#')[0] + '#' + url : fullUrl + '#' + url

        const dataToShare = {
            url: link,
            text: 'Venha conferir esse item no Achados & Perdidos',
            title: 'Achados & Perdidos'
        }

        navigator.share(dataToShare)
            .catch((error) => alert("Não foi possível compartilhar este item"))
    })
});