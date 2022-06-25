

var modal = document.getElementById('id01');
window.addEventListener('scroll', function() {
    let header = this.document.querySelector('header')
    header.classList.toggle('sticky', window.scrollY > 0)
})

function toggleMenu() {
    let menuToggle = document.querySelector('.toggle')
    let menu = document.querySelector('.menu')
    menuToggle.classList.toggle('active')
    menu.classList.toggle('active')
}
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}