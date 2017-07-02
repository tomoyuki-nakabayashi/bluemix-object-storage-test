const request = require('request');
const fs = require('fs');

var params = {
   "classifier_ids":[
      "traffic_1621924048"
   ],
   "threshold":0.1
}

var fileName = 'sample4_l.jpg';
var formData = {
  images_file: fs.createReadStream(__dirname + '/sample4_l.jpg'),
  parameters: JSON.stringify(params)

};

request({
  method: 'POST',
  url: 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify' + // eslint-disable-line
    '?api_key=bbe19e2884ee8607f73ed07cb79643a5521e0e4e' +
    '&version=2016-05-20',
  formData: formData
}, (err, response, body) => {
  console.log('error:', err); // Print the error if one occurred
  console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
  console.log('body:', body); // Print the body.
});
