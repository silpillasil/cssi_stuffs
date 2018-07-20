// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Use querySelector to store the div in a variable.
let responseBox = document.querySelector('#responseBox');
let redButton = document.querySelector('#red');

// Use addEventListener to respond to a click event.
redButton.addEventListener('click', e => {
  console.log("You clicked the red button!");
  responseBox.style.backgroundColor='red';
})

let greenButton = document.querySelector('#green');

// Use addEventListener to respond to a click event.
greenButton.addEventListener('click', e => {
  console.log("You clicked the green button!");
  responseBox.style.backgroundColor='green';

})

let blueButton = document.querySelector('#blue');

// Use addEventListener to respond to a click event.
blueButton.addEventListener('click', e => {
  console.log("You clicked the blue button!");
  responseBox.style.backgroundColor='blue';

})
