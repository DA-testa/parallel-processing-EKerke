# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    finishTime = [0] * n #inicializē masīvu ar n skaita nullēm, kas reprezentē laiku katra thread pabeigšanai 

    assignJobs = [(0,0)] * m #inicializē masīvu ar m tuples kur uzkrāj thread indeksu un katra darba uzsākšanas laiku 

    for i in range(m): 
        jobTime = data[i] 
        minFinishTime = finishTime[0] 
        minThread = 0  
        for j in range(n): 
            if finishTime[j] < minFinishTime: 
                minFinishTime = finishTime[j] 
                minThread = j 
        assignJobs[i] = (minThread, finishTime[minThread]) 
        finishTime[minThread] += jobTime

    output = [(assignJobs[i][0], assignJobs[i][1]) for i in range(m)] # izveido sarakstu ar izvadāmajiem pāriem

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split()) #reads the values of n and m from the keyboard

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = [] 
    data = list(map(int, input().split()))


    # TODO: create the function
    result = parallel_processing(n,m,data) 
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result: 
        print(i, j) 



if __name__ == "__main__":
    main()
