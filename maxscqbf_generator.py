from typing import List
import random

def generateInstance(name: str, n: int, subsetsSize: int):
    # create n empty subsets
    S = [set() for _ in range(n)]

    ensureUniverseCovered(n, S)
    ensureNonEmptySubsets(n, S)

    universe = set(range(n))

    # add exactly "subsetSize" vars to each subset S[i]
    for i in range(n):
        if len(S[i]) >= subsetsSize:
            continue
        
        candidateVars = list(universe - S[i])
        varsToBeAdded = random.sample(candidateVars, subsetsSize - len(S[i]))
        S[i].update(varsToBeAdded)


    A = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n - i):
            val = round(random.uniform(-100, 100), 2)
            A[i][i + j] = val
    
    writeInstanceToFile(name, n, S, A)

def ensureUniverseCovered(n: int, S: List[set[int]]):
    # the union of all subsets must cover the universe
    # to satisfy this, for each variable k, we add it to at least one subset i
    for k in range(n):
        i = random.randint(0, n - 1)
        S[i].add(k)

def ensureNonEmptySubsets(n: int, S: List[set[int]]):
    # to guaranty all subsets not being empty
    # add at least one variable for each subset
    for i in range(n):
        if len(S[i]) == 0:
            randomVar = random.randint(0, n - 1)
            S[i].add(randomVar)    

def writeInstanceToFile(name: str, n: int, S: List[set[int]], A: List[List[float]]):
    with open(f"{name}.txt", "w") as f:
        f.write(f"{n}\n")
        for i in range(n):
            sizeSi = len(S[i])
            if i == n - 1:
                f.write(f"{sizeSi}\n")
            else:
                f.write(f"{sizeSi} ")

        for i in range(n):
            elemIdx = 0
            for elem in S[i]:
                if elemIdx == len(S[i]) - 1:
                    f.write(f"{elem + 1}\n")
                else:
                    f.write(f"{elem + 1} ")
                elemIdx += 1

        for i in range(n):
            for j in range(n - i):
                aij = A[i][i + j]
                if j == n - i - 1:
                    f.write(f"{aij}\n")
                else:
                    f.write(f"{aij} ")


if __name__ == "__main__":
    instanceName = "teste3"
    generateInstance(instanceName, n=100, subsetsSize=50)