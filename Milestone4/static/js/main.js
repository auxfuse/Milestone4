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
let home = 'https://php-barbell.herokuapp.com/';
let localHome = 'http://127.0.0.1:8000/';

if (location.href === home || location.href === localHome)
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
        setTimeout(type, 340);
    }());