// Learning Processing
// Daniel Shiffman
// http://www.learningprocessing.com

// Example 17-3: Scrolling headlines 

// An array of news headlines
var headlines = phrases;

var x; // Horizontal location
var index = 0;

function setup() {
  createCanvas(windowWidth, windowHeight);

  // Initialize headline offscreen
  x = width;
}

function draw() {
  background(0);
  fill(255);

  // Display headline at x location
  textFont("Arial", 700);
  textAlign(LEFT);

  // A specific String from the array is displayed according to the value of the "index" variable.
  text(headlines[index], x, height-100); 

  // Decrement x
  x = x - 20;

  // If x is less than the negative width, then it is off the screen
  // textWidth() is used to calculate the width of the current String.
  var w = textWidth(headlines[index]); 
  if (x < -w) {
    x = width;
    // index is incremented when the current String has left the screen in order to display a new String.
    index = (index + 1) % headlines.length;
  }
}