// Create a new color picker instance
// https://iro.js.org/guide.html#getting-started
var colorPicker = new iro.ColorPicker(".colorPicker", {
  // color picker options
  // Option guide: https://iro.js.org/guide.html#color-picker-options
  width: 280,
  color: "rgb(255, 0, 0)",
  borderWidth: 1,
  borderColor: "#fff" });


// https://iro.js.org/guide.html#color-picker-events
colorPicker.on(["color:init", "color:change"], function (color) {
  // Show the current color in different formats
  // Using the selected color: https://iro.js.org/guide.html#selected-color-api
  fetch('http://192.168.0.192:5000/lightStrip/' + color.rgbString)
  .then(response => response.json())
  .then(data => console.log(data));
});

function ambient1(){
    fetch('http://192.168.0.192:5000/ambient1')
    .then(response => response.json())
    .then(data => console.log(data));
}

function ambient2(){
    fetch('http://192.168.0.192:5000/ambient2')
    .then(response => response.json())
    .then(data => console.log(data));
}

function strobe(){
    fetch('http://192.168.0.192:5000/strobe')
    .then(response => response.json())
    .then(data => console.log(data));
}

function off(){
    fetch('http://192.168.0.192:5000/off')
    .then(response => response.json())
    .then(data => console.log(data));
}

