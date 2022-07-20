
document.querySelector('form').onsubmit = function () {
  var myHeaders = new Headers();
  myHeaders.append("apikey", "13MHSPiFpdwWoay3HQRhEE1wdkXK8USY");
  var requestOptions = {
    method: 'GET',
    redirect: 'follow',
    headers: myHeaders
  };

  fetch("https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols=GBP,JPY,EUR", requestOptions)
    .then(response => response.json())
    .then(data => {
      const currency = document.querySelector('#currency').value.toUpperCase();
      // Get rate from data
      const rate = data.rates[currency];
      // Display message on the screen
      console.log(data);
      // Check if currency is valid:
      if (rate !== undefined) {
        // Display exchange on the screen
        document.querySelector('#result').innerHTML = `1 USD is equal to ${rate.toFixed(3)} ${currency}.`;
      }
      else {
        // Display error on the screen
        document.querySelector('#result').innerHTML = 'Invalid Currency.';
      }
    })
    // Catch any errors and log them to the console
    .catch(error => {
      console.log('Error:', error);
    });
  // Prevent default submission
  return false;
} 