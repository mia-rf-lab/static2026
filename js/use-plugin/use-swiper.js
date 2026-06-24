import renderRandomNum from '../modules/renderRandomNum.js';

// Home - KV
if ( $('.js-home-kv-slider').length ) {
  var sliderHomeKv = new Swiper(".js-home-kv-slider", {
    loop: true,
    longSwipesRatio: 0.3,
    slidesPerView: 1,
    spaceBetween: 0,
    autoplay: {
      delay: 5000,
      pauseOnMouseEnter: true,
      disableOnInteraction: false,
    },
    pagination: {
      el: '.home-kv-dots',
      bulletClass: 'dot',
      bulletActiveClass: 'active',
      clickable: true,
      renderBullet: function (index, className) {
        return `<span class="${className}"><span></span></span>`;
      }
    },
    navigation: {
      nextEl: ".home-kv-next",
      prevEl: ".home-kv-prev",
    },
  });
}


// Home - 關注焦點
if ( $('.swiper.topic').length ) {
  const homeFocusThumbSwiper = new Swiper('.topic-thumb .swiper', {
    loop: false,
    cssMode: true, // 此版 thumbs 功能會導致 slideChange 的 Transition 動畫與 grab 失效，故只能啟用 cssMode
    slidesPerView: 6,
    longSwipesRatio: 0.3,
    spaceBetween: 0,
    breakpoints: {
      320: {
        slidesPerView: 3,
      },
      506: {
        slidesPerView: 4,
      },
      650: {
        slidesPerView: 5,
      },
      778: {
        slidesPerView: 6,
      }
    },
    navigation: {
      prevEl: '.topic-thumb-prev',
      nextEl: '.topic-thumb-next',
    },
  });

  const homeFocusSwiper = new Swiper(".swiper.topic", {
    loop: false,
    grabCursor: true,
    simulateTouch: true,
    longSwipesRatio: 0.3, // Ratio to trigger swipe to next/previous slide during long swipes
    speed: 0,
    effect: 'fade',
    fadeEffect: {
      crossFade: true
    },
    thumbs: {
      swiper: homeFocusThumbSwiper,
    },
  });

  homeFocusSwiper.on('slideChangeTransitionEnd', function () {
    let targetObj = $(".swiper-slide-active em.num");
    renderRandomNum(targetObj, 1500);
  });
}


// 最新消息 - 影音專區
if ( $('.js-news-videos').length ) {
  var sliderNewsThumb = new Swiper(".js-news-thumb", {
    loop: false,
    longSwipesRatio: 0.3,
    slidesPerView: 4,
    spaceBetween: 5,
  });

  var sliderNewsVideos = new Swiper(".js-news-videos", {
    loop: false,
    longSwipesRatio: 0.3,
    slidesPerView: 1,
    spaceBetween: 0,
    navigation: {
      prevEl: ".news-videos-prev",
      nextEl: ".news-videos-next",
    },
    thumbs: {
      swiper: sliderNewsThumb,
    },
    on: {
      slideChange: function (el) {
        $('.yt_player_iframe').each(function(){
          this.contentWindow.postMessage('{"event":"command","func":"' + 'stopVideo' + '","args":""}', '*');
        });
      },
    },
  });
}


// 利害關係人溝通 - 外部倡議
if ( $('.js-materiality-analysis-propose').length ) {
  const swiper = new Swiper('.js-materiality-analysis-propose', {
    // autoHeight: true,
    loop: false,
    grabCursor: true,
    longSwipesRatio: 0.3,
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20,
      },
      768: {
        slidesPerView: 1,
        spaceBetween: 20,
      },
      1024: {
        slidesPerView: 2,
        spaceBetween: 40,
      },
      1360: {
        slidesPerView: 2,
        spaceBetween: 80,
      }
    },
    navigation: {
      prevEl: '.slider-propose-prev',
      nextEl: '.slider-propose-next',
    },
  });
}


// 關注焦點 - 重大議題策略與績效(timeline)
if ($('.js-timeline').length) {
  let timelineSwiper = Swiper; // Create a temp variable
  let timelineSwiperInit = false; // Trigger => off(default)

  function rwdTimelineSwiper() {
    let tablet = window.matchMedia('(max-width: 1023px)');
    let desktop = window.matchMedia('(min-width: 1024px)');

    // Map data attribute from swiper slides into a array
    let timelineDataArray = $(".js-timeline .swiper-slide")
      .map(function () {
        return [
          $.map($(this).data(), function (v) {
            return v;
          }),
        ];
      })
      .get();

    // Store Swiper setting in variable for reusing when windows resizing
    const timelineSwiperSetting = {
      loop: false,
      slidesPerView: 1,
      spaceBetween: 60,
      grabCursor: true,
      pagination: {
        el: '.timeline-pagination',
        bulletActiveClass: 'active',
        bulletClass: 'timeline-dot',
        clickable: true,
        renderBullet: function (index, className) {
          return (
            `<div class="${className}"><span>${timelineDataArray[index]}</span></div>`
          );
        },
      },
      navigation: {
        nextEl: ".timeline-next",
        prevEl: ".timeline-prev",
      },
    }

    // Enable (for larger than 768px)
    if(desktop.matches) {
      if (!timelineSwiperInit) { // 1. If trigger is off
        timelineSwiperInit = true; // 2. Turn it on
        timelineSwiper = new Swiper('.js-timeline', timelineSwiperSetting); // 3. Initialize swiper slider
      }
    }

    // Disable (for smaller than 767px)
    else if (tablet.matches) {
      if (timelineSwiperInit) { // 1. If trigger is on (如果沒有這個 if 判定， firefox 78.0.1 macOS 會報錯)
        timelineSwiperInit = false; // 2. Turn it off
        timelineSwiper.destroy(false, true); // 3. Destroy swiper slider, remove all swiper class, but not to delete Swiper instance(HTML elements)
      }
    }
  }

  rwdTimelineSwiper(); // Fire once

  $(document).ready(function() { // Add this row for new jQuery resize event snippet for a known bug that happened from iOS6 Safari.
    /* Store the window width */
    let windowWidth = $(window).width();

    $(window).resize(function(){
      // Check if the window width has actually changed and it's not just iOS triggering a resize event on scroll
      if ($(window).width() != windowWidth) {
        // Update the window width for next time
        windowWidth = $(window).width();
        // Do stuff below...
        rwdTimelineSwiper();
      }
    });
  });
}


// Component - gallery-slider
if ( $('.js-gallery-slider').length ) {
  $('.js-gallery-slider').each(function(index, gallerySlider) {
    const swiper = new Swiper(gallerySlider, {
      loop: false,
      grabCursor: true,
      longSwipesRatio: 0.3,
      breakpoints: {
        320: {
          slidesPerView: 1,
          spaceBetween: 0,
        },
        1024: {
          slidesPerView: 2,
          spaceBetween: 40,
        },
      },
      pagination: {
        el: '.dots',
        bulletClass: 'dot',
        bulletActiveClass: 'active',
        clickable: true,
      },
    });
  });
}