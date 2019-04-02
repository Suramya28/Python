
def solution(A):
    print(sorted(A));

    if max(A)<1:
        return 1;

    else:
        
        for a in range(1,max(A)):
            if a not in A:
                break;
    return a;
            
    

print(solution([-1, 1,2,4]));
            
    
            







    

        

    

