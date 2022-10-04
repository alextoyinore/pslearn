/**
 * redirects the document to the home page
 */

/* const logo = document.querySelector('.logo')
logo.addEventListener('click', function(){
    console.log('logo cliked!')
    window.location.assign("/")
}) */

/**
 * hides nav links and streches out search box
 */

 const search = document.querySelector('.search')
 const horizontal_nav_links = document.querySelector('.horizontal-nav-links')
 
 search.addEventListener('focus', function(){
     horizontal_nav_links.style.display = 'none'
     search.style.width = '50%'
 })