# Helina Asadi
# OR function , Hebbian Learning Algorithm , Bipolar Encoding


# INITIALIZING WEIGHTS
w0 = 0
w1 = 0
bias = 0


# SAMPLES & TARGETS :
# x0 , x1 , t (as in target)
samples = [[1 ,1 ,1],
           [1, -1, 1],
           [-1, 1, 1],
           [-1, -1, -1]]


# START LEARNING :
print("Learning starts now")
for sample in samples:

   w0 = w0 + sample[0]*sample[2]
   w1 = w1 + sample[1]*sample[2]
   bias = bias + sample[2]
   print("\nJust finished leaning a sample. Updates weights are :"
         "\nw0 :" ,w0 , " ,  w1 :" ,w1 , " ,  bias :" ,bias )


# ACTIVATION FUNCTION : Sign
   def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


# TESTING
# GETTING INPUT
while True :
    userInput = input("\nEnter input1 and input2 repectively "
                      "\nSeperate with space : ").split()

    input1 = int(userInput[0])
    input2 = int(userInput[1])


    output = sign(w0 * input1 + w1 * input2 + bias)
    if output == 1:
        AND = "True"
    elif output == -1:
        AND = "False"
    else :
        AND = "output is right on the border ; unable to classify"
    print("\noutput is" ,output , ":" , AND)