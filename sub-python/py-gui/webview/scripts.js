
function homePage() {
}
function paiedModels() {
    // alert('unsupported！')
    for (let sec of document.querySelectorAll("section")) {
        if (sec.id !== 'paid-models') {
            sec.setAttribute('hidden', 'hidden')
        } else {
            sec.setAttribute('hidden', '')
        }
    }
}
function moreSettings() {
    alert('unsupported！')
}
function importModels() {
    alert('unsupported！')
}
function exitApp() {
    process.exit(0)
}
function minimumWinwow() {
}