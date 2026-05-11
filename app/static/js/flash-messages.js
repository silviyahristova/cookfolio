// JavaScript to handle flash message behavior
document.addEventListener('DOMContentLoaded', function() {
    const flashMessages = document.querySelectorAll('.flash-message');

    flashMessages.forEach(function(message) {
        // Automatically fade out flash messages after 5 seconds
        setTimeout(function() {
            message.style.transition = 'opacity 0.5s ease';
            message.style.opacity = '0';
        }, 5000);
    });
});

//Manually dismiss flash messages when the close button is clicked
const closeBtns = document.querySelectorAll('.close-btn');
if (closeBtns) {
    closeBtns.forEach(function(btn) {
        btn.addEventListener('click', () => {
            const message = btn.closest('.flash-message');
            message.remove();
        });
    });
}