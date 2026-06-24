// Embed multiple youtube iframe
$( ".videos-slider .youtube" ).each(function() {
  let ytVideoId = $( this ).attr("id");

  // Based on the YouTube ID, we can easily find the thumbnail image
  let ytThumbnailImg = document.createElement("img");
  let ytMaxResThumbnail_url = "https://i.ytimg.com/vi/" + ytVideoId + "/maxresdefault.jpg"; // High resolution (1080p) thumbnail
  let ytHqThumbnail_url = "https://i.ytimg.com/vi/" + ytVideoId + "/hqdefault.jpg"; // Default resolution(360p) thumbnail

  ytThumbnailImg.setAttribute("class", "thumb"); // Add a class name for CSS styling
  ytThumbnailImg.setAttribute("src", ytMaxResThumbnail_url); // Use high resolution image

  // Detect Youtube video has a high resolution (1080p) thumbnail or not
  ytThumbnailImg.onload = function() {
    // console.log(ytThumbnailImg.naturalHeight);

    // If youtube return a base64 gif image(120*90) - in other words: no high resolution (1080p) thumbnail found
    if( ytThumbnailImg.naturalHeight <= 90 ) {
      ytThumbnailImg.setAttribute("src", ytHqThumbnail_url); // Use default resolution image
    }
  }

  $( this ).append(ytThumbnailImg);

  // Attach an onclick event to the YouTube Thumbnail to trigger embed iframe dynamically
  $( this ).click(function(){

    // Create an iFrame with autoplay set to true
    let ytIframe = document.createElement("iframe");
    ytIframe.setAttribute("src", "https://www.youtube.com/embed/" + ytVideoId + "?autoplay=1&autohide=1&border=0&wmode=opaque&enablejsapi=1");

    // Add class name for stop playing video after swiper slide changed
    ytIframe.setAttribute("class", "yt_player_iframe");

    // The height and width of the iFrame should be the same as parent
    ytIframe.style.width  = this.style.width;
    ytIframe.style.height = this.style.height;

    // Replace the YouTube thumbnail with YouTube HTML5 Player
    this.parentNode.replaceChild(ytIframe, this);

  });
});