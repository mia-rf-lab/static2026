// [Plugin] Cookies.js - Browser Notification Popup
if ( !Cookies.get('browser_notification') ) {
  $('.browser-notification').addClass('active');

  $('.browser-notification span').click(function () {
    $(this).parents('.browser-notification').addClass('ttt').removeClass('active');
    Cookies.set('browser_notification', 'confirmed', { expires: 365, sameSite: 'lax', secure: true })
  });
}