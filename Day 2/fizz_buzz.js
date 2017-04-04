/**
 * Created by Josh on 4/4/17.
 */

function fizzBuzz(number){
  if (number%3===0){
    if (number%5===0){
      return ("FizzBuzz");
    }
    else{
      return ("Fizz");
    }
    }
  else if (number%5===0){
    return ("Buzz");
  }
  else{
    return number
  }
}