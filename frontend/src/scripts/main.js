'use strict'

const accordionBtn = document.querySelectorAll('.aside__accordion-top')
const accordionList = document.querySelectorAll('.aside__accordion-list')

accordionBtn.forEach((button, index) => {
  button.addEventListener('click', (e) => {
    accordionList[index].classList.toggle('aside__accordion-active')
    
  })
})
