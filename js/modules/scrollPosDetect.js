function scrollPosDetect() {
  let webPageScrollPosition = $(window).scrollTop();
  let scrollTriggerPos   = 72; // Header height (px).

  if (webPageScrollPosition > scrollTriggerPos) {
    $('.sticky').addClass('active');
  } else {
    $('.sticky').removeClass('active');
  }
};

scrollPosDetect(); // Fire once when page loaded

$(window).scroll(function(){
  scrollPosDetect(); // Fire when page scrolled
})