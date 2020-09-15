#!/usr/bin/node
const num = process.argv[2];
function factorialRecursivo (n) { 
	if (n == 0){ 
		return 1; 
	}
	return n * factorialRecursivo (n-1); 
}
console.log(factorialRecursivo(parseInt(num)));
