// Typewriter animation global variables
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
    /**
     * Function to generate each word in the `words` list and create a typewriter
     * animation looping and passing each character of the current word to the
     * index page h2 element with the class name of `typewriter-txt`.
     */
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