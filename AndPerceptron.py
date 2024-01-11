# Helina Asadi           3rd practice
# AND function , Learning Algorithm : Single-layer Perceptron , Binary Inputs & Bipolar Targets , Threshold Activation Function
# alpha (learning rate) = 1     ,     theta (threshold) = 0.2

# INITIALIZING WEIGHTS
w0 = 0
w1 = 0
bias = 0
# SETTING LEARNING RATE
alpha = 1
# SETTING THE THRESHOLD
theta = 0.2


# SAMPLES & TARGETS :
# x0 , x1 , t (as in target)
samples = [[1 ,1 ,1],
           [1, 0, -1],
           [0, 1, -1],
           [0, 0, -1]]

# START LEARNING :
print("Learning starts now")
flag = True
while flag :
    w0compare = w0
    w1compare = w1
    biascompare = bias
    for sample in samples :
        # Calculating Y NetInput and f(YNI) with threshold
        YNI = w0*sample[0] + w1*sample[1] + bias
        if YNI > theta :
            fYNI = 1
        elif -theta <= YNI <= theta :
            fYNI = 0
        else :
            fYNI = -1     # for YNI less than theta
        # Updating weights ONLY if there is a mismatch
        if fYNI != sample[2] :
            w0 += alpha * sample[0] * sample[2]
            w1 += alpha * sample[1] * sample[2]
            bias+=alpha * sample[2]


    # TERMINATION CONDITION :
    # if there is no change in weights through one whole epoch, then terminate learning
    if w0compare==w0 and w1compare==w1 and biascompare==bias :
        flag = False



# TESTING
while True :
    # GETTING INPUT
    userInput = input("\nEnter input1 and input2 repectively "
                      "\nSeperate with space : ").split()

    input1 = int(userInput[0])
    input2 = int(userInput[1])


    # CLASSIFING

    def sign(x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0


    output = sign(w0 * input1 + w1 * input2 + bias)
    if output == 1:
        AND = "True"
    elif output == -1:
        AND = "False"
    else :
        AND = "output is right on the border ; unable to classify"
    print("\noutput is" ,output , ":" , AND)