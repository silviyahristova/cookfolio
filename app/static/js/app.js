//JS for navbar toggle
const menuToggle = document.getElementById('menu-toggle');
const navLinks = document.getElementById('navbar-links');

menuToggle.addEventListener('click', function(){
    navLinks.classList.toggle('show'); 
    
    const icon = menuToggle.querySelector('i');
    icon.classList.toggle('fa-bars');
    icon.classList.toggle('fa-xmark');
});

//Manual close flash messages

document.querySelectorAll('.flash-message .close-btn').forEach(button => {
    button.addEventListener('click', (e) => {
        const message = e.target.closest('.flash-message');
        message.remove();
    });
});