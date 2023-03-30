const LoginForm = document.querySelector('.authentication__login')
const forgotBtn = document.querySelector('.authentication__login-forgot')
const passwordForm = document.querySelector('.authentication__password')
const backBtn = document.querySelector('.authentication__password-back')

forgotBtn.addEventListener('click', () => {
  LoginForm.style.display = 'none'
  passwordForm.style.display = 'flex'
})

backBtn.addEventListener('click', () => {
  passwordForm.style.display = 'none'
  LoginForm.style.display = 'flex'
})

