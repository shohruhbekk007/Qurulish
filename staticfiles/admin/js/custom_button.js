document.addEventListener("DOMContentLoaded", function() {
    var customButton = document.getElementById('customButton');
    if (customButton) {
        customButton.addEventListener("click", function() {
            alert("Yangi tugma bosildi!");
            // Bu yerga tugma bosilganda bajariladigan harakatlarni yozing
        });
    }
});
