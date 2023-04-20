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

const accordiontitle = document.querySelectorAll('.content__item-title')
const accordionBox = document.querySelectorAll('.content__item-box')

accordiontitle.forEach((button, index) => {
  button.addEventListener('click', () => {

    if (button.classList.contains('content__title--active')){
      accordionBox[index].classList.remove('content__item--active')
      accordiontitle[index].classList.remove('content__title--active')
      return
    }

    for(let i = 0; i < accordionBox.length; i++) {
      accordionBox[i].classList.remove('content__item--active')
      accordiontitle[i].classList.remove('content__title--active')
    }

    accordionBox[index].classList.add('content__item--active')
    accordiontitle[index].classList.add('content__title--active')
  })
} )


        // for (let i = 0; i < toggles.length; i++) {
        //   toggles[i].addEventListener('click', () => {
        //     if (
        //       parseInt(contentDiv[i].style.height) != contentDiv[i].scrollHeight
        //     ) {
        //       contentDiv[i].style.height = contentDiv[i].scrollHeight + 'px'
        //       toggles[i].style.color = '#0084e9'
        //       icons[i].classList.remove('fa-plus')
        //       icons[i].classList.add('fa-minus')
        //     } else {
        //       contentDiv[i].style.height = '0px'
        //       toggles[i].style.color = '#111130'
        //       icons[i].classList.remove('fa-minus')
        //       icons[i].classList.add('fa-plus')
        //     }

        //     for (let j = 0; j < contentDiv.length; j++) {
        //       if (j !== i) {
        //         contentDiv[j].style.height = 0
        //         toggles[j].style.color = '#111130'
        //         icons[j].classList.remove('fa-minus')
        //         icons[j].classList.add('fa-plus')
        //       }
        //     }
        //   })
        // }