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

console.log("Running Click Events Script");
const clickedRedBox = document.querySelector('#box1')
clickedRedBox.addEventListener('click', changeColor(clickedRedBox))

const clickedPinkBox = document.querySelector('#box2')
clickedPinkBox.addEventListener('click', changeColor(clickedPinkBox))

const clickedOrangeBox = document.querySelector('#box3')
clickedOrangeBox.addEventListener('click', changeColor(clickedOrangeBox))

function changeColor(box)
{
  return () => {
    const boxOne = document.querySelector('#box1')
    const boxTwo = document.querySelector('#box2')
    const boxThree = document.querySelector('#box3')
    boxOne.style.backgroundColor = window.getComputedStyle(box).backgroundColor
    boxTwo.style.backgroundColor = window.getComputedStyle(box).backgroundColor
    boxThree.style.backgroundColor = window.getComputedStyle(box).backgroundColor
  }
}
