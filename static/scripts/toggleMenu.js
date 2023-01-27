function toggleMenu(id) {
    var options = document.getElementById(id).style
    if (!options.display) {
        options.display = 'block'
        return;
    }
    options.display = options.display == 'none' ? 'block' : 'none'
}

function showCardInformations(id, buttonId) {
    var information = document.getElementById(id).style
    var showInformationButton = document.getElementById(buttonId).style

    if (!information.display) {
        information.display = 'flex'
        showInformationButton.display = information.display == 'none' ? 'block' : 'none'
        return;
    }

    information.display = information.display == 'none' ? 'flex' : 'none'
    showInformationButton.display = information.display == 'none' ? 'block' : 'none'
}