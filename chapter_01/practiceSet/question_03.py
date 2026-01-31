#Install an external module and use it to perform an operation of your interest. 

#pip install pyjokes .... to install 

import pyjokes

joke = pyjokes.get_joke()
print(joke)


#it will print random jokes 