import renderRandomNum from './renderRandomNum.js';

const iOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
if ('IntersectionObserver' in window && !iOS) { // Detect browser support "IntersectionObserver" or not

  // [Custom Function] Detect elements is visible or not by Intersection Observer API
  let observer = new IntersectionObserver(function(entries) {

    entries.forEach(function (entry) {

      if ( entry.intersectionRatio > 0.01 ) {

        if (entry.target.querySelectorAll(".home .section--focus .swiper-slide-active").length > 0 ) {
          let targetObj = $(".section--focus .swiper-slide-active em.num");
          renderRandomNum(targetObj, 1500);
          observer.unobserve(entry.target); // turn-off observer for this entry after fire once
        }

        else if (entry.target.querySelectorAll("em.num").length > 0 ) {
          let targetObj = $("em.num");
          renderRandomNum(targetObj, 1000);
        }

        // If target is visible in the screen
        entry.target.classList.add('animated');

        if (!$("html").hasClass("dev")) {
          observer.unobserve(entry.target); // turn-off observer for this entry after fire once
        }

      }

      else if ( entry.intersectionRatio < 0.01 && $('html').hasClass('dev') ) {

        // If target is 'not' visible in the screen
        entry.target.classList.remove('animated');

      }

    });

  }, {
    rootMargin: '0px 0px -20%',
    threshold: [0, 0.01, 0.1, 0.2]
  });

  // [Custom JS] Detect elements is visible or not by Intersection Observer API
  const animeSections = document.querySelectorAll('.aos');
  animeSections.forEach(function (animeSection) {
    observer.observe(animeSection);
  });



  // [Custom Function] Detect current anchor active status by Intersection Observer API
  let observerAnchorStatus = new IntersectionObserver(function(entries) {
    const anchorMenu = $('ul.anchors-menu');

    entries.forEach(function (entry) {
      let anchorNum = entry.target.dataset.anchor;
      let anchorTar = anchorMenu.find('a[href="#' + anchorNum + '"]');

      if ( entry.intersectionRatio > 0.01 ) {
        anchorTar.addClass('active');
        // console.log(entry.target.className + ' is enter');
      } else if ( entry.intersectionRatio < 0.01 ) {
        anchorTar.removeClass('active');
        // console.log(entry.target.className + ' is out');
      }
    });
  }, {
    rootMargin: '-126px 0px -30%',
    threshold: [0, 0.01]
  });


  // [Custom JS] Detect elements is visible or not by Intersection Observer API
  const anchorSections = document.querySelectorAll('[data-anchor]');
  anchorSections.forEach(function (anchorSection) {
    observerAnchorStatus.observe(anchorSection);
  });

} else { // If browser not support 'IntersectionObserver' API, e.g. Safari before v12.1

  $('.aos').addClass('animated'); // Add class '.animated' to all '.aos' (animate on page loaded)

}