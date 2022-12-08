const $ = window.$;
const url = 'https://stefanbohacek.com/hellosalut/?lang=fr';
$('document').ready(function () {
  $.getJSON(url, function (response) {
    $('DIV#hello').text(response.hello);
  });
});
