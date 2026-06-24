// Encode input for prevent XSS
function htmlEncode(hash){
  return $("<div />").text(hash).html();
}

if( $('main.commitment-to-sdgs ul.goals').length ) {
  const sdgsHash = htmlEncode(window.location.hash.split("#")[1]);

  if ( sdgsHash ) {
    $('ul.goals .trigger_area, ul.goals .content_area').removeClass('active');

    const sdgTrigger = $('[data-jq-switcher-trigger='+sdgsHash+']') // 加減號切換
    const sdgTarget = $('[data-jq-switcher-target='+sdgsHash+']') // 展開內容切換

    sdgTrigger.addClass('active');
    sdgTarget.addClass('active').delay( 800 );

    sdgTarget.promise().done(function() {
      $('html, body').animate({
        scrollTop: sdgTrigger.offset().top - 72 - 23,
      }, 1000, function() {
        // console.log($('[data-jq-switcher-trigger='+sdgsHash+']').offset().top);
      });
    });
  }
}