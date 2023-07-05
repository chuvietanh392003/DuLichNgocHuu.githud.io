// Function to execute when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Code here will be executed once the DOM is fully loaded
  
    // Example: Change the text content of an element
    var heading = document.querySelector('h1');
    heading.textContent = 'Hello, World!';
  
    // Example: Add an event listener to a button
    var button = document.querySelector('#myButton');
    button.addEventListener('click', function() {
      alert('Button clicked!');
    });
  
    // Example: Fetch data from an API
    fetch('https://api.example.com/data')
      .then(response => response.json())
      .then(data => {
        // Process the retrieved data
        console.log(data);
      })
      .catch(error => {
        // Handle any errors that occurred during the fetch
        console.error(error);
      });
  });
  