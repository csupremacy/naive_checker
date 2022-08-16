#Test Answers checker
     

def verify(correctanswers):
    assert(isinstance(correctanswers, list))
    
    result = []
    
    print("Input the given answers separated by spaces. If no answer is given, input a /:\n")
    c = input()
    c = c.split()
    
    errorreport = ""
    
    for i in range(len(correctanswers)):
        if correctanswers[i] == c[i]:
            result.append(1)
        else:
            result.append(0)
            errorreport += "Mistake in %d!"%(i + 1) + " Should be \"" + correctanswers[i] + "\".\n"

    return (str(round(sum(result) / len(result) * 100, 2)) + "%\n"), errorreport

def main():
    taskcount = 0
    print("How many tasks are there?\n")
    taskcount = int(input())
    f =  open("feedback.txt", "w")
    f.write("Your results are as follows:\n")
    for v in range(taskcount):
        print("What is the task #%d?\n"%(v + 1))
        tname = input()
        print("Input the correct answers separated by spaces:\n")
        correct = input()
        percentage, errors = verify(correct.split())
        f.write("Results in " + tname + ".\n")
        f.write(errors)
        f.write(percentage + "\n")
    f.close()
    print("Your results have been recorded in feedback.txt.")
    return 0
    
if __name__ == "__main__":
    main()





