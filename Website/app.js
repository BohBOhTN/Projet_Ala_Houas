document.querySelectorAll('li').forEach(item => {
    item.addEventListener('click', function() {
      const userChoice = item.textContent;
      triggerLambdaFunction(userChoice);
    });
  });
  
  function triggerLambdaFunction(choice) {
    console.log('So you are interrested in :', choice);
  }