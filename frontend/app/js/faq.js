'use strict'

const accordionInfoBtn = document.querySelectorAll('#aside-info__accordion-top')
const accordionInfoList = document.querySelectorAll(
  '.aside-info__accordion-list'
)
const accordionInfoArrow = document.querySelectorAll('.aside-info__top-arrow')

accordionInfoBtn.forEach((button, index) => {
  button.addEventListener('click', (e) => {
    accordionInfoBtn[index].classList.toggle('accordion__top--active')
    accordionInfoList[index].classList.toggle('accordion__list--active')
    accordionInfoArrow[index].classList.toggle('accordion__arrow--active')
  })
})

//__________BURGER__________

const asideInfo = document.querySelector('.aside-info')
const burger = document.querySelector('.burger')

//____BURGER___
burger.addEventListener('click', menu)

function menu() {

  burger.classList.toggle('burger--active')
  asideInfo.classList.toggle('aside-info--active')
  
  if(document.body.classList.contains('body--active') && !burger.classList.contains('burger--active')) {
    document.body.classList.remove('body--active')
  } else {
    document.body.classList.add('body--active')
  }
}
