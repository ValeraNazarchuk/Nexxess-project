// Selecting DOM elements
const paginationArrow = document.querySelectorAll('.content__pagination-arrow'),
  paginationNumbers = document.querySelectorAll('.content__pagination-button')

// Setting an initial step
let currentStep = 0

// Function to update the button states
const updateBtn = () => {
  // If we are at the last step
  if (currentStep === paginationNumbers.length - 1) {
    paginationArrow[1].disabled = true
  } else if (currentStep === 0) {
    // If we are at the first step
    paginationArrow[0].disabled = true
  } else {
    paginationArrow[1].disabled = false
    paginationArrow[0].disabled = false
  }
}

// Add event listeners to the numbers
paginationNumbers.forEach((number, numIndex) => {
  number.addEventListener('click', (e) => {
    // Set the current step to the clicked number
    currentStep = numIndex
    // Remove the "pagination--active" class from the previously active number
    document
      .querySelector('.pagination--active')
      .classList.remove('pagination--active')
    // Add the "pagination--active" class to the clicked number
    number.classList.add('pagination--active')
    updateBtn() // Update the button states
  })
})

// Add event to the "Previous" and "Next" buttons
paginationArrow.forEach((button) => {
  button.addEventListener('click', (e) => {
    // Increment or decrement the current step based on the button clicked
    currentStep += e.target.closest('button').id === 'next' ? 1 : -1
    paginationNumbers.forEach((number, numIndex) => {
      // Toggle the "pagination--active" class on the number based on the current step
      number.classList.toggle('pagination--active', numIndex === currentStep)
      updateBtn() // Update the button states
    })
  })
})