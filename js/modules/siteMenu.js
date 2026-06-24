// Site Menu
const hamburger = $('.site-header .hamburger');
const htmlTag = $('html');
let bslTargetElement; // BodyScrollLock Element

// Click hamburger icon to open/close menu
$('.site-header .hamburger, nav.menu a:not([href="javascript:;"])').click(function(){

  if ( hamburger.css('display') !== 'none' ) {

    let bslTargetElement = document.querySelector('.site-header .rwd-panel');

    // Condition for checking menu actived or not.
    if( !htmlTag.hasClass('rwd-menu-active') ){

      // If menu have not active, add classes to make CSS open it.
      htmlTag.addClass('rwd-menu-active no-scroll');
      bodyScrollLock.disableBodyScroll(bslTargetElement);

    } else {

      // If menu already actived, remove above added classes to close menu.
      htmlTag.removeClass('rwd-menu-active no-scroll');
      bodyScrollLock.clearAllBodyScrollLocks();
    }

  };

});


$(window).resize(function(){
  // Close RWD menu & cancel bodyScrollLocks.
  $('html').removeClass('rwd-menu-active no-scroll');
  bodyScrollLock.clearAllBodyScrollLocks();
});


// Open sub menu in site menu on mobile size screen.
$('.menu-item-has-children > a').click(function(e){
  $(this).toggleClass('active');
  $(this).next('.sub-menu').toggleClass('active');
});