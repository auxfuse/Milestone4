// Alerts timeout
setTimeout(function() {
    $('#msg-alert').fadeOut('slow');
}, 3000);

// Typewriter
const words = [
    'Form',
    'Technique',
    'Strength',
    'Stability',
    'Explosivity',
    'Core',
    'Character'
];
let count = 0;
let currentWord = 0;
let currentText = '';
let letter = '';

(function type(){
    if(count === words.length) {
      count = 0;
    }
    currentText = words[count];
    letter = currentText.slice(0, ++currentWord);

    document.querySelector('.typewriter-txt').textContent = letter;
    if(letter.length === currentText.length){
        count++;
        currentWord = 0;
    }
    setTimeout(type, 400);
}());