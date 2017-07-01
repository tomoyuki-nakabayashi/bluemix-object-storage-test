const request = require('request');
const async = require('async');
const fs = require('fs');

var fileName = 'sample4_l.jpg';
fs.createReadStream(fileName).pipe(
  request({
    method: 'POST',
    url: 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify' + // eslint-disable-line
      '?api_key=bbe19e2884ee8607f73ed07cb79643a5521e0e4e' +
      '&version=2016-05-20',
    headers: {
      'Content-Length': fs.statSync(fileName).size
    },
    json: true
  }, (err, response, body) => {
    console.log('error:', err); // Print the error if one occurred
    console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
    console.log('body:', body); // Print the body.
    console.log('classes: ', body.images[0].classifiers[0].classes);
  }));
